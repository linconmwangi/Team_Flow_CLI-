# models.py

class User:
    def __init__(self, username, role="Developer"):
        self.username = username
        self.role = role

class Project:
    def __init__(self, project_id, name, assigned_user):
        self.id = project_id
        self.name = name
        self.assigned_user = assigned_user  # Linked to a User username
        self.tasks = []                    # One-to-Many: List of task dictionaries
