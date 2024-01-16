#!/usr/bin/python3
"""Return the results using recursive functions."""
import requests


def recurse(subreddit, hot_list=None, a_after="", count_a=0):
    """
    Recursively query the Reddit API and count the total number of hot
    articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): List to store hot articles (used for recursion).
        a_after (str): A token for pagination (used for recursion).
        count_a (int): The count of hot articles (used for recursion).

    Returns:
        list or None: The list of hot articles or None if
        no results are found.
    """
    # Initialize hot_list if not provided
    if hot_list is None:
        hot_list = []

    # Reddit API endpoint URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Request headers
    headers = {
        "User-Agent": "kabandapatrick2580"
    }

    # Request parameters
    params = {
        "after": a_after,  # Corrected the key name
        "count": count_a,  # Corrected the key name
        "limit": 30
    }

    try:
        # Make the API request
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Check if subreddit is invalid (HTTP status code 404)
        if response.status_code == 404:
            return None

        # Extract relevant data from the API response
        results = response.json().get("data")
        a_after = results.get("after")
        count_a += results.get("dist")

        # Extract titles from each child and append to hot_list
        for child in results.get("children"):
            hot_list.append(child.get("data").get("title"))

        # If there are more results, recurse with updated parameters
        if a_after is not None:
            return recurse(subreddit, hot_list, a_after, count_a)  # Corrected the function name

        return hot_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
