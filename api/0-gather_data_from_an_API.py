#!/usr/bin/python3

#module requests  impoting to be used in my codes
import requests
#provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import sys

def get_employee_todo_progress(employee_id):


    # Base URL for the JSONPlaceholder API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Endpoint for user details
    user_endpoint = f'{base_url}/users/{employee_id}'

    # Endpoint for user's TODO list
    todo_endpoint = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch user details
        user_response = requests.get(user_endpoint)
        user_data = user_response.json()

        # Fetch user's TODO list
        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()

        # Calculate TODO progress
        total_tasks = len(todo_data)
        completed_tasks = sum(task['completed'] for task in todo_data)

        # Display progress information
        print(f"Employee {user_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

        # Display titles of completed tasks
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Get employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to get and display employee TODO list progress
    get_employee_todo_progress(employee_id)
