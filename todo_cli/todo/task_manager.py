"""
TaskManager for the Todo CLI skill.
Handles in-memory storage and CRUD operations for tasks.
"""

from .task import Task
from typing import List, Optional


class TaskManager:
    """
    Manages a collection of Task objects in memory.
    
    Provides methods for adding, listing, updating, deleting, and marking tasks as complete/incomplete.
    """
    
    def __init__(self):
        """
        Initialize a new TaskManager instance.
        """
        self.tasks: List[Task] = []
        self._next_id = 1
    
    def add_task(self, title: str, description: str) -> Task:
        """
        Add a new task to the manager.
        
        Args:
            title (str): Title of the task
            description (str): Description of the task
            
        Returns:
            Task: The newly created task
        """
        task = Task(self._next_id, title, description, False)
        self.tasks.append(task)
        self._next_id += 1
        return task
    
    def list_tasks(self) -> List[Task]:
        """
        List all tasks.
        
        Returns:
            List[Task]: A list of all tasks
        """
        return self.tasks.copy()
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by ID.
        
        Args:
            task_id (int): ID of the task to retrieve
            
        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Update an existing task.
        
        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            
        Returns:
            bool: True if the task was updated, False if not found
        """
        task = self.get_task(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.
        
        Args:
            task_id (int): ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False if not found
        """
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
    
    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.
        
        Args:
            task_id (int): ID of the task to mark as complete
            
        Returns:
            bool: True if the task was marked complete, False if not found
        """
        task = self.get_task(task_id)
        if task:
            task.completed = True
            return True
        return False
    
    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.
        
        Args:
            task_id (int): ID of the task to mark as incomplete
            
        Returns:
            bool: True if the task was marked incomplete, False if not found
        """
        task = self.get_task(task_id)
        if task:
            task.completed = False
            return True
        return False
    
    def get_next_id(self) -> int:
        """
        Get the next available task ID.
        
        Returns:
            int: The next available ID
        """
        return self._next_id