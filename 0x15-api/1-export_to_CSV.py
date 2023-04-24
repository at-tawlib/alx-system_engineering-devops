#!/usr/bin/python3
"""
Use REST API to get employee details
Export these details to a CSV file
"""
import requests
import sys
import csv


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

    with open("{}.csv".format(employee_id), 'w') as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'.format(employee_id,
                       username, todo["completed"], todo["title"]))
