import unittest
import campaign


class TestPacer(unittest.TestCase):

    def test_large_campaign(self):
        print("\n---- Large Test Start")
        cycles = 86400 * 30
        goal = 50000 * 30
        refresh_rate = 10
        max_demand = 40
        c = campaign.Campaign(goal=goal, cycles=cycles, refresh_rate=refresh_rate, max_demand=max_demand).run_campaign()

        ideal_impression_counts_at_5_percent_increments = [int((goal / 20) * x) for x in range(21)]
        for i in range(len(ideal_impression_counts_at_5_percent_increments)):
            ideal_impression_count = ideal_impression_counts_at_5_percent_increments[i]
            actual_impression_count = c.checkpoint_impressions[i]
            delta = max(max_demand, round(ideal_impression_count * 0.05))
            print('Comparing ideal ({}) with actual ({}) to be within delta ({})'.format(ideal_impression_count,
                                                                                         actual_impression_count,
                                                                                         delta))
            self.assertAlmostEqual(actual_impression_count, ideal_impression_count, delta=delta)
        print("---- Large Test End")

    def test_small_campaign(self):
        print("\n---- Small Test Start")
        cycles = 86400
        goal = 50000
        refresh_rate = 3
        max_demand = 10
        c = campaign.Campaign(goal=goal, cycles=cycles, refresh_rate=refresh_rate, max_demand=max_demand).run_campaign()

        ideal_impression_counts_at_5_percent_increments = [int((goal / 20) * x) for x in range(21)]
        for i in range(len(ideal_impression_counts_at_5_percent_increments)):
            ideal_impression_count = ideal_impression_counts_at_5_percent_increments[i]
            actual_impression_count = c.checkpoint_impressions[i]
            delta = max(max_demand, round(ideal_impression_count * 0.05))
            print('Comparing ideal ({}) with actual ({}) to be within delta ({})'.format(ideal_impression_count,
                                                                                         actual_impression_count,
                                                                                         delta))
            self.assertAlmostEqual(actual_impression_count, ideal_impression_count, delta=delta)
        print("---- Small Test End")

    def test_tiny_campaign(self):
        print("\n---- Tiny Test Start")
        cycles = 60
        goal = 40
        refresh_rate = 1
        max_demand = 3
        c = campaign.Campaign(goal=goal, cycles=cycles, refresh_rate=refresh_rate, max_demand=max_demand).run_campaign()

        ideal_impression_counts_at_5_percent_increments = [int((goal/20) * x) for x in range(21)]
        for i in range(len(ideal_impression_counts_at_5_percent_increments)):
            ideal_impression_count = ideal_impression_counts_at_5_percent_increments[i]
            actual_impression_count = c.checkpoint_impressions[i]
            delta = max(max_demand, round(ideal_impression_count * 0.05))
            print('Comparing ideal ({}) with actual ({}) to be within delta ({})'.format(ideal_impression_count,
                                                                                         actual_impression_count,
                                                                                         delta))
            self.assertAlmostEqual(actual_impression_count, ideal_impression_count, delta=delta)
        print("---- Tiny Test End")

if __name__ == '__main__':
    unittest.main()
