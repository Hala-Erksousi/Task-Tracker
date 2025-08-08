import datetime
import json_File as j
from Task import Task
class TaskManager:
    def add_task(self,description):
        tasks_list=j.load_tasks()
        if tasks_list:
            id=tasks_list[-1]['id']+1
        else:
            id=1
        
        new_Task=Task(task_id=id,description=description)
        tasks_list.append(new_Task.to_dict())
        j.save_tasks(tasks_list)
        print(f"Task Added successfully (ID : {id})")

    def update_task(self,id,description):
        list_tasks=j.load_tasks()
        for task in list_tasks:
            if task['id']==id:
                task['description']=description
                task['updatedAt']=datetime.datetime.now().isoformat()
                break
    
        j.save_tasks(list_tasks)

    def delete_task(self,id):
        list_tasks=j.load_tasks()
        for task in list_tasks:
            if task['id']==id:
                list_tasks.remove(task)
                break
        
        j.save_tasks(list_tasks)

    def update_status(self,id,new_status):
        list_tasks=j.load_tasks()
        for task in list_tasks:
            if task['id']==id:
                task['status']=new_status
                task['updatedAt']=datetime.datetime.now().isoformat()
                break

        j.save_tasks(list_tasks)

    def list_tasks(self):
        list_tasks=j.load_tasks()
        for task in list_tasks:
            print(f"ID          : {task['id']}")
            print(f"description : {task['description']}")
            print(f"status      : {task['status']}")
            print(f"createdAt   : {task['createdAt']}")
            print(f"updatedAt   : {task['updatedAt']}")
            print("-" * 20)

    def list_tasks_by_status(self,status):
        tasks_list = j.load_tasks()
        found_tasks=False
        print(f"---To Do list status : {status} ---")
        for task in tasks_list:
            if task['status'] == status:
                print(f"ID          : {task['id']}")
                print(f"description : {task['description']}")
                print(f"status      : {task['status']}")
                print(f"createdAt   : {task['createdAt']}")
                print(f"updatedAt   : {task['updatedAt']}")
                print("-" * 20)
                found_tasks = True

        if not found_tasks:
            print(f"No tasks in status  '{status}'.")

    
