import json
import sys
from Task_Manager import TaskManager
def show_help():
    print("-------------------------------------------------------------------------------------------------------")
    print("                             Task Management (Task Tracker CLI)")
    print("-------------------------------------------------------------------------------------------------------")
    print("  add     < To Add a new Task                           : Description Task")
    print("  list    <[done|todo|in-progress]                      : To View tasks ( in a specific status)")
    print("  listAll <[done|todo|in-progress]                      : To View All tasks ")
    print("  update  <ID> To update the task description           : New description")
    print("  status  <ID> < To change the status of the task       : status (done, todo, in-progress)")
    print("  delete  <ID>                                          : To Delete the task")
    print("--------------------------------------------------------------------------------------------------------")

def main():
    manager=TaskManager()
    if len(sys.argv)<2:
        show_help()
        return
    command=sys.argv[1]
    if command=='add':
        if len(sys.argv)<3:
            print("Invalid, The add command requires a task description")
            return
        description=' '.join(sys.argv[2:])
        manager.add_task(description)

    elif command=='list':
        if len(sys.argv)>2:
            status=sys.argv[2]
        else:
            status='todo'
        manager.list_tasks_by_status(status)

    elif command=='listAll':
        manager.list_tasks()

    elif command=='delete':
        if len(sys.argv)>=2:
            id=int(sys.argv[2])
        else:
            print("Invalid Id ")
        manager.delete_task(id)

    elif command=='update':
        if len(sys.argv)>=4:
            id=int(sys.argv[2])
            description=' '.join(sys.argv[3:])
        manager.update_task(id,description)
    
    elif command=='status':
        if len(sys.argv)>=4:
            id=int(sys.argv[2])
            new_status=sys.argv[3]
        manager.update_status(id,new_status)
    elif command=='help':
        show_help()
        return
if __name__=='__main__':
    main()