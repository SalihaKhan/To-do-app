"""
Load command handler for the Todo CLI application.
Implements the manual load functionality for tasks.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.task_service import TaskService

def load_tasks_handler(task_service: 'TaskService', file_path: str = None):
    """
    Handle the load command to manually load tasks from a file.
    
    Args:
        task_service: The TaskService instance to load tasks into
        file_path: Optional file path to load from (uses default if not provided)
    """
    try:
        if file_path:
            # If a specific file path is provided, load from that location
            from persistence.storage import FileStorageManager
            storage_manager = FileStorageManager(file_path)
            loaded_tasks = storage_manager.load_tasks()
            
            # Update the task service with loaded tasks
            task_service._tasks = loaded_tasks
            
            # Update the next ID based on loaded tasks
            if loaded_tasks:
                task_service._next_id = max(task.id for task in loaded_tasks) + 1
            else:
                task_service._next_id = 1
        else:
            # Otherwise, use the default load method
            task_service.load_tasks()
        
        task_count = len(task_service.get_all_tasks())
        file_path = file_path or task_service._data_file
        print(f"Successfully loaded {task_count} tasks from {file_path}")
        
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error loading tasks: {str(e)}")