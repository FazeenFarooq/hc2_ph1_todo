# Data Model: CLI Todo Application

**Feature**: 001-cli-todo-app
**Date**: 2026-02-08

## Entities

### TodoItem
Represents a single todo item with the following attributes:

- **id** (int): Unique identifier for the todo item, auto-generated
- **title** (str): Title of the todo item, required
- **description** (str): Detailed description of the todo item, optional (can be empty)
- **completed** (bool): Completion status of the todo item, default: False

### TodoList
Represents a collection of TodoItem objects stored in memory:

- **items** (dict): Dictionary mapping integer IDs to TodoItem objects
- **next_id** (int): Counter for generating unique IDs, starts at 1

## Relationships
- TodoList contains zero or more TodoItem objects
- Each TodoItem has exactly one TodoList owner

## State Transitions
- TodoItem.completed can transition from False to True (mark complete)
- TodoItem.completed can transition from True to False (mark incomplete)

## Validation Rules
- TodoItem.title must not be empty or None
- TodoItem.id must be unique within the TodoList
- TodoItem.id must be a positive integer
- Operations on non-existent IDs must raise appropriate exceptions