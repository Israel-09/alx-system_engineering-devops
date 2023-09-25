#!/usr/bin/python3
'''gets employee information on tasks and give output on completed tasks'''


import requests
from sys import argv

u_id = int(argv[1])

todo = requests.get('https://jsonplaceholder.typicode.com/todos')
json_result = todo.json()

total = 0
completed = 0
task_comp = []

for task in json_result:
    if task.get('userId') == u_id:
        total += 1
        if task.get('completed') is True:
            completed += 1
            task_comp.append(task.get('title'))

user = requests.get('https://jsonplaceholder.typicode.com/users')
username = user.json()[u_id - 1].get('name')

print("Employee {} is done with tasks({}/{}):"
      .format(username, completed, total))
for title in task_comp:
    print("\t {}".format(title))
