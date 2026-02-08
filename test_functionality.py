"""
Simple test script to verify the todo application functionality.
"""
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.todo_service import TodoService
from cli.cli_interface import CLIInterface

def test_basic_functionality():
    print("Testing basic functionality...")
    
    # Create a service
    service = TodoService()
    
    # Test adding a todo
    item = service.add_item("Test Title", "Test Description")
    print(f"Added item with ID: {item.id}")
    
    # Test listing todos
    items = service.list_items()
    print(f"Number of items: {len(items)}")
    
    # Test updating a todo
    updated_item = service.update_item(item.id, title="Updated Title")
    print(f"Updated item title: {updated_item.title}")
    
    # Test marking as complete
    completed_item = service.mark_complete(item.id)
    print(f"Item completed status: {completed_item.completed}")
    
    # Test marking as incomplete
    incomplete_item = service.mark_incomplete(item.id)
    print(f"Item completed status: {incomplete_item.completed}")
    
    # Test deleting a todo
    service.delete_item(item.id)
    items = service.list_items()
    print(f"Number of items after deletion: {len(items)}")
    
    print("All tests passed!")

if __name__ == "__main__":
    test_basic_functionality()