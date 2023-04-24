#!/usr/bin/python3
"""
This script retrieves data from a REST API and exports it to a JSON file.

Usage:
    ./2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys

# check if employee ID is provided
if len(sys.argv) < 2:
    print("Please provide an employee ID")
    sys.exit(1)

# retrieve employee ID from command-line argument
EMPLOYEE_ID = sys.argv[1]

# define REST API url
API_URL = f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}/todos"

# retrieve task data from API
response = requests.get(API_URL)
tasks = response.json()

# group tasks by user
tasks_by_user = {}
for task in tasks:
    if task['completed']:
        task_status = 'completed'
    else:
        task_status = 'not completed'
    tasks_by_user.setdefault(task['userId'], []).append({
        'task': task['title'],
        'completed': task_status,
        'username': task['username']
    })

# write tasks to JSON file
with open(f"{EMPLOYEE_ID}.json", 'w') as f:
    json.dump(tasks_by_user, f)
