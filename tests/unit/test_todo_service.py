"""
Unit tests for listing todos in TodoService.
"""
import pytest
from src.models.todo_item import TodoItem
from src.services.todo_service import TodoService


def test_list_empty_todos():
    """Test listing when there are no todos."""
    service = TodoService()
    items = service.list_items()
    
    assert items == []
    assert len(items) == 0


def test_list_single_todo():
    """Test listing when there is one todo."""
    service = TodoService()
    service.add_item("Test Title", "Test Description")
    
    items = service.list_items()
    
    assert len(items) == 1
    assert items[0].title == "Test Title"
    assert items[0].description == "Test Description"
    assert items[0].completed is False


def test_list_multiple_todos():
    """Test listing when there are multiple todos."""
    service = TodoService()
    service.add_item("First Todo", "First Description")
    service.add_item("Second Todo", "Second Description")
    service.add_item("Third Todo", "Third Description")
    
    items = service.list_items()
    
    assert len(items) == 3
    assert items[0].title == "First Todo"
    assert items[1].title == "Second Todo"
    assert items[2].title == "Third Todo"


def test_list_todos_after_modifications():
    """Test listing todos after various operations."""
    service = TodoService()
    
    # Add some items
    service.add_item("Initial Todo", "Initial Description")
    service.add_item("Another Todo", "Another Description")
    
    # Verify initial state
    items = service.list_items()
    assert len(items) == 2
    
    # Update an item
    service.update_item(items[0].id, title="Updated Title")
    
    # Verify list reflects the update
    items = service.list_items()
    assert len(items) == 2
    assert items[0].title == "Updated Title"
    
    # Delete an item
    service.delete_item(items[1].id)
    
    # Verify list reflects the deletion
    items = service.list_items()
    assert len(items) == 1
    assert items[0].title == "Updated Title"