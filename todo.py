import os.path

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
    while True:
        tasks = load_todo()
        task = input('Enter the task: ')
        tasks.append(task + '\n')
        write_todo(tasks)
        print(f'The task "{task}" has been added to the list.')
        if input('Do you want to ADD more items to the list? (y/N): ').strip().lower() != 'y':
            break

def show_list():
    tasks = load_todo()
    if tasks:
        index = 1
        for task in tasks:
            print(f'{index}. {task.strip()}')
            index += 1
    else:
        print('Todo list is empty.')

def is_valid_index(i, tasks):
    return 0 <= i < len(tasks)

def delete_from_list():
    while True:
        tasks = load_todo()
        if tasks:
            i = 1
            for task in tasks:
                print(f'{i}. {task.strip()}')
                i = i + 1
            str_of_task_to_delete = input('Enter the index of the task you want to delete : ')
            int_of_task_to_delete = int(str_of_task_to_delete) - 1
            if is_valid_index(int_of_task_to_delete, tasks):
                deleted_task = tasks.pop(int_of_task_to_delete)
                write_todo(tasks)
                print(f'The task {deleted_task.strip()} has been deleted from the list')
            else:
                print('Invalid number, please try again')
        else:
            print('To-do list is empty')
        if input('Do you want to DELETE more items from the list? (y/N): ') != 'y':
            break

def main():

    while True:
        try:
            print('\tThis is a To-Do application\n')
            print('\tTo enter a task into the list, enter 1\n')
            print('\tTo show the list, enter 2\n')
            print('\tTo delete a task from the list, enter 3\n')

            user_option = int(input('Select your operation: '))
        except ValueError:
            print('Invalid input, please enter a number.')
            continue

        match user_option:
            case 1:
                add_task_to_list()
            case 2:
                show_list()
            case 3:
                delete_from_list()
            case _:
                print('Please enter a valid operation.')

        if input('Do you want to continue? (y/N): ') != 'y':
            break

if __name__ == "__main__":
    main()
