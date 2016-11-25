import random
import pacer


class ImpressionGenerator:
    def __init__(self, max_demand=1):
        # likelihood of impression rate to remain the same
        self.recurrence_probability = 0.85
        self.raw_impressions_this_cycle = 1

        # percentage of impressions this cycle to block
        self.throttle_rate = 0.0
        # impressions after throttling
        self.adjusted_impressions_this_cycle = None

        # random upper limit to impressions per cycle
        self.demand = random.randint(1, max_demand)

    def update(self):
        transition_probability = random.random()
        if transition_probability > self.recurrence_probability:
            # naturally transition the raw impressions this cycle due to randomness of network websites
            self.raw_impressions_this_cycle = random.randint(1, self.demand)

        # throttle rate should've been set by the pacer in the cycle loop below
        if self.throttle_rate > 0.0:
            # impose a limit to number of impressions this cycle, based on a calculated throttle rate
            self.adjusted_impressions_this_cycle = round(self.raw_impressions_this_cycle * (1 - self.throttle_rate))
        else:
            self.adjusted_impressions_this_cycle = self.raw_impressions_this_cycle


class Campaign:
    def __init__(self, goal=0, cycles=0, refresh_rate=0, max_demand=1):
        # counter of actual impressions shown
        self.current_impressions = 0
        self.cycles = cycles
        # how often you can update your throttle rate
        self.refresh_rate = refresh_rate
        # used in tests.py to make sure the campaign is paced evenly through the entire time
        self.checkpoint_indexes = [int((cycles / 20) * x) for x in range(21)]
        # keeps track of actual impressions at every checkpoint
        self.checkpoint_impressions = []

        self.impression_generator = ImpressionGenerator(max_demand)
        self.campaign_impression_goal = goal
        self.pacer = pacer.Pacer(campaign_impression_goal=goal, refresh_rate=refresh_rate, total_cycles=self.cycles)

    """Run an ad campaign

    Loop over the time of a campaign and simulate displaying impressions.

    The goal is to distribute impressions evenly during the time of the campaign.

    This method will utilize the throttle rate provided by the Pacer object to control the rate of impressions.
    """
    def run_campaign(self):
        # below is the "cycle loop"
        for i in range(self.cycles + 1):
            if i % self.refresh_rate == 0:
                # update pacer with the new impression count since the previous refresh cycle
                self.pacer.impression_count = self.current_impressions
                # Pacer decides a throttle rate
                self.impression_generator.throttle_rate = self.pacer.calculate_throttle_rate()

                # calculate adjusted impressions until next cycle refresh
                self.impression_generator.update()

            # keep track of impression counts whenever a checkpoint is hit
            if i in self.checkpoint_indexes:
                self.checkpoint_impressions.append(self.current_impressions)
            self.current_impressions += self.impression_generator.adjusted_impressions_this_cycle
        return self


if __name__ == '__main__':
    print("Do not run the campaign library file, run `make tests` instead...Exiting")
