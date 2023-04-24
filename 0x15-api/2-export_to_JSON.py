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
    employee_name = employee.json()["name"]
    username = employee.json()["username"]

    # get todos
    todos_response = requests.get(url="{}/todos".format(url))
    todos = todos_response.json()
    task_dict = {}
    tasks_list = []
    for todo in todos:
        task_dict["task"] = todo["title"]
        task_dict["completed"] = todo["completed"]
        task_dict["username"] = username
        tasks_list.append(task_dict)

    dictionary = {employee_id: tasks_list}
    # serializing json
    json_obj = json.dumps(dictionary)
    # writing to file
    with open("{}.json".format(employee_id), "w") as file:
        file.write(json_obj)
