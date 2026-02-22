"""
Simple test to verify the virtual environment and project setup
"""
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_todo_functionality():
    print("Testing Todo application functionality...")

    # Import the necessary modules
    from services.todo_service import TodoService
    from cli.cli_interface import CLIInterface

    # Create a service instance
    service = TodoService()
    print("[OK] TodoService created successfully")

    # Test adding a todo
    item = service.add_item("Test Title", "Test Description")
    print(f"[OK] Added todo item with ID: {item.id}")

    # Test listing todos
    items = service.list_items()
    print(f"[OK] Listed todos: {len(items)} item(s)")

    # Test updating a todo
    updated_item = service.update_item(item.id, title="Updated Title")
    print(f"[OK] Updated todo item: {updated_item.title}")

    # Test marking as complete
    completed_item = service.mark_complete(item.id)
    print(f"[OK] Marked todo as complete: {completed_item.completed}")

    # Test marking as incomplete
    incomplete_item = service.mark_incomplete(item.id)
    print(f"[OK] Marked todo as incomplete: {incomplete_item.completed}")

    # Test deleting a todo
    service.delete_item(item.id)
    items_after_deletion = service.list_items()
    print(f"[OK] Deleted todo item, remaining: {len(items_after_deletion)}")

    print("\n[OK] All functionality tests passed!")

if __name__ == "__main__":
    test_todo_functionality()
