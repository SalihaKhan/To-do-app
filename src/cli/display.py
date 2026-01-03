"""
CLI display utilities for the Todo CLI application.
Provides functions for displaying progress indicators and other UI elements.
"""

import sys
import time
from typing import Generator


def display_progress_bar(current: int, total: int, bar_length: int = 30):
    """
    Display a progress bar for file operations.
    
    Args:
        current: Current progress value
        total: Total value for completion
        bar_length: Length of the progress bar in characters
    """
    if total <= 0:
        return
    
    percent = float(current) * 100 / total
    filled_length = int(round(bar_length * current / float(total)))
    
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    
    sys.stdout.write(f'\r|{bar}| {percent:.2f}% Complete')
    sys.stdout.flush()
    
    if current == total:
        print()  # New line when complete


def display_loading_indicator(message: str = "Loading", duration: float = 0.5):
    """
    Display a simple loading indicator.
    
    Args:
        message: Message to display with the indicator
        duration: Duration to show each frame (in seconds)
    """
    for frame in ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']:
        print(f'\r{frame} {message}...', end='', flush=True)
        time.sleep(duration)
    print('\r✅ Done!')


def display_spinner(message: str = "Processing"):
    """
    Display a spinner animation for ongoing operations.
    
    Args:
        message: Message to display with the spinner
    """
    import itertools
    import threading
    import time
    
    def spin(cursor: Generator[str, None, None], done: threading.Event):
        for cursor_val in cursor:
            if done.is_set():
                break
            print(f'\r{cursor_val} {message}...', end='', flush=True)
            time.sleep(0.1)
    
    # Create a done event to stop the spinner
    done_event = threading.Event()
    
    # Start the spinner in a separate thread
    spinner_thread = threading.Thread(
        target=spin, 
        args=(itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']), done_event)
    )
    spinner_thread.start()
    
    return done_event, spinner_thread


def hide_spinner(done_event: threading.Event, spinner_thread: threading.Thread):
    """
    Stop and hide a spinner animation.
    
    Args:
        done_event: The threading.Event used to stop the spinner
        spinner_thread: The threading.Thread running the spinner
    """
    done_event.set()
    spinner_thread.join()
    print('\r', end='')  # Clear the line