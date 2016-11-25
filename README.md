# Clicktripz Pacing Algorithm Test

When advertisers decide to buy impressions from an ad-network, they buy 
them in advance in bulk. For example, Tripadvisor might buy 2,000,000 
impressions of their new "book direct" campaign at 0.01c per impression.

Pacing is about how fast the purchased impressions are delivered on the 
network. There are usually two kinds of industry "paces". The first one 
is "fast" pacing, which means the impressions are delivered as soon as 
they are available. The second, more commonly used pacing, is "even" 
pacing. In "even" pacing mode, the impressions are evenly distributed
across some time period. That means if a campaign is supposed to show 24
impressions in a day, you would expect to see 1 impression per hour, 
instead of 24 impressions in the first minute.

Implementing such a strategy involves an algorithm to decide 
how much to govern or slow-down the impressions being delivered for the 
advertiser. 

Here is an [example](http://rubiconproject.com/technology-blog/using-proportional-control-for-better-pacing/) of how Rubicon (an ad network) does pacing.

Some key points to know about ad networks (and this test) are:

* How many impressions you can show at any time is purely based on the 
type of websites you have in your network.

* The bandwidth of impressions that you can show can change second to 
second, and is impossible to predict.

* You won't be able to decide how much you want to slow down your 
impression count on a real-time, impression to impression basis. You 
need to allow some number N impressions to be shown before you can update
your algorithm. This number N is based on the refresh rate of the campaign.

## Test

Your job is to implement the `Pacer` class in pacer.py. The `Pacer` class is
used by `ImpressionGenerator` in campaign.py to limit the number of
impressions shown per cycle.

All tests should pass (regardless of how many times they are run) for 
this project to be considered complete.

## Rules

* You cannot change the function signature of `calculate_throttle_rate` 
or `__init__`, but you can add new function methods as you see fit.

* You cannot change tests.py

* You cannot change campaign.py

* Only standard libs

## Usage

You will need to install [Docker](https://docs.docker.com/engine/installation/)

See Makefile and Dockerfile.

## Turning it in

Once your `Pacer` class is implemented, send the whole pacer.py file as 
an email to:

> to: jobs@clicktripz.com

> subject: \<Your Name\> Python Backend Test

> body: any comments + gist of `Pacer` implementation
