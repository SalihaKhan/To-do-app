"""
Help command handler for the Todo CLI application.
Implements the help functionality including new persistence commands.
"""

def display_help():
    """
    Display help information for all available commands.
    """
    print("\n--- Help Information ---")
    print("Available commands:")
    print("  1. Add Task - Add a new task to the list")
    print("  2. List Tasks - Display all tasks")
    print("  3. Update Task - Modify an existing task")
    print("  4. Delete Task - Remove a task from the list")
    print("  5. Mark Task Status - Change task completion status")
    print("  6. Exit - Save and exit the application")
    print("")
    print("Additional persistence commands (type these at the main menu):")
    print("  save [filepath] - Manually save tasks to a file")
    print("  load [filepath] - Load tasks from a file")
    print("  backup [name] - Create a backup of current tasks")
    print("  restore <backup_path> - Restore tasks from a backup")
    print("  list-backups - List all available backups")
    print("  help - Show this help information")
    print("")
    print("Examples:")
    print("  save my_tasks.json")
    print("  backup my_backup")
    print("  restore backups/tasks_backup_20231201_120000.json")
    print("------------------------\n")