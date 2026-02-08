"""
Integration test for deleting todos via CLI.
"""
import sys
from io import StringIO
from unittest.mock import patch
from src.services.todo_service import TodoService
from src.cli.cli_interface import CLIInterface


def test_delete_todo_via_cli():
    """Test deleting a todo item via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Add a todo first
    added_item = service.add_item("Test Title", "Test Description")
    
    # Verify the item exists before deletion
    assert len(service.list_items()) == 1
    
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI to delete the todo
        cli.run(['delete', '--id', str(added_item.id)])
    
    # Verify the output
    output = captured_output.getvalue().strip()
    assert f"Deleted todo item with ID {added_item.id}" in output
    
    # Verify the item was deleted from the service
    assert len(service.list_items()) == 0


def test_delete_nonexistent_todo_via_cli():
    """Test deleting a nonexistent todo via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Capture stderr
    captured_output = StringIO()
    with patch('sys.stderr', captured_output):
        # Run the CLI to delete a nonexistent todo
        try:
            cli.run(['delete', '--id', '999'])
        except SystemExit:
            pass  # Expected to exit with error
    
    # Verify the error output
    output = captured_output.getvalue()
    assert "not found" in output


def test_delete_one_of_multiple_todos_via_cli():
    """Test deleting one of multiple todos via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Add multiple todos
    first_item = service.add_item("First", "First Description")
    second_item = service.add_item("Second", "Second Description")
    third_item = service.add_item("Third", "Third Description")
    
    # Verify all items exist
    assert len(service.list_items()) == 3
    
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI to delete the second todo
        cli.run(['delete', '--id', str(second_item.id)])
    
    # Verify the output
    output = captured_output.getvalue().strip()
    assert f"Deleted todo item with ID {second_item.id}" in output
    
    # Verify only the other two items remain
    remaining_items = service.list_items()
    assert len(remaining_items) == 2
    remaining_ids = [item.id for item in remaining_items]
    assert first_item.id in remaining_ids
    assert third_item.id in remaining_ids
    assert second_item.id not in remaining_ids