"""
Unit tests for deleting todos in TodoService.
"""
import pytest
from src.models.todo_item import TodoItem
from src.services.todo_service import TodoService, TodoNotFoundException


def test_delete_existing_todo():
    """Test deleting an existing todo."""
    service = TodoService()
    added_item = service.add_item("Test Title", "Test Description")
    
    # Verify the item exists before deletion
    assert len(service.list_items()) == 1
    assert added_item.id in service.items
    
    # Delete the item
    service.delete_item(added_item.id)
    
    # Verify the item is gone
    assert len(service.list_items()) == 0
    assert added_item.id not in service.items


def test_delete_nonexistent_todo_raises_exception():
    """Test that deleting a nonexistent todo raises TodoNotFoundException."""
    service = TodoService()
    
    with pytest.raises(TodoNotFoundException):
        service.delete_item(999)


def test_delete_middle_item_from_multiple():
    """Test deleting an item from the middle of multiple items."""
    service = TodoService()
    first_item = service.add_item("First", "First Description")
    second_item = service.add_item("Second", "Second Description")
    third_item = service.add_item("Third", "Third Description")
    
    # Verify all items exist
    assert len(service.list_items()) == 3
    
    # Delete the middle item
    service.delete_item(second_item.id)
    
    # Verify only the other two items remain
    remaining_items = service.list_items()
    assert len(remaining_items) == 2
    assert first_item in remaining_items
    assert third_item in remaining_items
    assert second_item not in remaining_items


def test_delete_item_then_verify_by_get():
    """Test that after deleting an item, getting it raises an exception."""
    service = TodoService()
    added_item = service.add_item("Test Title", "Test Description")
    
    # Delete the item
    service.delete_item(added_item.id)
    
    # Verify that getting the item now raises an exception
    with pytest.raises(TodoNotFoundException):
        service.get_item(added_item.id)


def test_delete_all_items():
    """Test deleting all items one by one."""
    service = TodoService()
    first_item = service.add_item("First", "First Description")
    second_item = service.add_item("Second", "Second Description")
    
    # Verify both items exist
    assert len(service.list_items()) == 2
    
    # Delete both items
    service.delete_item(first_item.id)
    service.delete_item(second_item.id)
    
    # Verify no items remain
    assert len(service.list_items()) == 0


def test_delete_preserves_other_items():
    """Test that deleting one item doesn't affect others."""
    service = TodoService()
    first_item = service.add_item("First", "First Description")
    second_item = service.add_item("Second", "Second Description")
    third_item = service.add_item("Third", "Third Description")
    
    # Delete the second item
    service.delete_item(second_item.id)
    
    # Verify the other items are unchanged
    remaining_items = service.list_items()
    assert len(remaining_items) == 2
    
    # Find the remaining items
    remaining_ids = [item.id for item in remaining_items]
    assert first_item.id in remaining_ids
    assert third_item.id in remaining_ids
    assert second_item.id not in remaining_ids
    
    # Verify the properties of the remaining items are unchanged
    for item in remaining_items:
        if item.id == first_item.id:
            assert item.title == "First"
            assert item.description == "First Description"
        elif item.id == third_item.id:
            assert item.title == "Third"
            assert item.description == "Third Description"