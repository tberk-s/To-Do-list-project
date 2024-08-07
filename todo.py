import os.path
import sys

todo_list = "to_do_list.txt"

def write_todo(todo):
    with open(todo_list, 'w') as file:
        file.writelines(todo)

def load_todo():
    if os.path.exists(todo_list):
        with open(todo_list, 'r') as file:
            return file.read()

def add_task_to_list(task):
    append = load_todo()
    append.append(task + '\n')
    write_todo(append)
    print(f'The task "{task}" has been added to the list.')

def show_list():
    if load_todo():
        index = 0
        for task in load_todo():
            print(f'{index}. task = {task.strip()}')
            index = index+1
