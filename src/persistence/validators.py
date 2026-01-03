"""
Validation utilities for the Todo CLI application.
Provides validation functions for file paths and other inputs related to persistence.
"""

import os
from pathlib import Path
from typing import Union


def validate_file_path(file_path: str) -> bool:
    """
    Validate that a file path is safe and accessible.
    
    Args:
        file_path: Path to validate
        
    Returns:
        bool: True if path is valid, raises ValueError otherwise
    """
    if not file_path:
        raise ValueError("File path cannot be empty")
    
    # Check for path traversal attempts
    if ".." in file_path or "~" in file_path:
        raise ValueError("Path traversal not allowed")
    
    path_obj = Path(file_path)
    
    # Check if the directory exists
    if not path_obj.parent.exists():
        raise ValueError(f"Directory does not exist: {path_obj.parent}")
    
    # Check if it's a file (not a directory)
    if path_obj.is_dir():
        raise ValueError("Path points to a directory, not a file")
    
    return True


def validate_backup_path(backup_path: str) -> bool:
    """
    Validate that a backup path is safe and accessible.
    
    Args:
        backup_path: Backup path to validate
        
    Returns:
        bool: True if path is valid, raises ValueError otherwise
    """
    return validate_file_path(backup_path)


def validate_data_integrity(tasks: list) -> bool:
    """
    Validate the integrity of task data.
    
    Args:
        tasks: List of tasks to validate
        
    Returns:
        bool: True if data integrity is valid, False otherwise
    """
    if not isinstance(tasks, list):
        return False
    
    for task in tasks:
        # Check if task has required attributes
        if not hasattr(task, 'id') or not hasattr(task, 'title') or not hasattr(task, 'completed'):
            return False
        
        # Check if task id is a positive integer
        if not isinstance(task.id, int) or task.id <= 0:
            return False
        
        # Check if title is a string
        if not isinstance(task.title, str):
            return False
    
    return True