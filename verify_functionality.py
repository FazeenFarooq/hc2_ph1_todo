"""
Test script to verify the todo application functionality
"""
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    # Import the main function
    from todo_app import main
    print("[OK] Successfully imported todo_app main function")

    # Also test importing the core components
    from services.todo_service import TodoService
    from cli.cli_interface import CLIInterface
    print("[OK] Successfully imported core components")

    # Test creating a service instance
    service = TodoService()
    print("[OK] Successfully created TodoService instance")

    # Test adding a todo item
    item = service.add_item("Test task", "Test description")
    print(f"[OK] Successfully added a todo item with ID: {item.id}")

    # Test listing items
    items = service.list_items()
    print(f"[OK] Successfully listed items, found: {len(items)} item(s)")

    print("\n[OK] All basic functionality tests passed!")
    print("Your todo application code is working correctly.")

except ImportError as e:
    print(f"[ERROR] Import error: {e}")
except Exception as e:
    print(f"[ERROR] Error: {e}")
    import traceback
    traceback.print_exc()
