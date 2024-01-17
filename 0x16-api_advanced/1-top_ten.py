#!/usr/bin/python3
"""web scrapping lessons"""
from requests import get


def top_ten(subreddit):
    """prints the title of the first ten hot subreddit post"""
    uri = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
                "User-Agent": "python-requests/2.31.0"
              }

    r = get(uri, headers=headers)

    try:
        if r.status_code != 200:
            print(None)
        else:
            posts = r.json().get('data').get('children')
            for i in range(10):
                title = posts[i].get('data').get('title')
                print(title)
    except Exception:
        print(None)
