#!/usr/bin/python3
"""
Module to retrieve and display employee TODO list progress.
"""

import requests
from sys import argv

def get_employee_todo_progress(employee_id):
    """
    Function to get and display employee TODO list progress.
    """
    # API endpoint for employee information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # API endpoint for employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetching user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetching TODO list
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Filtering completed tasks
    completed_tasks = [task for task in todo_data if task.get("completed")]

    # Displaying progress
    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{len(todo_data)}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)

