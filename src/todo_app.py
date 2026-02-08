"""
Main application entry point for the CLI Todo application.
"""

import os
import sys

# Add the src directory to the path so we can import from sibling directories
sys.path.insert(0, os.path.dirname(__file__))

from services.todo_service import TodoService
from cli.cli_interface import CLIInterface


def main():
    """
    Main entry point for the application.
    Initializes the service and CLI interface, then runs the application.
    """
    # Initialize the todo service
    todo_service = TodoService()

    # Initialize the CLI interface with the service
    cli_interface = CLIInterface(todo_service)

    # Run the CLI interface
    cli_interface.run()


if __name__ == "__main__":
    main()