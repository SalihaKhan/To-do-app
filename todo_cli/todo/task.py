"""
Task model for the Todo CLI skill.
Represents a single task with id, title, description, and completion status.
"""

class Task:
    """
    Represents a single todo task.
    
    Attributes:
        id (int): Sequential identifier for the task
        title (str): Title of the task
        description (str): Detailed description of the task
        completed (bool): Completion status of the task
    """
    
    def __init__(self, task_id: int, title: str, description: str, completed: bool = False):
        """
        Initialize a new Task instance.
        
        Args:
            task_id (int): Sequential identifier for the task
            title (str): Title of the task
            description (str): Detailed description of the task
            completed (bool): Completion status of the task (default: False)
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
    
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
        Convert the task to a dictionary representation.
        
        Returns:
            dict: Dictionary containing task attributes
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }