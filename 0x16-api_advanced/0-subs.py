#!/usr/bin/python3
"""web scrapping"""
import requests


def number_of_subscribers(subreddit):
    """gets the number of subscribers to 
    a subreddit

    Args:
        subreddit (str): string of the subreddit.
    Return:
        on success return the number of subcribers to the 
        subreddit otherwise return 0.
    """
    headers = {
                "User-Agent": "python-requests/2.31.0"
              }
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    response = requests.get(url, headers=headers)
    try:
        if response.status_code != 200:
            return 0
        else:
            json_body = response.json()
            child = json_body.get('data').get("children")[0]
            no_of_subs = child.get('data').get("subreddit_subscribers")
            return (no_of_subs)
    except Exception as e:
        return 0
