# Quickstart Guide: CLI Todo Application

**Feature**: 001-cli-todo-app
**Date**: 2026-02-08

## Getting Started

### Prerequisites
- Python 3.13 or higher
- UV package manager

### Installation
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies: `uv sync`
4. Run the application: `python -m src.todo_app`

### Basic Usage

#### Add a new todo item
```bash
python -m src.todo_app add --title "Buy groceries" --description "Milk, bread, eggs"
```

#### List all todo items
```bash
python -m src.todo_app list
```

#### Update an existing todo item
```bash
python -m src.todo_app update --id 1 --title "Buy groceries and vegetables" --description "Milk, bread, eggs, carrots"
```

#### Delete a todo item
```bash
python -m src.todo_app delete --id 1
```

#### Mark a todo item as complete
```bash
python -m src.todo_app complete --id 1
```

#### Mark a todo item as incomplete
```bash
python -m src.todo_app incomplete --id 1
```

### Example Workflow
1. Add a few todo items
2. List them to verify they were added
3. Mark one as complete
4. Update another item
5. List again to see changes
6. Delete an item when completed

### Expected Output
- Successful operations will display confirmation messages
- Failed operations will display error messages
- All data is stored in-memory only and will be lost when the application exits