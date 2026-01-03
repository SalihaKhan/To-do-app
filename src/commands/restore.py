"""
Restore command handler for the Todo CLI application.
Implements the restore functionality for tasks from backup.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.task_service import TaskService

def restore_tasks_handler(task_service: 'TaskService', backup_path: str):
    """
    Handle the restore command to restore tasks from a backup.
    
    Args:
        task_service: The TaskService instance to restore tasks into
        backup_path: Path to the backup file to restore from
    """
    try:
        # Use the storage manager to restore from backup
        storage_manager = task_service._storage_manager
        success = storage_manager.restore_from_backup(backup_path)
        
        if success:
            # Reload tasks into the service
            task_service.load_tasks()
            task_count = len(task_service.get_all_tasks())
            print(f"Successfully restored {task_count} tasks from {backup_path}")
        else:
            print(f"Failed to restore from {backup_path}")
        
    except FileNotFoundError:
        print(f"Error: Backup file not found - {backup_path}")
    except Exception as e:
        print(f"Error restoring from backup: {str(e)}")