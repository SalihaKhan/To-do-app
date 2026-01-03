"""
CLI messages for the Todo CLI application.
Provides standardized error and status messages for persistence operations.
"""

def display_error_message(error_type: str, details: str = ""):
    """
    Display a standardized error message.
    
    Args:
        error_type: Type of error that occurred
        details: Additional details about the error
    """
    print(f"❌ Error [{error_type}]: {details}")


def display_success_message(operation: str, details: str = ""):
    """
    Display a standardized success message.
    
    Args:
        operation: The operation that was successful
        details: Additional details about the success
    """
    print(f"✅ {operation} completed: {details}")


def display_status_message(status: str, details: str = ""):
    """
    Display a standardized status message.
    
    Args:
        status: The status to display
        details: Additional details about the status
    """
    print(f"ℹ️  {status}: {details}")


def display_warning_message(warning_type: str, details: str = ""):
    """
    Display a standardized warning message.
    
    Args:
        warning_type: Type of warning
        details: Additional details about the warning
    """
    print(f"⚠️  Warning [{warning_type}]: {details}")


def format_persistence_error(error: Exception) -> str:
    """
    Format a persistence-related error for display to the user.
    
    Args:
        error: The exception that occurred
        
    Returns:
        str: Formatted error message for the user
    """
    error_msg = str(error)
    
    # Provide more user-friendly messages for common errors
    if "Permission denied" in error_msg:
        return "Permission denied. Please check file permissions."
    elif "File not found" in error_msg or "No such file" in error_msg:
        return "File not found. Please check the file path."
    elif "Invalid file format" in error_msg:
        return "Invalid file format. The file may be corrupted or not a task file."
    else:
        return f"An error occurred: {error_msg}"