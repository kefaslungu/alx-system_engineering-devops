#!/usr/bin/python3
"""
gathers data from API and exports it to CSV file
"""
import csv
import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Usage: python3 1-export_to_CSV.py <employee_id>")

# Get employee ID from command line argument
employee_id = sys.argv[1]

# URLs for user and task data
url_user = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
url_tasks = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

# Make GET requests for user and task data
user_data = requests.get(url_user).json()
task_data = requests.get(url_tasks).json()

# Get employee name from user data
employee_name = user_data['name']

# Create CSV file with employee ID as filename
filename = "{}.csv".format(employee_id)

# Open CSV file in write mode and create DictWriter object
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header row to CSV file
    writer.writeheader()

    # Loop through task data and write each task to CSV file
    for task in task_data:
        completed = task['completed']
        title = task['title']

        writer.writerow({
            'USER_ID': employee_id,
            'USERNAME': employee_name,
            'TASK_COMPLETED_STATUS': str(completed),
            'TASK_TITLE': title
        })

# Print success message with filename
print("Data exported to {}".format(filename))
