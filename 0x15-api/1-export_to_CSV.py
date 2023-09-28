#!/usr/bin/python3
'''
create a csv file containing an empoloyee todo list
'''
import requests


if __name__ == '__main__':
    import csv
    from sys import argv

    u_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    filename = argv[1] + '.csv'

    user_url = base_url + '/users/' + argv[1]
    employee_response = requests.get(user_url)
    username = employee_response.json().get('username')

    todo_url = user_url + '/todos/'
    todos = requests.get(todo_url).json()

    with open(filename, 'w') as employee_file:
        employee_writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            employee_writer.writerow([u_id, username,
                                     todo.get('completed'), todo.get('title')])
