"""
Helper functions for the Todo CLI application.
Provides utility functions for the CLI interface.
"""


def display_menu():
    """
    Display the main menu options.
    """
    print("\n" + "="*40)
    print("         TODO CLI APPLICATION")
    print("="*40)
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("6. Exit")
    print("="*40)
    print("Additional commands: save, load, backup, restore, list-backups, help")
    print("Type 'help' for more information on commands")
    print("="*40)


def get_user_input(prompt: str) -> str:
    """
    Get input from the user with a prompt.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        str: The user's input
    """
    return input(prompt).strip()


def validate_task_id(task_id_str: str) -> int:
    """
    Validate and convert a task ID string to an integer.
    
    Args:
        task_id_str (str): String representation of a task ID
        
    Returns:
        int: The validated task ID
    """
    try:
        task_id = int(task_id_str)
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        return task_id
    except ValueError:
        raise ValueError("Task ID must be a valid integer")