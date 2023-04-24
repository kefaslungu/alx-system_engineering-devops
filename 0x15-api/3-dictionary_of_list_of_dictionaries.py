#!/usr/bin/python3
"""
Exports all tasks from all employees in JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    # Set the API endpoint and fetch the JSON data
    api_url = "https://jsonplaceholder.typicode.com/"
    tasks = requests.get(api_url + "todos").json()
    users = requests.get(api_url + "users").json()

    # Convert the user data into a dictionary for easy access
    users_dict = {user['id']: user['username'] for user in users}

    # Create a dictionary to store tasks for each user
    tasks_by_user = {}

    # Populate the tasks_by_user dictionary
    for task in tasks:
        # Get the user ID for the current task
        user_id = task['userId']

        # Add the current task to the user's list of tasks
        if user_id in tasks_by_user:
            tasks_by_user[user_id].append({
                'task': task['title'],
                'completed': task['completed'],
                'username': users_dict[user_id]
            })
        else:
            tasks_by_user[user_id] = [{
                'task': task['title'],
                'completed': task['completed'],
                'username': users_dict[user_id]
            }]

    # Save the tasks_by_user dictionary to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_by_user, json_file)
