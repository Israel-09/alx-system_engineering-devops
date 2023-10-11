#!/usr/bin/python3
'''
retrives information from reddit api
'''
import requests


def top_ten(subreddit):
    '''retrieves top ten post from a subreddit

    Args:
        subreddit (str): the subreddit
    '''
    if subreddit is None or str(subreddit).isalpha() is False:
        print("None")
        return

    headers = {'User-Agent': "Microsoft edge 117.0.2045.47"}
    url = "https://www.reddit.com/r/{}.json?limit=8".format(subreddit)
    response = requests.get(url, headers=headers)

    try:
        data = response.json().get("data")
        posts = data.get("children")
        for post in posts:
            post_data = post.get('data')
            print("{}".format(post_data.get('title')))
    except Exception:
        print("None")
