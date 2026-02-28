# The Evolution of Todo

A simple, in-memory command-line Todo application demonstrating spec-driven, agentic AI development using Spec-Kit Plus and Qwen.

## Project Overview

This is Phase I of the Todo application project - an in-memory CLI application that focuses on core todo functionality. The application now supports **both interactive menu mode and command-line mode**, built using Python 3.13+.

## Features

- **Interactive Menu Mode** - Run continuously with a user-friendly menu interface
- **Command-Line Mode** - Use individual commands for scripting
- **FastAPI REST API** - Optional web server mode
- Add todo items with title and description
- List all todo items with unique IDs and status indicators
- Update existing todo items
- Delete todo items by ID
- Mark todo items as complete or incomplete
- **JSON File Persistence** - Your todos are saved between sessions

## Project Structure

```
/src                    # Python source code
├── todo_app.py        # Main application entry point
├── models/            # Data models
│   ├── __init__.py
│   └── todo_item.py   # Todo item data model
├── services/          # Business logic
│   ├── __init__.py
│   └── todo_service.py # Todo service implementation
└── cli/               # Command-line interface
    ├── __init__.py
    └── cli_interface.py # CLI handler
/tests                  # Test files
├── unit/              # Unit tests
└── integration/       # Integration tests
/specs/001-cli-todo-app # Feature specifications
  └── spec.md          # Feature specification document
  └── checklists/      # Quality checklists
/history/prompts/       # Prompt history records
  └── 001-cli-todo-app # Feature-specific prompts
```

## Development Workflow

This project follows a strict spec-driven development workflow:
1. Specification (`/sp.specify`)
2. Planning (`/sp.plan`)
3. Task breakdown (`/sp.tasks`)
4. Implementation (`/sp.implement`)

## Technology Stack

- Language: Python 3.13+
- Environment: UV-based Python project
- Interface: Command-line (console) + Interactive Menu + REST API
- Storage: JSON file persistence (todos.json)

## Getting Started

### 1. Interactive Menu Mode (Recommended)

Run the application with an interactive menu that stays open until you choose to quit:

```bash
# Default mode - runs interactive menu
python src\todo_app.py

# Or explicitly specify menu mode
python src\todo_app.py --menu
```

**Menu Options:**
```
========================================
       TODO APPLICATION MENU
========================================
1. Add Task
2. Update Task
3. Delete Task
4. View Tasks
5. Mark Task Complete
6. Mark Task Incomplete
7. Quit
========================================
```

The program will repeatedly show the menu after each action, allowing you to perform multiple operations without restarting.

### 2. Command-Line Mode

Use individual commands for scripting:

```bash
# Add a new todo item
python src\todo_app.py add --title "Buy groceries" --description "Milk, bread, eggs"

# List all todo items
python src\todo_app.py list

# Update an existing todo item
python src\todo_app.py update --id 1 --title "Buy groceries and vegetables"

# Delete a todo item
python src\todo_app.py delete --id 1

# Mark a todo item as complete
python src\todo_app.py complete --id 1

# Mark a todo item as incomplete
python src\todo_app.py incomplete --id 1
```

### 3. FastAPI Server Mode

Run as a REST API server:

```bash
python src\todo_app.py --serve
```

Then access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## Input Validation

The interactive menu mode includes robust input validation:
- Invalid menu choices are rejected with helpful error messages
- Required fields prompt for re-entry if left empty
- Task IDs are validated to ensure they are valid numbers
- Keyboard interrupts (Ctrl+C) are handled gracefully

## Testing

Run verification scripts:
```bash
python verify_setup.py
python verify_functionality.py
```

Run pytest:
```bash
python -m pytest test_functionality.py -v
```

## Constitution

This project adheres to the principles outlined in the [constitution](.specify/memory/constitution.md):
- Spec-driven development
- CLI-first interface
- Test-first methodology
- Minimalist implementation
- Clean code standards
- Python-native implementation

## Example Session (Interactive Mode)

```
========================================
  Welcome to Todo Application!
========================================

========================================
       TODO APPLICATION MENU
========================================
1. Add Task
2. Update Task
3. Delete Task
4. View Tasks
5. Mark Task Complete
6. Mark Task Incomplete
7. Quit
========================================
Enter your choice (1-7): 1

--- Add New Task ---
Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, bread, eggs

[OK] Task added successfully with ID: 1

========================================
       TODO APPLICATION MENU
========================================
1. Add Task
2. Update Task
3. Delete Task
4. View Tasks
5. Mark Task Complete
6. Mark Task Incomplete
7. Quit
========================================
Enter your choice (1-7): 4

--- View Tasks ---

ID   Status   Title                          Description
----------------------------------------------------------------------
1    [ ]      Buy groceries                  Milk, bread, eggs

Total: 1 task(s)

========================================
       TODO APPLICATION MENU
========================================
Enter your choice (1-7): 7

========================================
  Thank you for using Todo Application!
  Goodbye!
========================================
```
