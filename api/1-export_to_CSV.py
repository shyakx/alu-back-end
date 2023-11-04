#!/usr/bin/python3
"""
Module to retrieve and display 
employee TODO list progress and export in CSV format.
"""

import requests
import csv
from sys import argv


def get_employee_todo_progress(employee_id):
    """
    Function to get and display employee TODO list progress and 
    export in CSV format.
    """
    # API endpoint for employee information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # API endpoint for employee's TODO list
    todo_url = 
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetching user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_id = user_data.get("id")
    username = user_data.get("username")

    # Fetching TODO list
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Writing data to CSV file
    csv_file_path = f"{user_id}.csv"
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
            "TASK_TITLE"])

        for task in todo_data:
            task_completed_status =
            "COMPLETED" if task.get("completed") else "NOT COMPLETED"
            task_title = task.get("title")
            csv_writer.writerow
            ([user_id, username, task_completed_status, task_title])

    print(f"Employee {username}
            is done with tasks ({user_id}/{len(todo_data)}):")
    for task in todo_data:
        print(f"\t{task['title']}")

    print(f"Data exported to {csv_file_path}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
