"""
Constants for the Todo CLI application.
Contains all constant values used throughout the application.
"""

# Persistence-related constants
DEFAULT_DATA_FILE = "tasks.json"
DEFAULT_BACKUP_DIR = "backups"
DEFAULT_CONFIG_FILE = "config.json"
MAX_BACKUP_FILES = 10
BACKUP_RETENTION_DAYS = 30

# File format constants
CURRENT_DATA_VERSION = "1.0"
DATA_FILE_ENCODING = "utf-8"

# Error messages
ERROR_FILE_NOT_FOUND = "File not found"
ERROR_PERMISSION_DENIED = "Permission denied"
ERROR_INVALID_FORMAT = "Invalid file format"
ERROR_CORRUPTED_DATA = "Data appears to be corrupted"