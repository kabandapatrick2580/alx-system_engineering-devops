#!/usr/bin/python3
"""Exporting information of employees using JSON format"""

# Importing the necessary modules
import json
import requests

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Define the base URL for the REST API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetching the list of users from the API
    users = requests.get(url + "users").json()

    # Writing employee tasks information to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(
            # Creating a dictionary comprehension to structure the JSON data
            {
                p.get("id"): [
                    {
                        "task": q.get("title"),
                        "completed": q.get("completed"),
                        "username": p.get("username")
                    }
                    # Fetching the TODO tasks for each user
                    for q in requests.get(
                        url + "todos",
                        params={"userId": p.get("id")}
                    ).json()
                ]
                # Iterating through each user
                for p in users
            },
            # Writing the dictionary to the JSON file
            jsonfile
        )
