#!/usr/bin/python3
"""Module for task 0"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'ALXReddit/0.1 by Achriki'}
    response = requests.get(url, headers=headers)
    if response.status_code >= 300:
        return 0

    return resonse.json().get("data").get("subscribers")
