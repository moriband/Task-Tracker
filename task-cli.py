import sys
import json
import os
from datetime import datetime
from email.policy import default

TASK_JSON_PATH = 'C:\\prgr\\Task Tracker\\tasks.json'

# Создание JSON, если его нет

if not os.path.exists(TASK_JSON_PATH):
    with open(TASK_JSON_PATH, 'w') as f:
        json.dump([], f, indent=4)

# Загрузка задач
with open(TASK_JSON_PATH, 'r') as f:
    try:
        tasks = json.load(f)
    except json.decoder.JSONDecodeError:
        tasks = []


def not_tasks():
    if not tasks:
        print('No tasks found.')
        sys.exit(0)

def save_tasks():
    with open(TASK_JSON_PATH, 'w') as f:
        json.dump(tasks, f, indent=4)

def print_task(task):
    print(f'ID: {task["id"]}')
    print(f'Description: {task["description"]}')
    print(f'Status: {task["status"]}')
    print(f'Created At: {task["createdAt"]}')
    print(f'Updated At: {task["updatedAt"]}\n')

#------------------------------COMMANDS-------------------------------

# LIST commands-------------------------------
if len(sys.argv) > 1 and sys.argv[1] == 'list':
    status = sys.argv[2] if len(sys.argv) > 2 else None
    not_tasks()
    filtered = [t for t in tasks if t['status'] == status] if status else tasks
    if not filtered:
        print('No tasks found for this status')
    for t in filtered:
        print_task(t)
    sys.exit(0)

# if len(sys.argv) > 2 and sys.argv[1] == 'list' and sys.argv[2] == 'todo':
#     not_tasks()
#     filtered_tasks = [task for task in tasks if task['status'] == sys.argv[2]]
#     if not filtered_tasks:
#         print('This type tasks not found.')
#     for task in filtered_tasks:
#         if task['status'] == 'todo':
#             print(f'ID: {task["id"]}')
#             print(f"Description: {task['description']}")
#             print(f"Status: {task['status']}")
#             print(f"Created At: {task['createdAt']}")
#             print(f"Updated At: {task['updatedAt']}")
#
# if len(sys.argv) > 2 and sys.argv[1] == 'list' and sys.argv[2] == 'done':
#     not_tasks()
#     filtered_tasks = [task for task in tasks if task['status'] == sys.argv[2]]
#     if not filtered_tasks:
#         print('This type tasks not found.')
#     for task in filtered_tasks:
#         if task['status'] == 'done':
#             print(f'ID: {task["id"]}')
#             print(f"Description: {task['description']}")
#             print(f"Status: {task['status']}")
#             print(f"Created At: {task['createdAt']}")
#             print(f"Updated At: {task['updatedAt']}")
#
# if len(sys.argv) > 2 and sys.argv[1] == 'list' and sys.argv[2] == 'in-progress':
#     not_tasks()
#     filtered_tasks = [task for task in tasks if task['status'] == sys.argv[2]]
#     if not filtered_tasks:
#         print('This type tasks not found.')
#     for task in filtered_tasks:
#         if task['status'] == 'in-progress':
#             print(f'ID: {task["id"]}')
#             print(f"Description: {task['description']}")
#             print(f"Status: {task['status']}")
#             print(f"Created At: {task['createdAt']}")
#             print(f"Updated At: {task['updatedAt']}")

# DELETE commands-----------------------------------
if len(sys.argv) > 1 and sys.argv[1] == 'delete_all':
    tasks.clear()
    save_tasks()
    print('All tasks deleted.')
    sys.exit(0)

if len(sys.argv) > 1 and sys.argv[1] == 'delete':
    not_tasks()
    try:
        task_id = int(sys.argv[2])
    except ValueError:
        print('Task ID must be an number.')
        sys.exit(1)
    task_to_delete = next((t for t in tasks if t['id'] == task_id), None)
    if task_to_delete:
        tasks.remove(task_to_delete)
        save_tasks()
        print(f'Task {task_id} deleted.')
    else:
        print(f'Task {task_id} not found.')
    sys.exit(0)

# UPDATE commands---------------------------------

if len(sys.argv) > 1 and sys.argv[1] == 'update':
    not_tasks()
    try:
        task_id = int(sys.argv[2])
    except ValueError:
        print('Task ID must be a number.')
        sys.exit(1)
    description = " ".join(sys.argv[3:-1])
    status = sys.argv[-1]
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks()
            print(f'Task ID {task_id} updated.')
            sys.exit(0)
    print(f'Task {task_id} does not exist.')
    sys.exit(1)

if len(sys.argv) > 1 and sys.argv[1] == 'mark-in-progress':
    not_tasks()
    try:
        task_id = int(sys.argv[2])
    except ValueError:
        print('Task ID must be a number.')
        sys.exit(1)
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in progress'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks()
            print(f'Task {task_id} marked as in progress.')
            sys.exit(0)
    print(f'Task {task_id} does not exist.')
    sys.exit(1)

if len(sys.argv) > 1 and sys.argv[1] == 'mark-done':
    not_tasks()
    try:
        task_id = int(sys.argv[2])
    except ValueError:
        print('Task ID must be a number.')
        sys.exit(1)
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks()
            print(f'Task {task_id} marked as done.')
            sys.exit(0)
    print(f'Task {task_id} does not exist.')
    sys.exit(1)

# ADD command---------------------------------------

if len(sys.argv) > 2 and sys.argv[1] == 'add':
    description = sys.argv[2]
    status = sys.argv[3] if len(sys.argv) > 3 else 'todo'
    new_id = max([task['id'] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()
    new_task = {
        'id': new_id,
        'description': description,
        'status': status,
        'createdAt': now,
        'updatedAt': now,
    }
    tasks.append(new_task)
    save_tasks()
    print(f'Task added (ID: {new_id}): {description}')
    sys.exit(0)

# IF COMMAND NOT EXIST---------------
print("Unknown command. Available commands:\nadd, update, delete, delete_all, list, mark-in-progress, mark-done.")