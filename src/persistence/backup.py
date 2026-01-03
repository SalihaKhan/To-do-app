"""
Backup manager for the Todo CLI application.
Handles creating, listing, and managing task backups.
"""

import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional
import json

from src.constants import DEFAULT_BACKUP_DIR, BACKUP_RETENTION_DAYS, MAX_BACKUP_FILES
from src.persistence.storage import FileStorageManager


class BackupManager:
    """
    Manages backup operations for task data, including creation, listing, 
    restoration, and retention policies.
    """
    
    def __init__(self, backup_directory: str = DEFAULT_BACKUP_DIR, 
                 retention_days: int = BACKUP_RETENTION_DAYS,
                 max_backups: int = MAX_BACKUP_FILES):
        """
        Initialize the BackupManager.
        
        Args:
            backup_directory: Directory to store backup files
            retention_days: Number of days to retain backups
            max_backups: Maximum number of backup files to keep
        """
        self.backup_dir = Path(backup_directory)
        self.retention_days = retention_days
        self.max_backups = max_backups
        
        # Create backup directory if it doesn't exist
        self.backup_dir.mkdir(exist_ok=True)
    
    def create_backup(self, storage_manager: FileStorageManager, 
                     backup_name: Optional[str] = None) -> str:
        """
        Create a backup of the current tasks.
        
        Args:
            storage_manager: FileStorageManager instance to get tasks from
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
        current_tasks = storage_manager.load_tasks()
        storage_manager.save_tasks(current_tasks, str(backup_path))
        
        # Apply retention policy after creating the new backup
        self._apply_retention_policy()
        
        return str(backup_path)
    
    def list_backups(self) -> List[Dict[str, Any]]:
        """
        List all available backup files with metadata.
        
        Returns:
            List[Dict[str, Any]]: List of backup file information
        """
        backups = []
        
        for backup_file in self.backup_dir.glob("*.json"):
            stat = backup_file.stat()
            modified_time = datetime.fromtimestamp(stat.st_mtime)
            
            # Try to extract metadata from the backup file
            metadata = self._extract_backup_metadata(backup_file)
            
            backups.append({
                "name": backup_file.name,
                "path": str(backup_file),
                "size": stat.st_size,
                "modified": modified_time.isoformat(),
                "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                "task_count": metadata.get("task_count", 0),
                "saved_at": metadata.get("saved_at", ""),
                "version": metadata.get("version", "")
            })
        
        # Sort by modification time (newest first)
        backups.sort(key=lambda x: x["modified"], reverse=True)
        return backups
    
    def restore_from_backup(self, backup_path: str, storage_manager: FileStorageManager) -> bool:
        """
        Restore tasks from a backup file.
        
        Args:
            backup_path: Path to the backup file to restore from
            storage_manager: FileStorageManager instance to restore tasks to
            
        Returns:
            bool: True if restore was successful, False otherwise
        """
        backup_file = Path(backup_path)
        
        if not backup_file.exists():
            raise FileNotFoundError(f"Backup file does not exist: {backup_path}")
        
        # Validate that this is a valid backup file
        if not self._is_valid_backup(backup_file):
            raise ValueError(f"Invalid backup file: {backup_path}")
        
        # Load tasks from backup and save to main storage
        backup_tasks = storage_manager.load_tasks(str(backup_file))
        success = storage_manager.save_tasks(backup_tasks)
        
        return success
    
    def _extract_backup_metadata(self, backup_file: Path) -> Dict[str, Any]:
        """
        Extract metadata from a backup file.
        
        Args:
            backup_file: Path to the backup file
            
        Returns:
            Dict[str, Any]: Metadata from the backup file
        """
        try:
            with open(backup_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # Return metadata fields if they exist
            return {
                "version": data.get("version", ""),
                "saved_at": data.get("saved_at", ""),
                "task_count": data.get("task_count", 0)
            }
        except Exception:
            # If there's an error reading the file, return empty metadata
            return {}
    
    def _is_valid_backup(self, backup_file: Path) -> bool:
        """
        Check if a file is a valid backup file.
        
        Args:
            backup_file: Path to the file to check
            
        Returns:
            bool: True if the file is a valid backup, False otherwise
        """
        try:
            with open(backup_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # Check if the file has the expected structure
            return isinstance(data, dict) and "tasks" in data
        except Exception:
            return False
    
    def _apply_retention_policy(self):
        """
        Apply retention policy by removing old backups.
        """
        # Get all backups sorted by modification time (oldest first)
        backups = self.list_backups()
        backups.sort(key=lambda x: x["modified"])  # Oldest first
        
        # Remove backups that exceed retention days
        cutoff_date = datetime.now() - timedelta(days=self.retention_days)
        for backup in backups:
            backup_date = datetime.fromisoformat(backup["modified"])
            if backup_date < cutoff_date:
                backup_path = Path(backup["path"])
                backup_path.unlink()  # Delete the file
        
        # After removing old backups, check if we still exceed max_backups
        backups = self.list_backups()
        backups.sort(key=lambda x: x["modified"])  # Oldest first
        
        # Remove oldest backups if we exceed the maximum count
        while len(backups) > self.max_backups:
            oldest_backup = backups.pop(0)
            backup_path = Path(oldest_backup["path"])
            backup_path.unlink()  # Delete the file