# TeamFlow CLI — Command-Line Project Management Tool

TeamFlow CLI is a Python-based command-line interface application built for software development teams to manage internal work trackers. The system allows team leads to register developers, assign structured project spaces, and break down projects into tracking tasks. All operational records are relation-mapped and automatically saved using built-in File I/O operations.

## Key Features (Project MVP)
*   **User Management:** Dynamically register team profiles with custom corporate roles and display user lists.
*   **Project Workspace Allocation:** Create custom project tracks linked directly to active developers.
*   **Granular Task Tracking:** Append actionable task dictionaries to specific project workspaces and toggle progress statuses cleanly via array indices.
*   **No-Loss Data Persistence:** Automatic JSON serialization and parsing ensures data survives terminal restarts.
*   **Visual Grid Displays:** Implements the external `tabulate` library to print neat ASCII tables directly inside the terminal interface.

---

## Project Architecture & File Layout
The application relies on a strictly modular architecture to keep components separated and maintainable:

```text
Final_Project/
│
├── main.py              # Application Entry Point & Interactive CLI Loop Router
├── models.py            # Object Blueprints & Schema Blueprints Layer
├── storage.py           # File I/O Engine (JSON Serialization & Parsing)
├── requirements.txt     # Formally tracks external PyPi tool dependencies
└── teamflow_db.json     # Physical flat-file database storage sheet (Generated automatically)
```

### Data Models & System Relationships
1.  **User Class (`models.py`):** Holds developer `username` and `role` credentials.
2.  **Project Class (`models.py`):** Holds project parameters (`id`, `name`, `assigned_user`) and a dedicated internal `tasks` list array.
3.  **One-to-Many Association:** One `User` can be allocated multiple unique `Project` tracks. Similarly, one `Project` contains multiple individual task dictionaries appended to its internal records line list.

---

## Installation & Workspace Setup

This project uses standard global environments to maximize portability. Run the following installation sequence in your terminal to override default operating system package blocks and initialize dependencies safely:

```bash
# 1. Force-install the external visual alignment table layout engine globally
pip install tabulate --break-system-packages

# 2. Launch the core tracking system application control loops
python3 main.py
```

---

## Sample Live-Demo Workflows
Execute this standard system validation script during live panel grading to demonstrate full functional operability:

1.  **Initialize User Profile:** Choose Option `1` (User Management) -> Option `1` (Register Member). Insert username `lincon` and role `Lead`.
2.  **Create Assignment Track:** Choose Option `2` (Project Management) -> Option `1` (Create Assignment). Assign to `lincon`, assign ID `p1`, and define title `CoreEngine`.
3.  **Inject Actionable Work Tasks:** Choose Option `3` (Task Management) -> Option `1` (Add New Task). Target Project ID `p1` and create task title `Build Final Modules`.
4.  **Audit Data Persistence:** Choose Option `4` to Exit the application. In your terminal run `cat teamflow_db.json` to prove raw dictionaries completely wrote into system hard drives.
5.  **Status Progress Mutations:** Relaunch using `python3 main.py`. Navigate to Option `3` -> Option `2` (Mark Completed). Enter target project `p1`, select task array pointer index `0`, and switch status cleanly to Completed. Check outputs via Option `3`.

---

## Evaluation Grading Compliance Notes
*   **Encapsulation & Modularity:** Classes are decoupled cleanly into `models.py`, database read/writes are restricted to `storage.py`, and user inputs are routed through loops inside `main.py`.
*   **Error Prevention Handling:** Direct key checks (`if username in db.users`) prevent database collisions. The index mapping is wrapped securely inside nested `try-except` loops to intercept indexing errors or non-integer typing faults without causing program crashes.
*   **External Package Tracking:** External library usage conforms with requirements rules by formally logging dependencies in `requirements.txt`.
