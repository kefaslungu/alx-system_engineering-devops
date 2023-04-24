#!/usr/bin/python3
"""
gathers data from API and exports it to CSV file
"""
import csv
import requests
import sys

"""REST API url"""

if len(sys.argv) < 2:
    sys.exit("Usage: python3 1-export_to_CSV.py <employee_id>")

# get the id of the person
employee_id = sys.argv[1]

# get the users url and tasks
url_user = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
url_tasks = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

# get the users data and tasks data
user_data = requests.get(url_user).json()
task_data = requests.get(url_tasks).json()

# Get employee information
employee_name = user_data['name']
filename = "{}.csv".format(employee_id)
# create the file
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for task in task_data:
        completed = task['completed']
        title = task['title']

        writer.writerow({
            'USER_ID': employee_id,
            'USERNAME': employee_name,
            'TASK_COMPLETED_STATUS': str(completed),
            'TASK_TITLE': title
        })

# print what ever.
print("Data exported to {}".format(filename))
