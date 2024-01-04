#!/usr/bin/python3
"""Script using REST API for an employee ID"""

# Importing the necessary module
import requests
import sys

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Extracting the employee ID from the command-line arguments
    employee_id = sys.argv[1]

    # Defining the base URL for the REST API
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    # Making a GET request to retrieve employee information
    response = requests.get(url)

    # Check if the employee was not found (HTTP status code other than 200)
    if response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    # Extracting the employee name from the JSON response
    employee_name = response.json().get('name')

    # Constructing the URL for the employee's TODO tasks
    todo_url = url + "/todos"

    # Making a GET request to retrieve the employee's TODO tasks
    response = requests.get(todo_url)
    tasks = response.json()

    # Initializing lists to store completed tasks and count the number of completed tasks
    tasks_done = []
    done = 0

    # Iterating through the tasks to find completed ones
    for task in tasks:
        if task.get('completed'):
            tasks_done.append(task)
            done += 1

    # Printing a summary of completed tasks for the employee
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))

    # Printing the titles of completed tasks
    for task in tasks_done:
        print("\t {}".format(task.get('title')))
