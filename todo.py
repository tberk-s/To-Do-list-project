
import os.path
import sys

todo_list = "to_do_list.txt"

def write_todo(todo):
    with open(todo_list, 'w') as file:
        file.writelines(todo)

def load_todo():
    if os.path.exists(todo_list):
        with open(todo_list, 'r') as file:
            return file.readlines()
    return []

def add_task_to_list():
    tasks = load_todo()
    task = input('Enter the task')
    tasks.append(task + '\n')
    write_todo(tasks)
    print(f'The task "{task}" has been added to the list.')

def show_list():
    if load_todo():
        index = 1
        for task in load_todo():
            print(f'{index}. task = {task.strip()}')
            index = index+1
    else:
        print('Todo list is empty')

def is_valid_index(i, tasks):
    return 0 <= i <= len(tasks)

def convert_to_int():
    return int(i_str) if i_str.isdigit() else -1

def delete_from_list():
    tasks = load_todo()
    if tasks:
        i = 1
        for task in tasks:
            print(f'{i}. {task.strip()}')
            i = i + 1
        str_of_task_to_delete = input('Enter the index of the task you want to delete')
        int_of_task_to_delete = int(str_of_task_to_delete) - 1
        if is_valid_index(int_of_task_to_delete, tasks):
            deleted_task = tasks.pop(int_of_task_to_delete)
            write_todo(tasks)
            print(f'The task {deleted_task.strip()} has been deleted from the list')
        else:
            print('Invalid number, please try again')
    else:
        print('To-do list is empty')

delete_from_list()
add_task_to_list()
show_list()
