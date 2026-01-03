"""
Save command handler for the Todo CLI application.
Implements the manual save functionality for tasks.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.task_service import TaskService

def save_tasks_handler(task_service: 'TaskService', file_path: str = None):
    """
    Handle the save command to manually save tasks to a file.
    
    Args:
        task_service: The TaskService instance to save tasks from
        file_path: Optional file path to save to (uses default if not provided)
    """
    try:
        if file_path:
            # If a specific file path is provided, save to that location
            from persistence.storage import FileStorageManager
            storage_manager = FileStorageManager(file_path)
            tasks = task_service.get_all_tasks()
            success = storage_manager.save_tasks(tasks)
        else:
            # Otherwise, use the default save method
            task_service.save_tasks()
            success = True
        
        if success:
            task_count = len(task_service.get_all_tasks())
            file_path = file_path or task_service._data_file
            print(f"Successfully saved {task_count} tasks to {file_path}")
        else:
            print("Failed to save tasks")
            
    except Exception as e:
        print(f"Error saving tasks: {str(e)}")