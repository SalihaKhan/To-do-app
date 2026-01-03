"""
Error handling utilities for file operations in the Todo CLI application.
Defines custom exceptions and error handling patterns for persistence operations.
"""

from typing import Any


class PersistenceError(Exception):
    """
    Base exception for persistence-related errors.
    """
    def __init__(self, message: str, error_code: str = "PERSISTENCE_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.error_code}] {self.message}"


class FileOperationError(PersistenceError):
    """
    Exception for file operation errors (save, load, backup, etc.).
    """
    def __init__(self, message: str, operation: str = "unknown", file_path: str = ""):
        self.operation = operation
        self.file_path = file_path
        error_code = f"FILE_OP_ERROR_{operation.upper()}"
        super().__init__(
            f"File operation '{operation}' failed for '{file_path}': {message}",
            error_code
        )


class DataIntegrityError(PersistenceError):
    """
    Exception for data integrity issues during persistence operations.
    """
    def __init__(self, message: str, context: str = ""):
        self.context = context
        super().__init__(
            f"Data integrity error{' in ' + context if context else ''}: {message}",
            "DATA_INTEGRITY_ERROR"
        )


class ValidationError(PersistenceError):
    """
    Exception for validation errors during persistence operations.
    """
    def __init__(self, message: str, field: str = "", value: Any = None):
        self.field = field
        self.value = value
        super().__init__(
            f"Validation error for field '{field}': {message}" if field 
            else f"Validation error: {message}",
            "VALIDATION_ERROR"
        )


def handle_file_operation(operation_name: str, file_path: str = ""):
    """
    Decorator to handle file operation errors consistently.
    
    Args:
        operation_name: Name of the operation being performed
        file_path: Path of the file being operated on
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except PermissionError:
                raise FileOperationError(
                    "Permission denied", 
                    operation_name, 
                    file_path
                )
            except FileNotFoundError:
                raise FileOperationError(
                    "File not found", 
                    operation_name, 
                    file_path
                )
            except OSError as e:
                raise FileOperationError(
                    f"OS error: {str(e)}", 
                    operation_name, 
                    file_path
                )
            except Exception as e:
                raise FileOperationError(
                    f"Unexpected error: {str(e)}", 
                    operation_name, 
                    file_path
                )
        return wrapper
    return decorator


def validate_file_path(file_path: str) -> bool:
    """
    Validate that a file path is safe and accessible.
    
    Args:
        file_path: Path to validate
        
    Returns:
        bool: True if path is valid, raises ValidationError otherwise
    """
    import os
    from pathlib import Path
    
    if not file_path:
        raise ValidationError("File path cannot be empty", "file_path", file_path)
    
    # Check for path traversal attempts
    if ".." in file_path or "~" in file_path:
        raise ValidationError("Path traversal not allowed", "file_path", file_path)
    
    path_obj = Path(file_path)
    
    # Check if the directory exists
    if not path_obj.parent.exists():
        raise ValidationError(f"Directory does not exist: {path_obj.parent}", "file_path", file_path)
    
    # Check if it's a file (not a directory)
    if path_obj.is_dir():
        raise ValidationError("Path points to a directory, not a file", "file_path", file_path)
    
    return True