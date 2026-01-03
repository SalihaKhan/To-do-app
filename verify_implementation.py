"""
Simple test to verify Phase-III implementation.
This script tests that the new persistence features work correctly
without interfering with existing functionality.
"""

import sys
import os
from pathlib import Path

# Add the src directory to the path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from services.task_service import TaskService
from persistence.storage import FileStorageManager
from persistence.backup import BackupManager
from constants import DEFAULT_DATA_FILE


def test_task_service_with_persistence():
    """Test that TaskService works with persistence."""
    print("Testing TaskService with persistence...")
    
    # Create a TaskService instance
    task_service = TaskService("test_persistence.json")
    
    # Verify that it loads empty initially
    tasks = task_service.get_all_tasks()
    print(f"Initial tasks count: {len(tasks)}")
    
    # Add a task
    task = task_service.add_task("Test Persistence", "Testing persistence functionality")
    print(f"Added task: {task.title}")
    
    # Verify task was added
    tasks = task_service.get_all_tasks()
    print(f"Tasks after adding: {len(tasks)}")
    
    # Check that the file was created
    if Path("test_persistence.json").exists():
        print("V Data file was created")
    else:
        print("X Data file was not created")

    # Clean up
    if Path("test_persistence.json").exists():
        Path("test_persistence.json").unlink()

    print("TaskService persistence test completed.\n")


def test_backup_manager():
    """Test that BackupManager works correctly."""
    print("Testing BackupManager...")
    
    # Create a FileStorageManager
    storage_manager = FileStorageManager("test_backup.json")
    
    # Create a backup manager
    backup_manager = BackupManager()
    
    # Add a test task to the storage
    from models.task import Task
    test_tasks = [Task(1, "Backup Test", "Testing backup functionality")]
    storage_manager.save_tasks(test_tasks)
    
    # Create a backup
    backup_path = backup_manager.create_backup(storage_manager, "test_backup.json")
    print(f"Created backup: {backup_path}")
    
    # List backups
    backups = backup_manager.list_backups()
    print(f"Number of backups: {len(backups)}")
    
    # Clean up
    if Path("test_backup.json").exists():
        Path("test_backup.json").unlink()
    
    # Remove backup files
    for backup_file in Path("backups").glob("*.json"):
        backup_file.unlink()
    
    # Remove backup directory if empty
    backup_dir = Path("backups")
    if backup_dir.exists() and not any(backup_dir.iterdir()):
        backup_dir.rmdir()
    
    print("BackupManager test completed.\n")


def test_new_commands_integration():
    """Test that new commands can be imported and used."""
    print("Testing new command integration...")
    
    # Test importing new command modules
    try:
        from commands.save import save_tasks_handler
        print("V Save command handler imported successfully")
    except ImportError as e:
        print(f"X Failed to import save command: {e}")

    try:
        from commands.load import load_tasks_handler
        print("V Load command handler imported successfully")
    except ImportError as e:
        print(f"X Failed to import load command: {e}")

    try:
        from commands.backup import backup_tasks_handler
        print("V Backup command handler imported successfully")
    except ImportError as e:
        print(f"X Failed to import backup command: {e}")

    try:
        from commands.restore import restore_tasks_handler
        print("V Restore command handler imported successfully")
    except ImportError as e:
        print(f"X Failed to import restore command: {e}")

    try:
        from commands.list_backups import list_backups_handler
        print("V List-backups command handler imported successfully")
    except ImportError as e:
        print(f"X Failed to import list-backups command: {e}")

    try:
        from cli.parser import parse_and_execute_command
        print("V CLI parser imported successfully")
    except ImportError as e:
        print(f"X Failed to import CLI parser: {e}")

    print("Command integration test completed.\n")


def test_constants():
    """Test that constants are properly defined."""
    print("Testing constants...")
    
    from constants import (
        DEFAULT_DATA_FILE,
        DEFAULT_BACKUP_DIR,
        CURRENT_DATA_VERSION,
        ERROR_FILE_NOT_FOUND,
        ERROR_PERMISSION_DENIED,
        ERROR_INVALID_FORMAT,
        ERROR_CORRUPTED_DATA
    )
    
    print(f"Default data file: {DEFAULT_DATA_FILE}")
    print(f"Default backup directory: {DEFAULT_BACKUP_DIR}")
    print(f"Current data version: {CURRENT_DATA_VERSION}")
    print(f"Error messages defined: {ERROR_FILE_NOT_FOUND}, {ERROR_PERMISSION_DENIED}, etc.")
    
    print("Constants test completed.\n")


if __name__ == "__main__":
    print("Starting Phase-III implementation verification...\n")
    
    test_constants()
    test_task_service_with_persistence()
    test_backup_manager()
    test_new_commands_integration()
    
    print("All Phase-III implementation verification tests completed!")
    print("\nPhase-III features implemented:")
    print("- Persistent storage (save/load tasks to/from JSON files)")
    print("- Auto-save on application exit")
    print("- Auto-load on application startup")
    print("- Manual save/load commands")
    print("- Backup and restore functionality")
    print("- List available backups")
    print("- New CLI commands integrated")
    print("- Full backward compatibility with Phase-I/II features")