import json


class TaskManager:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except:
            return {}

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, user_id, task):
        user_id = str(user_id)

        if user_id not in self.tasks:
            self.tasks[user_id] = []

        self.tasks[user_id].append(task)
        self.save_tasks()

    def show_tasks(self, user_id):
        return self.tasks.get(str(user_id), [])

    def delete_task(self, user_id, index):
        user_id = str(user_id)

        if user_id in self.tasks:
            if 0 <= index < len(self.tasks[user_id]):
                self.tasks[user_id].pop(index)
                self.save_tasks()
                return True

        return False

    def clear_tasks(self, user_id):
        user_id = str(user_id)

        if user_id in self.tasks:
            self.tasks[user_id] = []
            self.save_tasks()