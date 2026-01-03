"""
Backup command handler for the Todo CLI application.
Implements the backup functionality for tasks.
"""

from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from services.task_service import TaskService

def backup_tasks_handler(task_service: 'TaskService', backup_name: str = None):
    """
    Handle the backup command to create a backup of tasks.
    
    Args:
        task_service: The TaskService instance to backup tasks from
        backup_name: Optional name for the backup (uses timestamp if not provided)
    """
    try:
        # Use the storage manager to create a backup
        storage_manager = task_service._storage_manager
        backup_path = storage_manager.create_backup(backup_name)
        
        print(f"Backup created successfully: {backup_path}")
        
    except Exception as e:
        print(f"Error creating backup: {str(e)}")