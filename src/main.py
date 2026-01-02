"""
Main entry point for the Todo CLI application.
Implements a command-line interface for managing todo tasks.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.task import Task
from services.task_service import TaskService
from utils.helpers import display_menu, get_user_input, validate_task_id


def main():
    """Main function to run the Todo CLI application."""
    print("Welcome to the Todo CLI Application!")
    
    task_service = TaskService()
    
    while True:
        display_menu()
        choice = get_user_input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_task(task_service)
        elif choice == "2":
            list_tasks(task_service)
        elif choice == "3":
            update_task(task_service)
        elif choice == "4":
            delete_task(task_service)
        elif choice == "5":
            mark_task_status(task_service)
        elif choice == "6":
            print("Thank you for using the Todo CLI Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


def add_task(task_service):
    """Handle adding a new task."""
    print("\n--- Add New Task ---")
    title = get_user_input("Enter task title: ")
    if not title:
        print("Error: Task title cannot be empty.")
        return
    
    description = get_user_input("Enter task description: ")
    if not description:
        description = "No description provided"
    
    task = task_service.add_task(title, description)
    print(f"Task added successfully with ID {task.id}")


def list_tasks(task_service):
    """Handle listing all tasks."""
    print("\n--- Task List ---")
    tasks = task_service.get_all_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"{task.id}. [{status}] {task.title}")
        print(f"    {task.description}\n")


def update_task(task_service):
    """Handle updating an existing task."""
    print("\n--- Update Task ---")
    try:
        task_id_input = get_user_input("Enter task ID to update: ")
        task_id = validate_task_id(task_id_input)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    task = task_service.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    
    print(f"Current task: {task.title}")
    new_title = get_user_input(f"Enter new title (or press Enter to keep '{task.title}'): ")
    
    print(f"Current description: {task.description}")
    new_description = get_user_input(f"Enter new description (or press Enter to keep current): ")
    
    # Use None to indicate no change if user presses Enter
    updated_title = new_title if new_title else None
    updated_description = new_description if new_description else None
    
    if task_service.update_task(task_id, updated_title, updated_description):
        print("Task updated successfully.")
    else:
        print("Error: Failed to update task.")


def delete_task(task_service):
    """Handle deleting a task."""
    print("\n--- Delete Task ---")
    try:
        task_id_input = get_user_input("Enter task ID to delete: ")
        task_id = validate_task_id(task_id_input)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    if task_service.delete_task(task_id):
        print(f"Task with ID {task_id} deleted successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")


def mark_task_status(task_service):
    """Handle marking a task as complete/incomplete."""
    print("\n--- Mark Task Status ---")
    try:
        task_id_input = get_user_input("Enter task ID: ")
        task_id = validate_task_id(task_id_input)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    task = task_service.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    
    print(f"Current status: {'Completed' if task.completed else 'Pending'}")
    print("1. Mark as Complete")
    print("2. Mark as Incomplete")
    
    choice = get_user_input("Select option (1 or 2): ")
    
    if choice == "1":
        if task_service.mark_task_complete(task_id):
            print("Task marked as complete.")
        else:
            print("Error: Failed to update task status.")
    elif choice == "2":
        if task_service.mark_task_incomplete(task_id):
            print("Task marked as incomplete.")
        else:
            print("Error: Failed to update task status.")
    else:
        print("Error: Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()