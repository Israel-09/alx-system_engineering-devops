#!/usr/bin/python3
'''
create a csv file containing an empoloyee todo list
'''
import requests


def get_username(endpoint: str, u_id: str) -> str:
    '''
    Args:
        endpoint (str): the base url of the api
        u_id (str): id  of the Employee
    Return:
        on sucess the username of the employee
    '''
    user_url = endpoint + '/users/' + u_id
    employee_response = requests.get(user_url)
    employee_json = employee_response.json()
    username = employee_json.get('username')
    return (username)


def get_todo(endpoint: str, u_id: int, username: str) -> str:
    '''
    Args:
        endpoint (str): the base url of the api
        u_id (int): id  of the Employee
        username
    Return:
        on sucess returns details of employee's task
    '''
    todo_matrix = []
    todo_url = endpoint + '/todos/'
    todo_response = requests.get(todo_url)
    todo_json = todo_response.json()

    for todo in todo_json:
        if todo.get('userId') == u_id:
            todo_dict = {}
            todo_dict['task'] = todo.get('title')
            todo_dict['completed'] = todo.get("completed")
            todo_dict['username'] = username
            todo_matrix.append(todo_dict)

    return (todo_matrix)


if __name__ == '__main__':
    import csv
    from sys import argv
    from json import dump

    u_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    filename = argv[1] + '.json'

    username = get_username(base_url, argv[1])
    todo_info = get_todo(base_url, u_id, username)

    tasks = {argv[1]: todo_info}

    with open(filename, 'w') as employee_file:
        dump(tasks, employee_file)
#        employee_writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL)
#        employee_writer.writerows(todo_info)
