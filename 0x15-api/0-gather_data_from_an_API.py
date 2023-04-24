#!/usr/bin/python3
""" Use REST API to get employee details """
import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    # get employee from API (employee name)
    employee = requests.get(url=url)
    employee_name = employee.json()["name"]

    # get todos
    todos_response = requests.get(url="{}/todos".format(url))
    todos = todos_response.json()

    completed = []
    for todo in todos:
        if todo["completed"]:
            completed.append(todo["title"])

    print("Employee {} is done with tasks({}/{})".
          format(employee_name, len(completed), len(todos)))
    for todo in completed:
        print("\t {}".format(todo))
