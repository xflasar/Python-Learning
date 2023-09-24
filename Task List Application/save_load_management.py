import json
from task import Task

def save_tasks(tasks):
    with open('tasks.json', 'w') as json_file:
        json.dump([task.__dict__ for task in tasks], json_file)
    print("Tasks were saved to 'tasks.json'.")

def load_tasks():
    try:
        with open('tasks.json', 'r') as json_file:
            saved_tasks = json.load(json_file)
        
        #convert the tasks to task objects 
        tasks = [Task(**task_dict) for task_dict in saved_tasks]
        print("Tasks loaded from 'tasks.json'.")
        return tasks
    except FileNotFoundError:
        print('No saved tasks found!')
        return []