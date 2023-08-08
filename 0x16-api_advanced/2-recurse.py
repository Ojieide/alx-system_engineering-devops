#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after_url=''):
	"""
	Returns a list containing the titles of all hot articles for a
    given subreddit
	"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=1{}'.format(
        subreddit, after_url)
    response = requests.get(url, allow_redirects=False, headers={
                            "User-Agent": "api_advanced-project"})
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        for child in data['data']['children']:
            title = child['data']['title']
            hot_list.append(title)
        if data['data'].get('after'):
            after_url = '&after={}'.format(data['data']['after'])
            recurse(subreddit, hot_list, after_url)
        return hot_list
