"""
List-backups command handler for the Todo CLI application.
Implements the functionality to list available backups.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.task_service import TaskService

def list_backups_handler(task_service: 'TaskService'):
    """
    Handle the list-backups command to display available backups.
    
    Args:
        task_service: The TaskService instance to get backup information from
    """
    try:
        # Use the storage manager to list backups
        storage_manager = task_service._storage_manager
        backups = storage_manager.list_backups()
        
        if not backups:
            print("No backups found.")
            return
        
        print(f"Found {len(backups)} backup(s):")
        print("-" * 80)
        print(f"{'Name':<30} {'Size':<10} {'Modified':<20}")
        print("-" * 80)
        
        for backup in backups:
            name = backup['name'][:27] + "..." if len(backup['name']) > 30 else backup['name']
            size = f"{backup['size']} bytes"
            modified = backup['modified'][:19]  # Only show date and time part
            print(f"{name:<30} {size:<10} {modified:<20}")
        
        print("-" * 80)
        
    except Exception as e:
        print(f"Error listing backups: {str(e)}")