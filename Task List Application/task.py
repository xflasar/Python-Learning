# task.py
class Task:
    def __init__(self, title, description, completed=False):
        self.title=title
        self.description=description
        self.completed=completed
    
    def mark_as_completed(self):
        self.completed = True
    
    def __str__(self):
        status= "Completed" if self.completed else "Not Completed"
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.completed}"