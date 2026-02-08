"""
Unit tests for toggling completion status in TodoService.
"""
import pytest
from src.models.todo_item import TodoItem
from src.services.todo_service import TodoService, TodoNotFoundException


def test_mark_todo_complete():
    """Test marking a todo item as complete."""
    service = TodoService()
    item = service.add_item("Test Title", "Test Description")
    
    # Verify initial state
    assert item.completed is False
    
    # Mark as complete
    completed_item = service.mark_complete(item.id)
    
    # Verify the item is now complete
    assert completed_item.completed is True
    assert service.get_item(item.id).completed is True


def test_mark_todo_incomplete():
    """Test marking a todo item as incomplete."""
    service = TodoService()
    item = service.add_item("Test Title", "Test Description")
    
    # Mark as complete first
    service.mark_complete(item.id)
    assert service.get_item(item.id).completed is True
    
    # Mark as incomplete
    incomplete_item = service.mark_incomplete(item.id)
    
    # Verify the item is now incomplete
    assert incomplete_item.completed is False
    assert service.get_item(item.id).completed is False


def test_mark_nonexistent_todo_raises_exception():
    """Test that marking a nonexistent todo raises TodoNotFoundException."""
    service = TodoService()
    
    with pytest.raises(TodoNotFoundException):
        service.mark_complete(999)
    
    with pytest.raises(TodoNotFoundException):
        service.mark_incomplete(999)


def test_mark_complete_preserves_other_properties():
    """Test that marking complete doesn't change other properties."""
    service = TodoService()
    item = service.add_item("Test Title", "Test Description")
    
    # Mark as complete
    completed_item = service.mark_complete(item.id)
    
    # Verify other properties are unchanged
    assert completed_item.id == item.id
    assert completed_item.title == item.title
    assert completed_item.description == item.description
    assert completed_item.completed is True


def test_mark_incomplete_preserves_other_properties():
    """Test that marking incomplete doesn't change other properties."""
    service = TodoService()
    item = service.add_item("Test Title", "Test Description")
    
    # Mark as complete first
    service.mark_complete(item.id)
    
    # Mark as incomplete
    incomplete_item = service.mark_incomplete(item.id)
    
    # Verify other properties are unchanged
    assert incomplete_item.id == item.id
    assert incomplete_item.title == item.title
    assert incomplete_item.description == item.description
    assert incomplete_item.completed is False


def test_mark_complete_and_incomplete_cycle():
    """Test marking an item complete and then incomplete."""
    service = TodoService()
    item = service.add_item("Test Title", "Test Description")
    
    # Initially incomplete
    assert item.completed is False
    
    # Mark complete
    service.mark_complete(item.id)
    assert service.get_item(item.id).completed is True
    
    # Mark incomplete
    service.mark_incomplete(item.id)
    assert service.get_item(item.id).completed is False
    
    # Mark complete again
    service.mark_complete(item.id)
    assert service.get_item(item.id).completed is True


def test_mark_multiple_items():
    """Test marking multiple items."""
    service = TodoService()
    first_item = service.add_item("First", "First Description")
    second_item = service.add_item("Second", "Second Description")
    third_item = service.add_item("Third", "Third Description")
    
    # Mark first and third as complete, leave second incomplete
    service.mark_complete(first_item.id)
    service.mark_complete(third_item.id)
    
    # Verify states
    assert service.get_item(first_item.id).completed is True
    assert service.get_item(second_item.id).completed is False
    assert service.get_item(third_item.id).completed is True
    
    # Mark first as incomplete
    service.mark_incomplete(first_item.id)
    
    # Verify updated states
    assert service.get_item(first_item.id).completed is False
    assert service.get_item(second_item.id).completed is False
    assert service.get_item(third_item.id).completed is True