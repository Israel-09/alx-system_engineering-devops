#!/usr/bin/python3
'''
retrives information from reddit api
'''
import requests


def number_of_subscribers(subreddit):
    '''number of a subreddit subscriber

    Args:
        subreddit (str): the subreddit
    Return:
        On success the amount of subscribers
        otherwise 0
    '''
    if subreddit is None or str(subreddit).isalpha() is False:
        return 0

    headers = {'User-Agent': "Microsoft edge 117.0.2045.47"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)

    try:
        return (response.json().get("data").get("subscribers"))
    except Exception:
        return 0
