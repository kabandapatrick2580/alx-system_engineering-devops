#!/usr/bin/python3

# Importing the 'get' function from the 'requests' module
from requests import get

def number_of_subscribers(subreddit_name):
    """
    Get the number of subscribers for a given subreddit.

    Parameters:
    - subreddit_name (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers or 0 if an error occurs.
    """

    # Check if the subreddit_name is valid
    if subreddit_name is None or not isinstance(subreddit_name, str):
        return 0

    # Construct the URL for the subreddit information
    subreddit_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit_name)
    
    # Set the user-agent header to avoid issues with Reddit API
    request_headers = {'User-Agent': 'Patrick'}

    # Make a GET request to the Reddit API
    response = get(subreddit_url, headers=request_headers)
    
    # Parse the JSON response
    response_data = response.json()

    try:
        # Extract the number of subscribers from the JSON response
        subscribers_count = response_data.get('data').get('subscribers')
        return subscribers_count

    except Exception:
        # Return 0 if there's an exception during the extraction
        return 0
