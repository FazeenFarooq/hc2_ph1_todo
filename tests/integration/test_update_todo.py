"""
Integration test for updating todos via CLI.
"""
import sys
from io import StringIO
from unittest.mock import patch
from src.services.todo_service import TodoService
from src.cli.cli_interface import CLIInterface


def test_update_todo_via_cli():
    """Test updating a todo item via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Add a todo first
    added_item = service.add_item("Original Title", "Original Description")
    
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI to update the todo
        cli.run(['update', '--id', str(added_item.id), '--title', 'Updated Title'])
    
    # Verify the output
    output = captured_output.getvalue().strip()
    assert f"Updated todo item with ID {added_item.id}" in output
    
    # Verify the item was updated in the service
    updated_item = service.get_item(added_item.id)
    assert updated_item.title == "Updated Title"
    assert updated_item.description == "Original Description"


def test_update_todo_with_new_description_via_cli():
    """Test updating a todo's description via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Add a todo first
    added_item = service.add_item("Original Title", "Original Description")
    
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI to update the todo's description
        cli.run(['update', '--id', str(added_item.id), '--description', 'Updated Description'])
    
    # Verify the output
    output = captured_output.getvalue().strip()
    assert f"Updated todo item with ID {added_item.id}" in output
    
    # Verify the item was updated in the service
    updated_item = service.get_item(added_item.id)
    assert updated_item.title == "Original Title"
    assert updated_item.description == "Updated Description"


def test_update_todo_with_both_title_and_description_via_cli():
    """Test updating both title and description of a todo via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Add a todo first
    added_item = service.add_item("Original Title", "Original Description")
    
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI to update both title and description
        cli.run([
            'update', 
            '--id', str(added_item.id), 
            '--title', 'Updated Title',
            '--description', 'Updated Description'
        ])
    
    # Verify the output
    output = captured_output.getvalue().strip()
    assert f"Updated todo item with ID {added_item.id}" in output
    
    # Verify the item was updated in the service
    updated_item = service.get_item(added_item.id)
    assert updated_item.title == "Updated Title"
    assert updated_item.description == "Updated Description"


def test_update_nonexistent_todo_via_cli():
    """Test updating a nonexistent todo via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Capture stderr
    captured_output = StringIO()
    with patch('sys.stderr', captured_output):
        # Run the CLI to update a nonexistent todo
        try:
            cli.run(['update', '--id', '999', '--title', 'Updated Title'])
        except SystemExit:
            pass  # Expected to exit with error
    
    # Verify the error output
    output = captured_output.getvalue()
    assert "not found" in output