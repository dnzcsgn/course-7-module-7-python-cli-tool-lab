class Task:
    def __init__(self, title):
        # Assign the title and default completion status
        self.title = title
        self.completed = False

    def complete(self):
        # Mark as complete and print confirmation
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")


class User:
    def __init__(self, name):
        # Store user's name and initialize empty task list
        self.name = name
        self.tasks = []

    def add_task(self, task):
        # Add a task and print confirmation
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        # Find a task by title, return task or None
        for task in self.tasks:
            if task.title == title:
                return task
        return None