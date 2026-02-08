"""
Integration test for adding todo via CLI.
"""
import sys
from io import StringIO
from unittest.mock import patch
from src.services.todo_service import TodoService
from src.cli.cli_interface import CLIInterface


def test_add_todo_via_cli():
    """Test adding a todo item via the CLI interface."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Mock sys.argv to simulate command line arguments
    with patch('sys.argv', ['todo_app', 'add', '--title', 'Test Title', '--description', 'Test Description']):
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            # Run the CLI with mocked arguments
            cli.run(['add', '--title', 'Test Title', '--description', 'Test Description'])
        
        # Verify the output
        output = captured_output.getvalue().strip()
        assert "Added todo item with ID 1" in output
    
    # Verify the item was added to the service
    items = service.list_items()
    assert len(items) == 1
    assert items[0].id == 1
    assert items[0].title == "Test Title"
    assert items[0].description == "Test Description"
    assert items[0].completed is False


def test_add_todo_via_cli_without_description():
    """Test adding a todo item via the CLI interface without description."""
    # Create a service and CLI interface
    service = TodoService()
    cli = CLIInterface(service)
    
    # Test adding without description
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        # Run the CLI with mocked arguments
        cli.run(['add', '--title', 'Test Title'])
    
    # Verify the output
    output = captured_output.getvalue().strip()
    assert "Added todo item with ID 1" in output
    
    # Verify the item was added to the service
    items = service.list_items()
    assert len(items) == 1
    assert items[0].id == 1
    assert items[0].title == "Test Title"
    assert items[0].description == ""
    assert items[0].completed is False