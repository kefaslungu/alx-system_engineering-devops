#!/usr/bin/python3
"""
gathers data from API and exports it to JSON file
"""
import json
import requests
import sys

"""REST API url"""

if len(sys.argv) < 2:
    print("Please provide an employee ID")
    sys.exit(1)

EMPLOYEE_ID = sys.argv[1]
API_URL = f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}/todos"

response = requests.get(API_URL)
tasks = response.json()

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

with open(f"{EMPLOYEE_ID}.json", 'w') as f:
    json.dump(tasks_by_user, f)
