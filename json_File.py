import json
import os
FILE_NAME='tasks.json'
def load_tasks():
    if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size==0:
        with open(FILE_NAME,'w')as f :
            json.dump([],f)
            return []
    else:
        with open(FILE_NAME,'r')as f:
            return json.load(f)

def save_tasks(tasks_list):
    with open(FILE_NAME,'w') as f:
        json.dump(tasks_list,f,indent=4)

tasks=load_tasks()