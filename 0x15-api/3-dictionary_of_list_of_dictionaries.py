#!/usr/bin/python3
"""
Use REST API to get employee details
then expor the data to jsonf ile
"""
import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users"
    # get all employees from API (employee name)
    employees = requests.get(url=url).json()

    dictionary = {}
    for employee in employees:
        employee_id = employee['id']
        username = employee['username']
        # get todos of employee
        todos_response = requests.get(url="{}/{}/todos"
                                      .format(url, employee_id))
        todos = todos_response.json()

        dictionary[employee_id] = []
        tasks_list = []
        for todo in todos:
            tasks_list.append({
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            })
            dictionary[employee_id] = tasks_list
    # writing to file
    with open("todo_all_employees.json".format(employee_id), "w") as file:
        # serializing json
        json.dump(dictionary, file)
