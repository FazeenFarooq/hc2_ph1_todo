"""
Main application entry point for the CLI Todo application.
"""

import os
import sys
from typing import List, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Add the src directory to the path so we can import from sibling directories
sys.path.insert(0, os.path.dirname(__file__))

from services.todo_service import TodoService, TodoNotFoundException
from cli.cli_interface import CLIInterface
from models.todo_item import TodoItem


# Pydantic models for request/response
class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the todo item")
    description: str = Field(default="", description="Description of the todo item")


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, description="New title for the todo item")
    description: Optional[str] = Field(default=None, description="New description for the todo item")


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    model_config = {"from_attributes": True}


# Initialize FastAPI app
app = FastAPI(
    title="Todo API",
    description="REST API for managing todo items",
    version="0.1.0"
)

# Initialize the todo service (shared between CLI and API)
todo_service = TodoService()


def main():
    """
    Main entry point for the application.
    Initializes the service and CLI interface, then runs the application.
    """
    # Initialize the CLI interface with the service
    cli_interface = CLIInterface(todo_service)

    # Run the CLI interface
    cli_interface.run()


# FastAPI endpoints
@app.get("/todos", response_model=List[TodoResponse], tags=["Todos"])
def list_todos():
    """
    Retrieve all todo items.
    """
    items = todo_service.list_items()
    return items


@app.get("/todos/{todo_id}", response_model=TodoResponse, tags=["Todos"])
def get_todo(todo_id: int):
    """
    Retrieve a specific todo item by ID.
    """
    try:
        item = todo_service.get_item(todo_id)
        return item
    except TodoNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@app.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED, tags=["Todos"])
def create_todo(todo: TodoCreate):
    """
    Create a new todo item.
    """
    item = todo_service.add_item(title=todo.title, description=todo.description)
    return item


@app.put("/todos/{todo_id}", response_model=TodoResponse, tags=["Todos"])
def update_todo(todo_id: int, todo: TodoUpdate):
    """
    Update an existing todo item.
    """
    try:
        item = todo_service.update_item(
            item_id=todo_id,
            title=todo.title,
            description=todo.description
        )
        return item
    except TodoNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Todos"])
def delete_todo(todo_id: int):
    """
    Delete a todo item.
    """
    try:
        todo_service.delete_item(todo_id)
    except TodoNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@app.post("/todos/{todo_id}/complete", response_model=TodoResponse, tags=["Todos"])
def mark_todo_complete(todo_id: int):
    """
    Mark a todo item as complete.
    """
    try:
        item = todo_service.mark_complete(todo_id)
        return item
    except TodoNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@app.post("/todos/{todo_id}/incomplete", response_model=TodoResponse, tags=["Todos"])
def mark_todo_incomplete(todo_id: int):
    """
    Mark a todo item as incomplete.
    """
    try:
        item = todo_service.mark_incomplete(todo_id)
        return item
    except TodoNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


if __name__ == "__main__":
    import argparse
    
    # Check if --serve flag is present before any other parsing
    if '--serve' in sys.argv:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        # Run CLI mode - pass all arguments to the CLI parser
        main()