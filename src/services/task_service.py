"""
Task service for the Todo CLI application.
Implements CRUD operations for tasks with in-memory storage.
"""

from typing import List, Optional
from models.task import Task


class TaskService:
    """
    Service class for managing tasks in memory.
    
    Provides methods for adding, listing, updating, deleting, and marking tasks as complete/incomplete.
    """
    
    def __init__(self):
        """
        Initialize a new TaskService instance.
        """
        self._tasks: List[Task] = []
        self._next_id = 1
    
    def add_task(self, title: str, description: str) -> Task:
        """
        Add a new task to the service.
        
        Args:
            title (str): Title of the task
            description (str): Description of the task
            
        Returns:
            Task: The newly created task
        """
        task = Task(self._next_id, title, description, False)
        self._tasks.append(task)
        self._next_id += 1
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            List[Task]: A list of all tasks
        """
        return self._tasks.copy()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by ID.
        
        Args:
            task_id (int): ID of the task to retrieve
            
        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self._tasks:
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
        task = self.get_task_by_id(task_id)
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
        task = self.get_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
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
        task = self.get_task_by_id(task_id)
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
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False