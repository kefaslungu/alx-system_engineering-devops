#!/usr/bin/python3
"""
returns info about employee TODO progress
"""
import sys
import requests

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Get employee information
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee = response.json()
employee_name = employee['name']

# Get employee's TODO list
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
todos = response.json()

# Calculate TODO progress
total_tasks = len(todos)
done_tasks = sum(todo['completed'] for todo in todos)

# Print progress report
print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo['completed']:
        print(f"\t {todo['title']}")
