"""
Datetime utilities for the Todo CLI application.
Provides functions for handling and formatting datetime values.
"""

from datetime import datetime
from typing import Union


def format_timestamp(timestamp: Union[datetime, str] = None, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format a datetime object or string into a readable format.
    
    Args:
        timestamp: The datetime object or ISO string to format (uses current time if None)
        format_str: The format string to use (default: "%Y-%m-%d %H:%M:%S")
        
    Returns:
        str: Formatted timestamp string
    """
    if timestamp is None:
        timestamp = datetime.now()
    elif isinstance(timestamp, str):
        # If it's a string, try to parse it as ISO format
        try:
            timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        except ValueError:
            # If it's not in ISO format, use current time
            timestamp = datetime.now()
    
    return timestamp.strftime(format_str)


def get_current_timestamp() -> str:
    """
    Get the current timestamp in ISO format.
    
    Returns:
        str: Current timestamp in ISO format
    """
    return datetime.now().isoformat()


def parse_timestamp(timestamp_str: str) -> datetime:
    """
    Parse a timestamp string into a datetime object.
    
    Args:
        timestamp_str: The timestamp string to parse
        
    Returns:
        datetime: Parsed datetime object
    """
    return datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))


def format_backup_filename(base_name: str = "tasks", timestamp: str = None) -> str:
    """
    Format a backup filename with a timestamp.
    
    Args:
        base_name: Base name for the backup file (default: "tasks")
        timestamp: Timestamp string to use (uses current time if None)
        
    Returns:
        str: Formatted backup filename
    """
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    return f"{base_name}_backup_{timestamp}.json"