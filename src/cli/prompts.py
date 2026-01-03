"""
CLI prompts for the Todo CLI application.
Provides functions for user prompts and confirmations.
"""

def confirm_action(prompt: str = "Are you sure you want to proceed?") -> bool:
    """
    Prompt the user for confirmation before performing a destructive action.
    
    Args:
        prompt: The confirmation prompt to display
        
    Returns:
        bool: True if user confirms, False otherwise
    """
    response = input(f"{prompt} (y/N): ").strip().lower()
    return response in ['y', 'yes', '1', 'true', 'ok']


def get_user_input_with_default(prompt: str, default_value: str) -> str:
    """
    Get user input with a default value.
    
    Args:
        prompt: The prompt to display to the user
        default_value: The default value to use if user presses Enter
        
    Returns:
        str: The user input or default value
    """
    user_input = input(f"{prompt} (default: {default_value}): ").strip()
    return user_input if user_input else default_value


def prompt_for_file_path(action: str = "save") -> str:
    """
    Prompt the user for a file path.
    
    Args:
        action: The action being performed (save/load/backup/restore)
        
    Returns:
        str: The file path provided by the user
    """
    if action == "save":
        prompt = "Enter file path to save tasks to (or press Enter for default): "
    elif action == "load":
        prompt = "Enter file path to load tasks from: "
    elif action == "restore":
        prompt = "Enter backup file path to restore from: "
    else:  # backup
        prompt = "Enter backup name (or press Enter for timestamp): "
    
    return input(prompt).strip()