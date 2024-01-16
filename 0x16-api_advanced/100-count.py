#!/usr/bin/python3
"""100-count module."""
import requests


def count_words(subreddit, word_alist, word_acounts=[], after=None):
    """
    Recursively query the Reddit API, parse post titles, and print word counts.

    Args:
        subreddit (str): The subreddit to search.
        word_alist (list): List of words to count.
        result_list (list): List of word occurrences.
        after (str): Token for pagination.

    Returns:
        None: The results are printed directly.
    """
    user_agent = {'User-agent': 'kabandapatrick2580'}
    posts = requests.get(
            f'http://www.reddit.com/r/{subreddit}/hot.json?after={after}',
            headers=user_agent
            )

    if after is None:
        word_alist = [word.lower() for word in word_alist]

    if posts.status_code == 200:
        posts_data = posts.json()['data']
        next = posts_data['after']
        posts = posts_data['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_alist:
                    word_acounts.append(word)

        if next is not None:
            count_words(subreddit, word_alist, word_acounts, next)
        else:
            output = {}
            for word in word_acounts:
                if word.lower() in output:
                    output[word.lower()] += 1
                else:
                    output[word.lower()] = 1

            for key, value in sorted(
                    output.items(),
                    key=lambda item: (item[1], item[0]),
                    reverse=True
                    ):
                print(f'{key}: {value}')
    else:
        return
