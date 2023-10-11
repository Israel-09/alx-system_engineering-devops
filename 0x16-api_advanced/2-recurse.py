#!/usr/bin/python2
"""
retrives information from an api
"""
from requests import get


def recurse(subreddit, hot_list=[], after=None) -> list:
    """
    recursively obtains a list of all the title of
    hot articles for a given subreddit

    Args:
        subredit (str): the provided subreddit.
        hot_list (list): a list of all article's title.
        after (str): this is the id of the thing for pagination
    Return:
        on success, a list of all article's title
        on failure, returns None.
    """

    if subreddit is None or str(subreddit).isalpha() is False:
        return None

    params = {
            'after': after,
            }
    headers = {'User-Agent': 'Microsoft edge v117.0.2045.47'}
    url = "https://www.reddit.com/r/{}/.json".format(subreddit)
    response = get(url, headers=headers, params=params)
    data = response.json().get('data')

    if data.get('dist') < 1:
        return hot_list

    try:
        articles = data.get('children')
        for article in articles:
            hot_list.append(article.get('data').get('title'))
        after = article.get('data').get('name')
        return recurse(subreddit, hot_list, after)
    except Exception:
        return None
