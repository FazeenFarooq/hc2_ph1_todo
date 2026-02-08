"""
Integration test for marking todos complete/incomplete via CLI.
"""
import sys
from io import StringIO
from unittest.mock import patch
from src.services.todo_service import TodoService
from src.cli.cli_interface import CLIInterface


def test_mark_todo_complete_via_cli():
    """Test marking a todo as complete via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Add a todo first
    added_item = service.add_item("Test Title", "Test Description")
    
    # Verify initial state
    assert service.get_item(added_item.id).completed is False
    
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI to mark the todo as complete
        cli.run(['complete', '--id', str(added_item.id)])
    
    # Verify the output
    output = captured_output.getvalue().strip()
    assert f"Marked todo item with ID {added_item.id} as complete" in output
    
    # Verify the item was marked as complete in the service
    assert service.get_item(added_item.id).completed is True


def test_mark_todo_incomplete_via_cli():
    """Test marking a todo as incomplete via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Add a todo first and mark it as complete
    added_item = service.add_item("Test Title", "Test Description")
    service.mark_complete(added_item.id)
    
    # Verify initial state
    assert service.get_item(added_item.id).completed is True
    
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI to mark the todo as incomplete
        cli.run(['incomplete', '--id', str(added_item.id)])
    
    # Verify the output
    output = captured_output.getvalue().strip()
    assert f"Marked todo item with ID {added_item.id} as incomplete" in output
    
    # Verify the item was marked as incomplete in the service
    assert service.get_item(added_item.id).completed is False


def test_mark_nonexistent_todo_via_cli():
    """Test marking a nonexistent todo via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Capture stderr for complete command
    captured_output = StringIO()
    with patch('sys.stderr', captured_output):
        try:
            cli.run(['complete', '--id', '999'])
        except SystemExit:
            pass  # Expected to exit with error
    
    # Verify the error output
    output = captured_output.getvalue()
    assert "not found" in output
    
    # Capture stderr for incomplete command
    captured_output = StringIO()
    with patch('sys.stderr', captured_output):
        try:
            cli.run(['incomplete', '--id', '999'])
        except SystemExit:
            pass  # Expected to exit with error
    
    # Verify the error output
    output = captured_output.getvalue()
    assert "not found" in output


def test_mark_complete_then_incomplete_via_cli():
    """Test marking a todo complete then incomplete via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Add a todo first
    added_item = service.add_item("Test Title", "Test Description")
    
    # Verify initial state
    assert service.get_item(added_item.id).completed is False
    
    # Mark as complete via CLI
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        cli.run(['complete', '--id', str(added_item.id)])
    
    output = captured_output.getvalue().strip()
    assert f"Marked todo item with ID {added_item.id} as complete" in output
    assert service.get_item(added_item.id).completed is True
    
    # Mark as incomplete via CLI
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        cli.run(['incomplete', '--id', str(added_item.id)])
    
    output = captured_output.getvalue().strip()
    assert f"Marked todo item with ID {added_item.id} as incomplete" in output
    assert service.get_item(added_item.id).completed is False