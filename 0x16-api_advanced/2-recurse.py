#!/usr/bin/python3
"""
Recursive function that queries a Reddit
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    recursive functions the queries teh reddit and returns a
    list containing the titles of all hot articles of a subreddit
    """
    global after

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    agent = {'User-agent': 'Google Chrome Version 113.0.5672.63'}
    response = requests.get(url, headers=agent, params={'after': after},
                            allow_redirects=False)

    if response.status_code == 200:
        after_results = response.json().get('data').get('after')
        if after_results is not None:
            after = after_results
            recurse(subreddit, hot_list)
        titles = results.json().get('data').get('children')
        for title in titles:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        return None
