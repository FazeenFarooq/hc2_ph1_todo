"""
CLI interface handler for the Todo application.
"""

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

    def _display_menu(self):
        """Display the main menu options."""
        print("\n" + "=" * 40)
        print("       TODO APPLICATION MENU")
        print("=" * 40)
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Quit")
        print("=" * 40)

    def _get_valid_input(self, prompt, required=True, min_length=1):
        """
        Get validated input from user.
        
        Args:
            prompt: The prompt to display
            required: Whether input is required
            min_length: Minimum length of input
            
        Returns:
            str: Validated user input
        """
        while True:
            try:
                user_input = input(prompt).strip()
                if not user_input and required:
                    print("This field is required. Please enter a value.")
                    continue
                if len(user_input) < min_length:
                    print(f"Input must be at least {min_length} character(s).")
                    continue
                return user_input
            except EOFError:
                print("\nUse option 7 to quit.")
                continue
            except KeyboardInterrupt:
                print("\n\nUse option 7 to quit.")
                continue

    def _get_valid_int(self, prompt, min_value=None, max_value=None):
        """
        Get a valid integer input from user.
        
        Args:
            prompt: The prompt to display
            min_value: Minimum allowed value
            max_value: Maximum allowed value
            
        Returns:
            int: Validated integer
        """
        while True:
            try:
                user_input = input(prompt).strip()
                value = int(user_input)
                
                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}.")
                    continue
                if max_value is not None and value > max_value:
                    print(f"Value must be at most {max_value}.")
                    continue
                return value
            except ValueError:
                print("Please enter a valid number.")
                continue
            except EOFError:
                print("\nUse option 7 to quit.")
                continue
            except KeyboardInterrupt:
                print("\n\nUse option 7 to quit.")
                continue

    def _handle_add(self):
        """Handle adding a new task."""
        print("\n--- Add New Task ---")
        title = self._get_valid_input("Enter task title: ")
        description = self._get_valid_input("Enter task description (optional, press Enter to skip): ", required=False)
        
        try:
            new_item = self.todo_service.add_item(title, description)
            print(f"\n[OK] Task added successfully with ID: {new_item.id}")
        except ValueError as e:
            print(f"\n[ERROR] {e}")

    def _handle_update(self):
        """Handle updating an existing task."""
        print("\n--- Update Task ---")
        
        items = self.todo_service.list_items()
        if not items:
            print("No tasks available to update.")
            return
        
        self._display_tasks()
        
        task_id = self._get_valid_int("Enter task ID to update: ", min_value=1)
        
        try:
            item = self.todo_service.get_item(task_id)
            print(f"\nCurrent task: {item.title}")
            print(f"Current description: {item.description or '(none)'}")
            print("\nEnter new values (press Enter to keep current):")
            
            new_title = self._get_valid_input(f"New title [{item.title}]: ", required=False)
            new_description = self._get_valid_input("New description: ", required=False)
            
            # Use current values if new values are empty
            title = new_title if new_title else item.title
            description = new_description if new_description else item.description
            
            updated_item = self.todo_service.update_item(task_id, title=title, description=description)
            print(f"\n[OK] Task ID {updated_item.id} updated successfully!")
        except TodoNotFoundException:
            print(f"\n[ERROR] Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"\n[ERROR] {e}")

    def _handle_delete(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")
        
        items = self.todo_service.list_items()
        if not items:
            print("No tasks available to delete.")
            return
        
        self._display_tasks()
        
        task_id = self._get_valid_int("Enter task ID to delete: ", min_value=1)
        
        try:
            self.todo_service.delete_item(task_id)
            print(f"\n[OK] Task ID {task_id} deleted successfully!")
        except TodoNotFoundException:
            print(f"\n[ERROR] Task with ID {task_id} not found.")

    def _handle_view(self):
        """Handle viewing all tasks."""
        print("\n--- View Tasks ---")
        
        items = self.todo_service.list_items()
        
        if not items:
            print("No tasks found. Add a task to get started!")
            return
        
        self._display_tasks()
        print(f"\nTotal: {len(items)} task(s)")

    def _handle_complete(self):
        """Handle marking a task as complete."""
        print("\n--- Mark Task Complete ---")
        
        items = self.todo_service.list_items()
        if not items:
            print("No tasks available.")
            return
        
        self._display_tasks()
        
        task_id = self._get_valid_int("Enter task ID to mark complete: ", min_value=1)
        
        try:
            item = self.todo_service.mark_complete(task_id)
            print(f"\n[OK] Task ID {item.id} marked as complete!")
        except TodoNotFoundException:
            print(f"\n[ERROR] Task with ID {task_id} not found.")

    def _handle_incomplete(self):
        """Handle marking a task as incomplete."""
        print("\n--- Mark Task Incomplete ---")
        
        items = self.todo_service.list_items()
        if not items:
            print("No tasks available.")
            return
        
        self._display_tasks()
        
        task_id = self._get_valid_int("Enter task ID to mark incomplete: ", min_value=1)
        
        try:
            item = self.todo_service.mark_incomplete(task_id)
            print(f"\n[OK] Task ID {item.id} marked as incomplete!")
        except TodoNotFoundException:
            print(f"\n[ERROR] Task with ID {task_id} not found.")

    def _display_tasks(self):
        """Display all tasks in a formatted list."""
        items = self.todo_service.list_items()
        
        if not items:
            print("No tasks found.")
            return
        
        print(f"\n{'ID':<4} {'Status':<8} {'Title':<30} {'Description'}")
        print("-" * 70)
        
        for item in items:
            status = "[X]" if item.completed else "[ ]"
            title = item.title[:27] + "..." if len(item.title) > 30 else item.title
            desc = (item.description[:30] + "...") if len(item.description) > 30 else (item.description or "-")
            print(f"{item.id:<4} {status:<8} {title:<30} {desc}")

    def run(self):
        """
        Run the interactive CLI interface.
        Displays menu repeatedly until user chooses to quit.
        """
        print("\n" + "=" * 40)
        print("  Welcome to Todo Application!")
        print("=" * 40)
        
        while True:
            self._display_menu()
            
            try:
                choice = self._get_valid_int("Enter your choice (1-7): ", min_value=1, max_value=7)
                
                if choice == 1:
                    self._handle_add()
                elif choice == 2:
                    self._handle_update()
                elif choice == 3:
                    self._handle_delete()
                elif choice == 4:
                    self._handle_view()
                elif choice == 5:
                    self._handle_complete()
                elif choice == 6:
                    self._handle_incomplete()
                elif choice == 7:
                    print("\n" + "=" * 40)
                    print("  Thank you for using Todo Application!")
                    print("  Goodbye!")
                    print("=" * 40)
                    break
                else:
                    print("\n[ERROR] Invalid choice. Please enter a number between 1 and 7.")
                    
            except KeyboardInterrupt:
                print("\n\n[WARNING] Interrupted! Use option 7 to quit properly.")
                continue
            except Exception as e:
                print(f"\n[ERROR] An unexpected error occurred: {e}")
                print("Please try again.")
                continue


def main():
    """Main entry point for the CLI interface."""
    service = TodoService()
    cli = CLIInterface(service)
    cli.run()


if __name__ == "__main__":
    main()
