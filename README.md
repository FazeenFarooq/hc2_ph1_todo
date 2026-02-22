# The Evolution of Todo

A simple, in-memory command-line Todo application demonstrating spec-driven, agentic AI development using Spec-Kit Plus and Qwen.

## Project Overview

This is Phase I of the Todo application project - an in-memory CLI application that focuses on core todo functionality without persistence. The application is built using Python 3.13+ with a command-line interface.

## Features

- Add todo items with title and description
- List all todo items with unique IDs and status indicators
- Update existing todo items
- Delete todo items by ID
- Mark todo items as complete or incomplete

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
- Interface: Command-line (console)
- Storage: In-memory only (no file system, database, or persistence)

## Getting Started

1. Ensure Python 3.13+ is installed
2. Install dependencies using UV: `uv sync`
3. Run the application: `python -m src.todo_app`

### Available Commands

- Add a new todo item: `python -m src.todo_app add --title "Buy groceries" --description "Milk, bread, eggs"`
- List all todo items: `python -m src.todo_app list`
- Update an existing todo item: `python -m src.todo_app update --id 1 --title "Buy groceries and vegetables"`
- Delete a todo item: `python -m src.todo_app delete --id 1`
- Mark a todo item as complete: `python -m src.todo_app complete --id 1`
- Mark a todo item as incomplete: `python -m src.todo_app incomplete --id 1`

## Testing

Run unit tests: `python -m pytest tests/unit/`
Run integration tests: `python -m pytest tests/integration/`
Run all tests: `python -m pytest tests/`

## Constitution

This project adheres to the principles outlined in the [constitution](.specify/memory/constitution.md):
- Spec-driven development
- CLI-first interface
- Test-first methodology
- Minimalist implementation
- Clean code standards
- Python-native implementation


 1 # Add a todo
      2 python src\todo_app.py add --title "Buy groceries" --description "Milk, bread, eggs"
      3 
      4 # List todos (will show your item now!)
      5 python src\todo_app.py list
      6 
      7 # Mark complete
      8 python src\todo_app.py complete --id 1
      9 
     10 # Update
     11 python src\todo_app.py update --id 1 --title "New title"
     12 
     13 # Delete
     14 python src\todo_app.py delete --id 1