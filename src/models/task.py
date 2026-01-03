"""
Task model for the Todo CLI application.
Implements the Task entity as specified in the requirements.
"""

from datetime import datetime
from typing import Dict, Any, Optional


class Task:
    """
    Represents a single todo task with id, title, description, and completion status.

    Attributes:
        id (int): Sequential identifier for the task
        title (str): Title of the task
        description (str): Detailed description of the task
        completed (bool): Completion status of the task
        created_at (datetime): Timestamp when the task was created
        updated_at (datetime): Timestamp when the task was last updated
    """

    def __init__(self, task_id: int, title: str, description: str, completed: bool = False,
                 created_at: Optional[datetime] = None, updated_at: Optional[datetime] = None):
        """
        Initialize a new Task instance.

        Args:
            task_id (int): Sequential identifier for the task
            title (str): Title of the task
            description (str): Detailed description of the task
            completed (bool): Completion status of the task (default: False)
            created_at (datetime): Timestamp when the task was created (default: current time)
            updated_at (datetime): Timestamp when the task was last updated (default: current time)
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def __str__(self):
        """
        String representation of the task.

        Returns:
            str: Formatted string showing task details
        """
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}. {self.title} - {self.description}"

    def __repr__(self):
        """
        Developer-friendly representation of the task.

        Returns:
            str: Detailed representation of the task object
        """
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"

    def to_dict(self):
        """
        Convert the task to a dictionary representation for serialization.

        Returns:
            dict: Dictionary containing task attributes
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """
        Create a Task instance from a dictionary representation.

        Args:
            data: Dictionary containing task attributes

        Returns:
            Task: New Task instance created from the data
        """
        from datetime import datetime

        # Handle backward compatibility - if timestamps don't exist, create them
        created_at_str = data.get('created_at')
        updated_at_str = data.get('updated_at')

        created_at = datetime.fromisoformat(created_at_str) if created_at_str else datetime.now()
        updated_at = datetime.fromisoformat(updated_at_str) if updated_at_str else datetime.now()

        return cls(
            task_id=data['id'],
            title=data['title'],
            description=data.get('description', ''),
            completed=data.get('completed', False),
            created_at=created_at,
            updated_at=updated_at
        )