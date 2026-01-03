"""
File storage manager for the Todo CLI application.
Handles saving and loading task data to/from disk.
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging

from src.models.task import Task
from src.constants import (
    DEFAULT_DATA_FILE, 
    DATA_FILE_ENCODING, 
    CURRENT_DATA_VERSION,
    ERROR_FILE_NOT_FOUND,
    ERROR_PERMISSION_DENIED,
    ERROR_INVALID_FORMAT,
    ERROR_CORRUPTED_DATA
)


def save_tasks_to_file(tasks: List[Task], file_path: str = DEFAULT_DATA_FILE) -> bool:
    """
    Save tasks to a JSON file.
    
    Args:
        tasks: List of Task objects to save
        file_path: Path to save the tasks to (default: DEFAULT_DATA_FILE)
        
    Returns:
        bool: True if save was successful, False otherwise
    """
    target_path = Path(file_path)
    
    try:
        # Prepare data with metadata
        data_to_save = {
            "version": CURRENT_DATA_VERSION,
            "saved_at": datetime.now().isoformat(),
            "task_count": len(tasks),
            "tasks": [task.to_dict() for task in tasks]
        }
        
        # Write to file
        with open(target_path, 'w', encoding=DATA_FILE_ENCODING) as file:
            json.dump(data_to_save, file, indent=2, ensure_ascii=False)
        
        logging.getLogger(__name__).info(f"Successfully saved {len(tasks)} tasks to {target_path}")
        return True
        
    except PermissionError:
        logging.getLogger(__name__).error(f"Permission denied when saving to {target_path}")
        raise Exception(ERROR_PERMISSION_DENIED)
    except OSError as e:
        logging.getLogger(__name__).error(f"OS error when saving to {target_path}: {e}")
        raise Exception(f"OS error: {str(e)}")
    except Exception as e:
        logging.getLogger(__name__).error(f"Unexpected error when saving to {target_path}: {e}")
        raise Exception(f"Save failed: {str(e)}")


def load_tasks_from_file(file_path: str = DEFAULT_DATA_FILE) -> List[Task]:
    """
    Load tasks from a JSON file.
    
    Args:
        file_path: Path to load the tasks from (default: DEFAULT_DATA_FILE)
        
    Returns:
        List[Task]: List of Task objects loaded from the file
    """
    target_path = Path(file_path)
    
    if not target_path.exists():
        logging.getLogger(__name__).info(f"Data file {target_path} does not exist, returning empty task list")
        return []
    
    try:
        with open(target_path, 'r', encoding=DATA_FILE_ENCODING) as file:
            data = json.load(file)
        
        # Validate data structure
        if not isinstance(data, dict):
            raise Exception(ERROR_INVALID_FORMAT)
        
        if "tasks" not in data:
            raise Exception(ERROR_INVALID_FORMAT)
        
        # Load tasks from the data
        task_dicts = data["tasks"]
        tasks = []
        
        for task_dict in task_dicts:
            try:
                task = Task.from_dict(task_dict)
                tasks.append(task)
            except Exception as e:
                logging.getLogger(__name__).warning(f"Failed to load task from dict {task_dict}: {e}")
                # Continue loading other tasks even if one fails
        
        logging.getLogger(__name__).info(f"Successfully loaded {len(tasks)} tasks from {target_path}")
        return tasks
        
    except json.JSONDecodeError as e:
        logging.getLogger(__name__).error(f"Invalid JSON in file {target_path}: {e}")
        raise Exception(ERROR_INVALID_FORMAT)
    except PermissionError:
        logging.getLogger(__name__).error(f"Permission denied when loading from {target_path}")
        raise Exception(ERROR_PERMISSION_DENIED)
    except OSError as e:
        logging.getLogger(__name__).error(f"OS error when loading from {target_path}: {e}")
        raise Exception(f"OS error: {str(e)}")
    except Exception as e:
        logging.getLogger(__name__).error(f"Unexpected error when loading from {target_path}: {e}")
        raise Exception(f"Load failed: {str(e)}")


class FileStorageManager:
    """
    Manages file-based storage for tasks, including saving, loading, and backup operations.
    """
    
    def __init__(self, data_file_path: str = DEFAULT_DATA_FILE):
        """
        Initialize the FileStorageManager.
        
        Args:
            data_file_path: Path to the main data file
        """
        self.data_file_path = Path(data_file_path)
        self.backup_dir = self.data_file_path.parent / "backups"
        
        # Create backup directory if it doesn't exist
        self.backup_dir.mkdir(exist_ok=True)
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
    
    def save_tasks(self, tasks: List[Task], file_path: Optional[str] = None) -> bool:
        """
        Save tasks to a JSON file.
        
        Args:
            tasks: List of Task objects to save
            file_path: Optional file path to save to (uses default if not provided)
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        target_path = Path(file_path) if file_path else self.data_file_path
        
        try:
            # Prepare data with metadata
            data_to_save = {
                "version": CURRENT_DATA_VERSION,
                "saved_at": datetime.now().isoformat(),
                "task_count": len(tasks),
                "tasks": [task.to_dict() for task in tasks]
            }
            
            # Write to file
            with open(target_path, 'w', encoding=DATA_FILE_ENCODING) as file:
                json.dump(data_to_save, file, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Successfully saved {len(tasks)} tasks to {target_path}")
            return True
            
        except PermissionError:
            self.logger.error(f"Permission denied when saving to {target_path}")
            raise Exception(ERROR_PERMISSION_DENIED)
        except OSError as e:
            self.logger.error(f"OS error when saving to {target_path}: {e}")
            raise Exception(f"OS error: {str(e)}")
        except Exception as e:
            self.logger.error(f"Unexpected error when saving to {target_path}: {e}")
            raise Exception(f"Save failed: {str(e)}")
    
    def load_tasks(self, file_path: Optional[str] = None) -> List[Task]:
        """
        Load tasks from a JSON file.
        
        Args:
            file_path: Optional file path to load from (uses default if not provided)
            
        Returns:
            List[Task]: List of Task objects loaded from the file
        """
        target_path = Path(file_path) if file_path else self.data_file_path
        
        if not target_path.exists():
            self.logger.info(f"Data file {target_path} does not exist, returning empty task list")
            return []
        
        try:
            with open(target_path, 'r', encoding=DATA_FILE_ENCODING) as file:
                data = json.load(file)
            
            # Validate data structure
            if not isinstance(data, dict):
                raise Exception(ERROR_INVALID_FORMAT)
            
            if "tasks" not in data:
                raise Exception(ERROR_INVALID_FORMAT)
            
            # Load tasks from the data
            task_dicts = data["tasks"]
            tasks = []
            
            for task_dict in task_dicts:
                try:
                    task = Task.from_dict(task_dict)
                    tasks.append(task)
                except Exception as e:
                    self.logger.warning(f"Failed to load task from dict {task_dict}: {e}")
                    # Continue loading other tasks even if one fails
            
            self.logger.info(f"Successfully loaded {len(tasks)} tasks from {target_path}")
            return tasks
            
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in file {target_path}: {e}")
            raise Exception(ERROR_INVALID_FORMAT)
        except PermissionError:
            self.logger.error(f"Permission denied when loading from {target_path}")
            raise Exception(ERROR_PERMISSION_DENIED)
        except OSError as e:
            self.logger.error(f"OS error when loading from {target_path}: {e}")
            raise Exception(f"OS error: {str(e)}")
        except Exception as e:
            self.logger.error(f"Unexpected error when loading from {target_path}: {e}")
            raise Exception(f"Load failed: {str(e)}")
    
    def create_backup(self, backup_name: Optional[str] = None) -> str:
        """
        Create a backup of the current tasks.
        
        Args:
            backup_name: Optional name for the backup file (uses timestamp if not provided)
            
        Returns:
            str: Path to the created backup file
        """
        # Generate backup name if not provided
        if not backup_name:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"tasks_backup_{timestamp}.json"
        
        backup_path = self.backup_dir / backup_name
        
        # Load current tasks and save to backup location
        current_tasks = self.load_tasks()
        self.save_tasks(current_tasks, str(backup_path))
        
        self.logger.info(f"Created backup: {backup_path}")
        return str(backup_path)
    
    def list_backups(self) -> List[Dict[str, Any]]:
        """
        List all available backup files.
        
        Returns:
            List[Dict[str, Any]]: List of backup file information
        """
        backups = []
        
        for backup_file in self.backup_dir.glob("*.json"):
            stat = backup_file.stat()
            backups.append({
                "name": backup_file.name,
                "path": str(backup_file),
                "size": stat.st_size,
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "created": datetime.fromtimestamp(stat.st_ctime).isoformat()
            })
        
        # Sort by modification time (newest first)
        backups.sort(key=lambda x: x["modified"], reverse=True)
        return backups
    
    def restore_from_backup(self, backup_path: str) -> bool:
        """
        Restore tasks from a backup file.
        
        Args:
            backup_path: Path to the backup file to restore from
            
        Returns:
            bool: True if restore was successful, False otherwise
        """
        backup_file = Path(backup_path)
        
        if not backup_file.exists():
            raise FileNotFoundError(f"Backup file does not exist: {backup_path}")
        
        # Load tasks from backup
        backup_tasks = self.load_tasks(str(backup_file))
        
        # Save to main data file
        success = self.save_tasks(backup_tasks)
        
        if success:
            self.logger.info(f"Successfully restored {len(backup_tasks)} tasks from backup: {backup_path}")
        
        return success