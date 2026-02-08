"""
Integration test for listing todos via CLI.
"""
import sys
from io import StringIO
from unittest.mock import patch
from src.services.todo_service import TodoService
from src.cli.cli_interface import CLIInterface


def test_list_empty_todos_via_cli():
    """Test listing todos when there are no todos."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI for listing
        cli.run(['list'])
    
    # Verify the output
    output = captured_output.getvalue().strip()
    assert "No todo items found." in output


def test_list_single_todo_via_cli():
    """Test listing when there is one todo."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Add a todo first
    service.add_item("Test Title", "Test Description")
    
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI for listing
        cli.run(['list'])
    
    # Verify the output contains the added todo
    output = captured_output.getvalue()
    assert "Test Title" in output
    assert "Test Description" in output
    assert "○" in output  # Uncompleted status


def test_list_multiple_todos_via_cli():
    """Test listing when there are multiple todos."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Add multiple todos
    service.add_item("First Todo", "First Description")
    service.add_item("Second Todo", "Second Description")
    service.mark_complete(service.items[1].id)  # Mark the first one as complete
    
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI for listing
        cli.run(['list'])
    
    # Verify the output contains all todos
    output = captured_output.getvalue()
    assert "First Todo" in output
    assert "Second Todo" in output
    assert "First Description" in output
    assert "Second Description" in output
    assert "✓" in output  # Completed status for first item
    assert "○" in output  # Uncompleted status for second item