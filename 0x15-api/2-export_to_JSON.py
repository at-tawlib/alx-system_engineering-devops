#!/usr/bin/python3
"""
Use REST API to get employee details
then expor the data to jsonf ile
"""
import json
import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    # get employee from API (employee name)
    employee = requests.get(url=url)
    username = employee.json()["username"]

    # get todos
    todos_response = requests.get(url="{}/todos".format(url))
    todos = todos_response.json()
    tasks_list = []
    for todo in todos:
        tasks_list.append({
            "task": todo["title"],
            "completed": todo["completed"],
            "username": username
            })

    dictionary = {employee_id: tasks_list}
    # writing to file
    with open("{}.json".format(employee_id), "w") as file:
        # serializing json
        json.dump(dictionary, file)
