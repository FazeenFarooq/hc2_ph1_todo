"""
Simple test to check imports
"""
import sys
import os

print("Python executable:", sys.executable)
print("Python version:", sys.version_info)

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    print("Attempting to import TodoService...")
    from services.todo_service import TodoService
    print("✓ TodoService imported successfully")
    
    print("Attempting to import CLIInterface...")
    from cli.cli_interface import CLIInterface
    print("✓ CLIInterface imported successfully")
    
    print("Attempting to import todo_app main...")
    from todo_app import main
    print("✓ todo_app main imported successfully")
    
    print("\nAll imports successful!")
    
    # Test creating a service
    service = TodoService()
    print("✓ TodoService instantiated successfully")
    
    # Test adding an item
    item = service.add_item("Test", "Description")
    print(f"✓ Added item with ID: {item.id}")
    
except ImportError as e:
    print(f"Import error: {e}")
    import traceback
    traceback.print_exc()
except Exception as e:
    print(f"Other error: {e}")
    import traceback
    traceback.print_exc()