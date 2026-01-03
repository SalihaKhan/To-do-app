"""
CLI parser for the Todo CLI application.
Handles parsing and routing of CLI commands including new persistence commands.
"""

from typing import TYPE_CHECKING, List, Optional
import sys
import os

# Add the src directory to the path so we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if TYPE_CHECKING:
    from services.task_service import TaskService

def parse_and_execute_command(task_service: 'TaskService', user_input: str) -> bool:
    """
    Parse user input and execute the appropriate command.
    
    Args:
        task_service: The TaskService instance to operate on
        user_input: The raw user input string
        
    Returns:
        bool: True if the command was recognized and executed, False otherwise
    """
    # Split the input into command and arguments
    parts = user_input.strip().split(' ', 1)
    command = parts[0].lower()
    
    # Handle the command based on its name
    if command == 'save':
        # Extract file path if provided
        file_path = parts[1] if len(parts) > 1 else None
        from commands.save import save_tasks_handler
        save_tasks_handler(task_service, file_path)
        return True
    
    elif command == 'load':
        # Extract file path if provided
        file_path = parts[1] if len(parts) > 1 else None
        from commands.load import load_tasks_handler
        load_tasks_handler(task_service, file_path)
        return True
    
    elif command == 'backup':
        # Extract backup name if provided
        backup_name = parts[1] if len(parts) > 1 else None
        from commands.backup import backup_tasks_handler
        backup_tasks_handler(task_service, backup_name)
        return True
    
    elif command == 'restore':
        # Extract backup path - this is required
        if len(parts) < 2:
            print("Error: Restore command requires a backup path")
            return True  # Command was recognized but had an error
        
        backup_path = parts[1]
        from commands.restore import restore_tasks_handler
        restore_tasks_handler(task_service, backup_path)
        return True
    
    elif command == 'list-backups' or command == 'list_backups':
        from commands.list_backups import list_backups_handler
        list_backups_handler(task_service)
        return True
    
    # Command not recognized by the persistence module
    return False