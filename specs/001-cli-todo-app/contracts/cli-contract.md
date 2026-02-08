# API Contract: CLI Todo Application

**Feature**: 001-cli-todo-app
**Date**: 2026-02-08

## Command Interface

### Add Todo Item
- **Command**: `add`
- **Arguments**:
  - `--title` (required): Title of the todo item
  - `--description` (optional): Description of the todo item
- **Returns**: Success message with assigned ID
- **Errors**: 
  - Missing title argument
  - Empty title

### List Todo Items
- **Command**: `list`
- **Arguments**: None
- **Returns**: Formatted list of all todo items with ID, title, description, and completion status
- **Errors**: None

### Update Todo Item
- **Command**: `update`
- **Arguments**:
  - `--id` (required): ID of the todo item to update
  - `--title` (optional): New title for the todo item
  - `--description` (optional): New description for the todo item
- **Returns**: Success message
- **Errors**:
  - Invalid ID format
  - Non-existent ID

### Delete Todo Item
- **Command**: `delete`
- **Arguments**:
  - `--id` (required): ID of the todo item to delete
- **Returns**: Success message
- **Errors**:
  - Invalid ID format
  - Non-existent ID

### Mark Complete
- **Command**: `complete`
- **Arguments**:
  - `--id` (required): ID of the todo item to mark complete
- **Returns**: Success message
- **Errors**:
  - Invalid ID format
  - Non-existent ID

### Mark Incomplete
- **Command**: `incomplete`
- **Arguments**:
  - `--id` (required): ID of the todo item to mark incomplete
- **Returns**: Success message
- **Errors**:
  - Invalid ID format
  - Non-existent ID

## Data Format

### Todo Item Representation
```
{
  "id": int,
  "title": str,
  "description": str,
  "completed": bool
}
```

### Success Response
```
{
  "status": "success",
  "message": str,
  "data": object (optional)
}
```

### Error Response
```
{
  "status": "error",
  "message": str
}
```