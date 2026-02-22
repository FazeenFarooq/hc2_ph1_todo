"""
CLI interface handler for the Todo application.
"""

import argparse
import sys
import os

# Add the src directory to the path so we can import from sibling directories
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.todo_service import TodoService, TodoNotFoundException


class CLIInterface:
    """
    Handles command-line interface interactions for the Todo application.
    """
    
    def __init__(self, todo_service):
        """
        Initialize the CLI interface with a TodoService instance.
        
        Args:
            todo_service (TodoService): The service to handle todo operations
        """
        self.todo_service = todo_service
        self.parser = self._create_parser()
    
    def _create_parser(self):
        """
        Create and configure the argument parser.
        
        Returns:
            argparse.ArgumentParser: Configured argument parser
        """
        parser = argparse.ArgumentParser(
            prog='todo_app',
            description='A simple CLI Todo application',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  %(prog)s add --title "Buy groceries" --description "Milk, bread, eggs"
  %(prog)s list
  %(prog)s update --id 1 --title "Buy groceries and vegetables"
  %(prog)s delete --id 1
  %(prog)s complete --id 1
  %(prog)s incomplete --id 1
            """
        )
        
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # Add command
        add_parser = subparsers.add_parser('add', help='Add a new todo item')
        add_parser.add_argument('--title', required=True, help='Title of the todo item')
        add_parser.add_argument('--description', required=False, default='', help='Description of the todo item')
        
        # List command
        list_parser = subparsers.add_parser('list', help='List all todo items')
        
        # Update command
        update_parser = subparsers.add_parser('update', help='Update an existing todo item')
        update_parser.add_argument('--id', type=int, required=True, help='ID of the todo item to update')
        update_parser.add_argument('--title', required=False, help='New title for the todo item')
        update_parser.add_argument('--description', required=False, help='New description for the todo item')
        
        # Delete command
        delete_parser = subparsers.add_parser('delete', help='Delete a todo item')
        delete_parser.add_argument('--id', type=int, required=True, help='ID of the todo item to delete')
        
        # Complete command
        complete_parser = subparsers.add_parser('complete', help='Mark a todo item as complete')
        complete_parser.add_argument('--id', type=int, required=True, help='ID of the todo item to mark complete')
        
        # Incomplete command
        incomplete_parser = subparsers.add_parser('incomplete', help='Mark a todo item as incomplete')
        incomplete_parser.add_argument('--id', type=int, required=True, help='ID of the todo item to mark incomplete')
        
        return parser
    
    def run(self, args=None):
        """
        Run the CLI interface with the provided arguments.
        
        Args:
            args (list, optional): Command-line arguments. Defaults to None (uses sys.argv).
        """
        if args is None:
            args = sys.argv[1:]
        
        parsed_args = self.parser.parse_args(args)
        
        if not parsed_args.command:
            self.parser.print_help()
            return
        
        try:
            if parsed_args.command == 'add':
                self._handle_add(parsed_args)
            elif parsed_args.command == 'list':
                self._handle_list()
            elif parsed_args.command == 'update':
                self._handle_update(parsed_args)
            elif parsed_args.command == 'delete':
                self._handle_delete(parsed_args)
            elif parsed_args.command == 'complete':
                self._handle_complete(parsed_args)
            elif parsed_args.command == 'incomplete':
                self._handle_incomplete(parsed_args)
            else:
                self.parser.print_help()
        except TodoNotFoundException as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}", file=sys.stderr)
            sys.exit(1)
    
    def _handle_add(self, args):
        """
        Handle the 'add' command.
        
        Args:
            args: Parsed arguments for the add command
        """
        try:
            new_item = self.todo_service.add_item(args.title, args.description)
            print(f"Added todo item with ID {new_item.id}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    def _handle_list(self):
        """Handle the 'list' command."""
        items = self.todo_service.list_items()

        if not items:
            print("No todo items found.")
            return

        print(f"{'ID':<4} {'Status':<8} {'Title':<30} {'Description'}")
        print("-" * 70)

        for item in items:
            status = "[X]" if item.completed else "[ ]"
            title = item.title[:27] + "..." if len(item.title) > 30 else item.title
            desc = item.description[:30] + "..." if len(item.description) > 30 else item.description
            print(f"{item.id:<4} {status:<8} {title:<30} {desc}")
    
    def _handle_update(self, args):
        """
        Handle the 'update' command.
        
        Args:
            args: Parsed arguments for the update command
        """
        try:
            updated_item = self.todo_service.update_item(
                args.id,
                title=args.title,
                description=args.description
            )
            print(f"Updated todo item with ID {updated_item.id}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    def _handle_delete(self, args):
        """
        Handle the 'delete' command.
        
        Args:
            args: Parsed arguments for the delete command
        """
        try:
            self.todo_service.delete_item(args.id)
            print(f"Deleted todo item with ID {args.id}")
        except TodoNotFoundException as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    def _handle_complete(self, args):
        """
        Handle the 'complete' command.
        
        Args:
            args: Parsed arguments for the complete command
        """
        try:
            item = self.todo_service.mark_complete(args.id)
            print(f"Marked todo item with ID {item.id} as complete")
        except TodoNotFoundException as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    def _handle_incomplete(self, args):
        """
        Handle the 'incomplete' command.
        
        Args:
            args: Parsed arguments for the incomplete command
        """
        try:
            item = self.todo_service.mark_incomplete(args.id)
            print(f"Marked todo item with ID {item.id} as incomplete")
        except TodoNotFoundException as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


def main():
    """Main entry point for the CLI interface."""
    service = TodoService()
    cli = CLIInterface(service)
    cli.run()


if __name__ == "__main__":
    main()