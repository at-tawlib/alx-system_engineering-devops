#!/usr/bin/python3
"""
get subscribers count from Reddit API for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    response = requests.get(url, headers=agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')
    except Exception:
        return 0
