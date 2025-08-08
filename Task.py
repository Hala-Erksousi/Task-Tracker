import datetime
import json_File as j
class Task:
    def __init__(self,task_id,description):
        self.id=task_id
        self.description=description
        self.status="todo"
        self.created_at=datetime.datetime.now().isoformat()
        self.updated_at=datetime.datetime.now().isoformat()

    def to_dict(self):
        return {
            "id" :self.id,
            "description": self.description,
            "status":self.status,
            "createdAt":self.created_at,
            "updatedAt":self.updated_at
        }



   


