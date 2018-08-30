#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        return number of subscribers for a given subreddit
        return 0 if invalid subreddit given
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # get user agent
    # https://stackoverflow.com/questions/10606133/ -->
    # sending-user-agent-using-requests-library-in-python
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get(url, headers=headers).json()
    subscribers = r.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
