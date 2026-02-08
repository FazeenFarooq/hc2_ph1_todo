"""
Unit tests for updating todos in TodoService.
"""
import pytest
from src.models.todo_item import TodoItem
from src.services.todo_service import TodoService, TodoNotFoundException


def test_update_existing_todo_title():
    """Test updating the title of an existing todo."""
    service = TodoService()
    original_item = service.add_item("Original Title", "Original Description")
    
    updated_item = service.update_item(original_item.id, title="Updated Title")
    
    assert updated_item.id == original_item.id
    assert updated_item.title == "Updated Title"
    assert updated_item.description == "Original Description"
    assert updated_item.completed == original_item.completed


def test_update_existing_todo_description():
    """Test updating the description of an existing todo."""
    service = TodoService()
    original_item = service.add_item("Original Title", "Original Description")
    
    updated_item = service.update_item(original_item.id, description="Updated Description")
    
    assert updated_item.id == original_item.id
    assert updated_item.title == "Original Title"
    assert updated_item.description == "Updated Description"
    assert updated_item.completed == original_item.completed


def test_update_existing_todo_both_fields():
    """Test updating both title and description of an existing todo."""
    service = TodoService()
    original_item = service.add_item("Original Title", "Original Description")
    
    updated_item = service.update_item(
        original_item.id, 
        title="Updated Title", 
        description="Updated Description"
    )
    
    assert updated_item.id == original_item.id
    assert updated_item.title == "Updated Title"
    assert updated_item.description == "Updated Description"
    assert updated_item.completed == original_item.completed


def test_update_nonexistent_todo_raises_exception():
    """Test that updating a nonexistent todo raises TodoNotFoundException."""
    service = TodoService()
    
    with pytest.raises(TodoNotFoundException):
        service.update_item(999, title="Updated Title")


def test_updated_todo_persists_in_service():
    """Test that the updated todo is reflected when retrieving from the service."""
    service = TodoService()
    original_item = service.add_item("Original Title", "Original Description")
    
    service.update_item(original_item.id, title="Updated Title")
    
    retrieved_item = service.get_item(original_item.id)
    assert retrieved_item.title == "Updated Title"
    assert retrieved_item.description == "Original Description"


def test_update_todo_does_not_change_id_or_completion_status():
    """Test that updating a todo doesn't change its ID or completion status."""
    service = TodoService()
    original_item = service.add_item("Original Title", "Original Description")
    # Mark as complete to test that status persists after update
    service.mark_complete(original_item.id)
    
    updated_item = service.update_item(original_item.id, title="Updated Title")
    
    assert updated_item.id == original_item.id
    assert updated_item.completed == True  # Should remain completed