# main.py
from tabulate import tabulate
from storage import TeamFlowStorage  # Importing our file engine from storage.py

# Initialize our data engine from the storage module
db = TeamFlowStorage()

# INTERACTIVE CLI MENU LOOPS
def main_menu():
    while True:
       
        print("    TEAMFLOW CLI APP COMMANDS ")
        print("1. User Management Menu")
        print("2. Project Management Menu")
        print("3. Task Management Menu")
        print("4. Exit Application")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            user_menu()
        elif choice == "2":
            project_menu()
        elif choice == "3":
            task_menu()
        elif choice == "4":
            print("\n Progress saved to local file. Thank you!")
            break
        else:
            print(" Invalid entry! Please type a number between 1 and 4.")

# --- USER MANAGEMENT ---
def user_menu():
    print("\n--- USER MANAGEMENT ---")
    print("1. Register New Team Member")
    print("2. List All Active Team Members")
    choice = input("Select operation (1-2): ").strip()

    if choice == "1":
        username = input("Enter unique username: ").strip().lower()
        if not username:
            print("Error: Username cannot be blank.")
            return
        if username in db.users:
            print("Error: That user already exists.")
            return
        role = input("Enter team role (e.g. Chef, Developer): ").strip()
        
        from models import User  # import to create the user object safely
        db.users[username] = User(username, role if role else "Developer")
        db.save_to_json()
        print(f"Success: '{username}' added to the team!")

    elif choice == "2":
        if not db.users:
            print(" No team members registered yet.")
            return
        table_rows = [[u.username, u.role] for u in db.users.values()]
        print("\n" + tabulate(table_rows, headers=["Username", "Corporate Role"], tablefmt="grid"))

# --- PROJECT MANAGEMENT ---
def project_menu():
    print("\n--- PROJECT MANAGEMENT  ---")
    print("1. Create New Project Assignment")
    print("2. List All Running Projects")
    choice = input("Select operation (1-2): ").strip()

    if choice == "1":
        user = input("Assign to which username?: ").strip().lower()
        if user not in db.users:
            print(" Error: User profile not found in system.")
            return
        pid = input("Enter unique Project ID (e.g. p1): ").strip().lower()
        if pid in db.projects:
            print("Error: Project ID already taken.")
            return
        name = input("Enter functional Project Name: ").strip()
        
        from models import Project
        db.projects[pid] = Project(pid, name, user)
        db.save_to_json()
        print(f" Success: Project '{name}' assigned to user '{user}'!")

    elif choice == "2":
        if not db.projects:
            print(" No projects active right now.")
            return
        table_rows = [[p.id, p.name, p.assigned_user, len(p.tasks)] for p in db.projects.values()]
        print("\n" + tabulate(table_rows, headers=["Project ID", "Name", "Assigned Owner", "Total Tasks"], tablefmt="grid"))

# --- TASK MANAGEMENT ---
def task_menu():
    print("\n--- TASK MANAGEMENT ---")
    print("1. Add New Task to a Project")
    print("2. Mark an Existing Task as Complete")
    print("3. View Detailed Project Status (With Tasks)")
    choice = input("Select operation (1-3): ").strip()

    if choice == "1":
        pid = input("Enter Target Project ID: ").strip().lower()
        if pid not in db.projects:
            print("Error: Project ID not found.")
            return
        title = input("Enter clear Task Title: ").strip()
        if not title:
            print("Error: Title can't be empty.")
            return
            
        task_data = {"title": title, "status": "Pending"}
        db.projects[pid].tasks.append(task_data)
        db.save_to_json()
        print(f"Success: Task added into project layout workflow!")

    elif choice == "2":
        pid = input("Enter Project ID containing the task: ").strip().lower()
        if pid not in db.projects:
            print("Error: Project ID not found.")
            return
        project = db.projects[pid]
        if not project.tasks:
            print("This project has zero tasks recorded.")
            return
            
        print("\n--- Current Tasks ---")
        for idx, task in enumerate(project.tasks):
            print(f"[{idx}] {task['title']} - {task['status']}")
            
        try:
            task_idx = int(input("\nSelect Task Index Number to complete: ").strip())
            project.tasks[task_idx]["status"] = "Completed"
            db.save_to_json()
            print("Success: Task status switched cleanly to Completed!")
        except (ValueError, IndexError):
            print("Error: That selection index does not exist.")

    elif choice == "3":
        pid = input("Enter Project ID to expand: ").strip().lower()
        if pid not in db.projects:
            print("Error: Project ID not found.")
            return
        project = db.projects[pid]
        print(f"\nProject Summary: {project.name} (Owner: {project.assigned_user})")
        if not project.tasks:
            print("No individual tasks assigned to this project space.")
            return
            
        table_rows = [[t["title"], t["status"]] for t in project.tasks]
        print("\n" + tabulate(table_rows, headers=["Work Task Title", "Progress Status"], tablefmt="grid"))

if __name__ == "__main__":
    main_menu()
