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
    user_url = endpoint + '/users/' + str(u_id)
    employee_response = requests.get(user_url)
    employee_json = employee_response.json()
    username = employee_json.get('username')
    return (username)


def get_todo(endpoint: str, u_id: int, username: str) -> str:
    '''
    return a list of of a user's tasks
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
            todo_dict['username'] = username
            todo_dict['task'] = todo.get('title')
            todo_dict['completed'] = todo.get("completed")
            todo_matrix.append(todo_dict)

    return (todo_matrix)


def get_usercount(endpoint: str) -> int:
    '''
    returns the number of employees
    '''
    user_url = endpoint + '/users/'
    user_response = requests.get(user_url)
    users = user_response.json()

    max_id = 0

    for user in users:
        if user.get('id') > max_id:
            max_id = user.get('id')

    return (max_id)


if __name__ == '__main__':
    import csv
    from json import dump

    base_url = "https://jsonplaceholder.typicode.com"
    filename = 'todo_all_employees.json'

    users_num = get_usercount(base_url)

    tasks = {}
    for u_id in range(1, users_num + 1):
        username = get_username(base_url, u_id)
        todo_info = get_todo(base_url, u_id, username)
        tasks[u_id] = todo_info

    with open(filename, 'w') as employee_file:
        dump(tasks, employee_file)
#        employee_writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL)
#        emp0loyee_writer.writerows(todo_info)
