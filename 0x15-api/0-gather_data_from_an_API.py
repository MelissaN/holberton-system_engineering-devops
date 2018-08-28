#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
"""
import requests
from sys import argv


def display():
    """return API data"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in users.json():
        if u.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (u.get('name'))
            break
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if t.get('completed') is True:
                    NUMBER_OF_DONE_TASKS += 1
                    TASK_TITLE.append(t.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    display()
