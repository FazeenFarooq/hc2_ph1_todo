"""
Unit tests for TodoItem creation.
"""
import pytest
from src.models.todo_item import TodoItem


def test_create_valid_todo_item():
    """Test creating a valid TodoItem with title and description."""
    item = TodoItem(id=1, title="Test Title", description="Test Description")
    
    assert item.id == 1
    assert item.title == "Test Title"
    assert item.description == "Test Description"
    assert item.completed is False


def test_create_todo_item_without_description():
    """Test creating a TodoItem without providing a description."""
    item = TodoItem(id=1, title="Test Title")
    
    assert item.id == 1
    assert item.title == "Test Title"
    assert item.description == ""
    assert item.completed is False


def test_create_completed_todo_item():
    """Test creating a TodoItem with completed status."""
    item = TodoItem(id=1, title="Test Title", description="Test Description", completed=True)
    
    assert item.id == 1
    assert item.title == "Test Title"
    assert item.description == "Test Description"
    assert item.completed is True


def test_create_todo_item_empty_title_error():
    """Test that creating a TodoItem with empty title raises ValueError."""
    with pytest.raises(ValueError):
        TodoItem(id=1, title="", description="Test Description")


def test_create_todo_item_none_title_error():
    """Test that creating a TodoItem with None title raises ValueError."""
    with pytest.raises(ValueError):
        TodoItem(id=1, title=None, description="Test Description")


def test_create_todo_item_whitespace_only_title_error():
    """Test that creating a TodoItem with whitespace-only title raises ValueError."""
    with pytest.raises(ValueError):
        TodoItem(id=1, title="   ", description="Test Description")


def test_todo_item_repr():
    """Test the string representation of a TodoItem."""
    item = TodoItem(id=1, title="Test Title", description="Test Description", completed=True)
    repr_str = repr(item)
    
    assert "TodoItem" in repr_str
    assert "id=1" in repr_str
    assert "title='Test Title'" in repr_str
    assert "description='Test Description'" in repr_str
    assert "completed=True" in repr_str


def test_todo_item_equality():
    """Test equality comparison between TodoItems."""
    item1 = TodoItem(id=1, title="Test Title", description="Test Description", completed=True)
    item2 = TodoItem(id=1, title="Test Title", description="Test Description", completed=True)
    item3 = TodoItem(id=2, title="Different Title", description="Test Description", completed=True)
    
    assert item1 == item2
    assert item1 != item3
    assert item1 != "not a todo item"


def test_todo_item_to_dict():
    """Test converting a TodoItem to a dictionary."""
    item = TodoItem(id=1, title="Test Title", description="Test Description", completed=True)
    item_dict = item.to_dict()
    
    assert item_dict == {
        "id": 1,
        "title": "Test Title",
        "description": "Test Description",
        "completed": True
    }


def test_todo_item_from_dict():
    """Test creating a TodoItem from a dictionary."""
    data = {
        "id": 1,
        "title": "Test Title",
        "description": "Test Description",
        "completed": True
    }
    item = TodoItem.from_dict(data)
    
    assert item.id == 1
    assert item.title == "Test Title"
    assert item.description == "Test Description"
    assert item.completed is True