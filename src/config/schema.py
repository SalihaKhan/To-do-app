"""
Configuration schema for persistence settings in the Todo CLI application.
Defines the structure and validation rules for configuration data.
"""

from typing import Dict, Any
import os
from pathlib import Path

class ConfigSchema:
    """
    Defines the configuration schema for persistence settings.
    """
    
    def __init__(self):
        """
        Initialize the configuration schema with default values.
        """
        self.defaults = {
            "data_file_path": "tasks.json",
            "backup_directory": "backups/",
            "auto_save": True,
            "backup_retention_days": 30,
            "max_backups": 10,
            "file_format": "json"
        }
    
    def validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate and normalize configuration values.
        
        Args:
            config: Dictionary containing configuration values
            
        Returns:
            Dict[str, Any]: Validated and normalized configuration
        """
        validated_config = self.defaults.copy()
        
        # Validate data file path
        if "data_file_path" in config:
            validated_config["data_file_path"] = str(config["data_file_path"])
        
        # Validate backup directory
        if "backup_directory" in config:
            validated_config["backup_directory"] = str(config["backup_directory"])
            # Ensure directory ends with separator
            if not validated_config["backup_directory"].endswith(os.sep):
                validated_config["backup_directory"] += os.sep
        
        # Validate auto_save setting
        if "auto_save" in config:
            validated_config["auto_save"] = bool(config["auto_save"])
        
        # Validate backup retention days
        if "backup_retention_days" in config:
            days = int(config["backup_retention_days"])
            validated_config["backup_retention_days"] = max(1, days)  # At least 1 day
        
        # Validate max backups
        if "max_backups" in config:
            max_backups = int(config["max_backups"])
            validated_config["max_backups"] = max(1, max_backups)  # At least 1 backup
        
        # Validate file format
        if "file_format" in config:
            format_type = str(config["file_format"]).lower()
            if format_type in ["json", "csv"]:
                validated_config["file_format"] = format_type
            else:
                validated_config["file_format"] = "json"  # Default to JSON
        
        return validated_config
    
    def get_default_config(self) -> Dict[str, Any]:
        """
        Get the default configuration values.
        
        Returns:
            Dict[str, Any]: Default configuration values
        """
        return self.defaults.copy()