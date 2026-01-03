"""
Test implementation for Phase-III persistence features.
This file tests the basic functionality of the persistence features.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

# Add the src directory to the path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from services.task_service import TaskService
from models.task import Task
from persistence.storage import FileStorageManager, save_tasks_to_file, load_tasks_from_file
from persistence.backup import BackupManager


def test_basic_persistence():
    """Test basic persistence functionality."""
    print("Testing basic persistence functionality...")
    
    # Create a task service
    test_file = "test_tasks.json"
    task_service = TaskService(test_file)
    
    # Add a test task
    task = task_service.add_task("Test Task", "This is a test task")
    print(f"Added task: {task.title} with ID {task.id}")
    
    # Verify the task was added
    tasks = task_service.get_all_tasks()
    print(f"Total tasks: {len(tasks)}")
    
    # Check if the task was saved to file
    if os.path.exists(test_file):
        print(f"Data file created: {test_file}")
        
        # Load tasks from the file directly to verify
        loaded_tasks = load_tasks_from_file(test_file)
        print(f"Loaded tasks from file: {len(loaded_tasks)}")
        
        if loaded_tasks:
            print(f"First loaded task: {loaded_tasks[0].title}")
    else:
        print("ERROR: Data file was not created!")
    
    # Clean up test file
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"Cleaned up test file: {test_file}")
    
    print("Basic persistence test completed.\n")


def test_backup_functionality():
    """Test backup functionality."""
    print("Testing backup functionality...")
    
    # Create a task service
    test_file = "test_tasks_backup.json"
    task_service = TaskService(test_file)
    
    # Add some test tasks
    task_service.add_task("Backup Test 1", "First backup test task")
    task_service.add_task("Backup Test 2", "Second backup test task")
    
    print(f"Added {len(task_service.get_all_tasks())} tasks")
    
    # Create a backup
    backup_path = task_service._storage_manager.create_backup("test_backup.json")
    print(f"Created backup: {backup_path}")
    
    # List backups
    backups = task_service._storage_manager.list_backups()
    print(f"Available backups: {len(backups)}")
    
    # Restore from backup
    if backups:
        # Add another task to change the state
        task_service.add_task("After Backup Task", "Task added after backup")
        print(f"Tasks after adding new task: {len(task_service.get_all_tasks())}")
        
        # Restore from the backup
        task_service._storage_manager.restore_from_backup(backup_path)
        print(f"Tasks after restore: {len(task_service.get_all_tasks())}")
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)
    if os.path.exists(backup_path):
        os.remove(backup_path)
    
    # Remove backup directory if empty
    backup_dir = Path("backups")
    if backup_dir.exists() and not any(backup_dir.iterdir()):
        backup_dir.rmdir()
    
    print("Backup functionality test completed.\n")


def test_task_model_extensions():
    """Test the extended Task model with timestamps."""
    print("Testing extended Task model...")
    
    # Create a task with timestamps
    task = Task(1, "Timestamp Test", "Testing timestamp functionality")
    print(f"Task created at: {task.created_at}")
    print(f"Task updated at: {task.updated_at}")
    
    # Convert to dict and back
    task_dict = task.to_dict()
    print(f"Task as dict: {task_dict}")
    
    # Create from dict
    restored_task = Task.from_dict(task_dict)
    print(f"Restored task: {restored_task.title}")
    print(f"Restored task created at: {restored_task.created_at}")
    
    print("Task model extension test completed.\n")


if __name__ == "__main__":
    print("Starting Phase-III implementation tests...\n")
    
    test_task_model_extensions()
    test_basic_persistence()
    test_backup_functionality()
    
    print("All tests completed!")