from task import Task
from save_load_management import save_tasks, load_tasks

tasks = load_tasks()

while True:
    print('\nTask List Menu:')
    print('1. Add Task')
    print('2. List Task')
    print('3. Mark as Completed')
    print('4. Delete Task')
    print('5. Exit')

    choice = int(input('Please choose option (1,2,3,4,5): '))

    match choice:
        case 1:
            title = input('Enter task title: ')
            description = input('Enter task description: ')
            task = Task(title, description)
            tasks.append(task)
            save_tasks(tasks)
            print('Task added successfully.')
        case 2:
            if not tasks:
                print('No tasks available.')
            else:
                for idx, task in enumerate(tasks, start=1):
                    print(f"Task {idx}:")
                    print(task)
        case 3:
            if not tasks:
                print('No tasks available.')
            else:
                print('Tasks:')
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.title} ({'Completed' if task.completed else 'Not Completed'})")

                try:
                    task_index = int(input("Enter the task number you want to change status to Completed: "))
                    
                    if task_index == 1:
                        task_index = 0

                    if 0 <= task_index < len(tasks):
                        tasks[task_index].mark_as_completed()
                        print(f"Task '{tasks[task_index].title}' was marked completed!")
                        save_tasks(tasks)
                    else:
                        print('Invalid task number. Please choose a valid task number.')
                except ValueError:
                    print('Invalid input. Please enter a valid task number.')
        case 4:
            if not tasks:
                print('No tasks available.')
            else:
                print('Tasks:')
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.title} ({'Completed' if task.completed else 'Not Completed'})")

                try:
                    task_index = int(input("Enter the task number you want to delete: "))

                    if task_index == 1:
                        task_index = 0

                    if 0 <= task_index < len(tasks):
                        deleted_task_title = tasks.pop(task_index).title
                        print(f"Task '{deleted_task_title}' was deleted!")
                        save_tasks(tasks)
                    else:
                        print('Invalid task number. Please choose a valid task number.')
                except ValueError:
                    print('Invalid input. Please enter a valid task number.')
        case 5:
            save_tasks(tasks)
            print('Exiting Task List. Thank you for using.')
            exit()
        case _:
            print('Please select an valid choice from menu.')