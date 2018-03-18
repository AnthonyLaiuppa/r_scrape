r_scrape
======

I was tired of having to watch reddit myself, so I created this simple tool to do it for me. 

It works using reddits api, slack, and config.json.

It watches for posts in real time that come to your subreddit of choice, then checks them for keywords.

If there are keyword matches it notifies you in slack. 

Its fairly easy to use, fill out the config.json.

_You will need to create an api on reddit to get a token, and a bot on slack to get a token for that too._

Next 

> pip install -r requirements.txt
> python run.py
