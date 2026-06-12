# storage.py
import json
import os
from models import User, Project  # Importing our blueprints from models.py

DATABASE_FILE = "teamflow_db.json"

class TeamFlowStorage:
    def __init__(self):
        self.users = {}      
        self.projects = {}   
        self.load_from_json()

    def save_to_json(self):
        """Saves current memory data straight into the text file."""
        data_to_save = {
            "users": {name: u.__dict__ for name, u in self.users.items()},
            "projects": {pid: p.__dict__ for pid, p in self.projects.items()}
        }
        with open(DATABASE_FILE, "w") as file:
            json.dump(data_to_save, file, indent=4)

    def load_from_json(self):
        """Loads data from the file back into operational Python objects."""
        if not os.path.exists(DATABASE_FILE):
            return
        with open(DATABASE_FILE, "r") as file:
            raw_data = json.load(file)
            for name, u_data in raw_data.get("users", {}).items():
                self.users[name] = User(u_data["username"], u_data["role"])
            for pid, p_data in raw_data.get("projects", {}).items():
                project = Project(pid, p_data["name"], p_data["assigned_user"])
                project.tasks = p_data.get("tasks", [])
                self.projects[pid] = project
