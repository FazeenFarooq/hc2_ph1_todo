"""
TodoService handles the business logic for todo operations.
"""

import json
import os

from models.todo_item import TodoItem


class TodoNotFoundException(Exception):
    """Exception raised when a todo item is not found."""
    pass


class TodoService:
    """
    Service class that manages the collection of TodoItem objects in memory.

    Attributes:
        items (dict): Dictionary mapping integer IDs to TodoItem objects
        next_id (int): Counter for generating unique IDs, starts at 1
    """

    def __init__(self, data_file=None):
        """Initialize the TodoService with an empty collection or load from file."""
        self.items = {}
        self.next_id = 1
        self.data_file = data_file or os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "todos.json"
        )
        self._load_data()
    
    def add_item(self, title, description=""):
        """
        Add a new todo item to the collection.
        
        Args:
            title (str): Title of the todo item
            description (str, optional): Description of the todo item. Defaults to "".
            
        Returns:
            TodoItem: The newly created TodoItem with a unique ID
        """
        # Create a new TodoItem with the next available ID
        new_item = TodoItem(id=self.next_id, title=title, description=description, completed=False)
        
        # Add the item to the collection
        self.items[self.next_id] = new_item
        
        # Increment the ID counter for the next item
        self.next_id += 1
        
        # Save to file
        self._save_data()
        
        return new_item
    
    def get_item(self, item_id):
        """
        Retrieve a todo item by its ID.
        
        Args:
            item_id (int): ID of the todo item to retrieve
            
        Returns:
            TodoItem: The todo item with the specified ID
            
        Raises:
            TodoNotFoundException: If no item exists with the specified ID
        """
        if item_id not in self.items:
            raise TodoNotFoundException(f"Todo item with ID {item_id} not found")
        
        return self.items[item_id]
    
    def list_items(self):
        """
        Retrieve all todo items in the collection.
        
        Returns:
            list: A list of all TodoItem objects in the collection
        """
        return list(self.items.values())
    
    def update_item(self, item_id, title=None, description=None):
        """
        Update an existing todo item.
        
        Args:
            item_id (int): ID of the todo item to update
            title (str, optional): New title for the todo item. Defaults to None.
            description (str, optional): New description for the todo item. Defaults to None.
            
        Returns:
            TodoItem: The updated TodoItem
            
        Raises:
            TodoNotFoundException: If no item exists with the specified ID
        """
        if item_id not in self.items:
            raise TodoNotFoundException(f"Todo item with ID {item_id} not found")
        
        item = self.items[item_id]
        
        # Update the item's attributes if new values are provided
        if title is not None:
            item.title = title
        if description is not None:
            item.description = description
        
        self._save_data()
        return item
    
    def delete_item(self, item_id):
        """
        Delete a todo item by its ID.
        
        Args:
            item_id (int): ID of the todo item to delete
            
        Raises:
            TodoNotFoundException: If no item exists with the specified ID
        """
        if item_id not in self.items:
            raise TodoNotFoundException(f"Todo item with ID {item_id} not found")
        
        del self.items[item_id]
        self._save_data()
    
    def mark_complete(self, item_id):
        """
        Mark a todo item as complete.
        
        Args:
            item_id (int): ID of the todo item to mark complete
            
        Returns:
            TodoItem: The updated TodoItem marked as complete
            
        Raises:
            TodoNotFoundException: If no item exists with the specified ID
        """
        if item_id not in self.items:
            raise TodoNotFoundException(f"Todo item with ID {item_id} not found")
        
        item = self.items[item_id]
        item.completed = True
        self._save_data()
        return item
    
    def mark_incomplete(self, item_id):
        """
        Mark a todo item as incomplete.
        
        Args:
            item_id (int): ID of the todo item to mark incomplete
            
        Returns:
            TodoItem: The updated TodoItem marked as incomplete
            
        Raises:
            TodoNotFoundException: If no item exists with the specified ID
        """
        if item_id not in self.items:
            raise TodoNotFoundException(f"Todo item with ID {item_id} not found")
        
        item = self.items[item_id]
        item.completed = False
        self._save_data()
        return item
    
    def _save_data(self):
        """Save todos to JSON file."""
        data = {
            "next_id": self.next_id,
            "items": {str(k): v.to_dict() for k, v in self.items.items()}
        }
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    
    def _load_data(self):
        """Load todos from JSON file if it exists."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.next_id = data.get("next_id", 1)
                    for item_id, item_data in data.get("items", {}).items():
                        self.items[int(item_id)] = TodoItem(
                            id=int(item_id),
                            title=item_data["title"],
                            description=item_data.get("description", ""),
                            completed=item_data.get("completed", False)
                        )
            except (json.JSONDecodeError, KeyError):
                # If file is corrupted, start fresh
                self.items = {}
                self.next_id = 1