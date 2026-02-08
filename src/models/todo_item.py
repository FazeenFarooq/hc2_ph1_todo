"""
TodoItem data model representing a single todo item.
"""

class TodoItem:
    """
    Represents a single todo item with the following attributes:
    - id (int): Unique identifier for the todo item, auto-generated
    - title (str): Title of the todo item, required
    - description (str): Detailed description of the todo item, optional (can be empty)
    - completed (bool): Completion status of the todo item, default: False
    """
    
    def __init__(self, id, title, description="", completed=False):
        """
        Initialize a TodoItem instance.
        
        Args:
            id (int): Unique identifier for the todo item
            title (str): Title of the todo item
            description (str, optional): Detailed description of the todo item. Defaults to "".
            completed (bool, optional): Completion status of the todo item. Defaults to False.
        
        Raises:
            ValueError: If title is empty or None
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or None")
        
        self.id = id
        self.title = title.strip()
        self.description = description or ""
        self.completed = completed
    
    def __repr__(self):
        """String representation of the TodoItem."""
        return f"TodoItem(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"
    
    def __eq__(self, other):
        """Check equality with another TodoItem."""
        if not isinstance(other, TodoItem):
            return False
        return (self.id == other.id and 
                self.title == other.title and 
                self.description == other.description and 
                self.completed == other.completed)
    
    def to_dict(self):
        """Convert the TodoItem to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a TodoItem from a dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )