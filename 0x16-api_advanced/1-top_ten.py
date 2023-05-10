#!/usr/bin/python3
"""
Titles of first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    queries and prints the titles of the first 10 hot posts listed
    for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return "None"

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    agent = {'User-agent': 'Google Chrome Version 113.0.5672.63'}
    response = requests.get(url, headers=agent, params={'limit': 10})
    results = response.json()

    try:
        hot_reddits = results.get('data').get('children')
        for hot in hot_reddits:
            print(hot.get('data').get('title'))
    except Exception:
        return "None"
