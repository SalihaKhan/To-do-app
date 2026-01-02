"""
CLI interface for the Todo CLI skill.
Provides a command-line menu for interacting with tasks.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from todo_cli.todo.task_manager import TaskManager
from typing import Optional


class TodoCLI:
    """
    Command-line interface for the Todo application.
    Provides menu options for all 5 supported actions.
    """
    
    def __init__(self):
        """
        Initialize a new TodoCLI instance.
        """
        self.task_manager = TaskManager()
    
    def display_menu(self):
        """
        Display the main menu options.
        """
        print("\n" + "="*40)
        print("         TODO CLI APPLICATION")
        print("="*40)
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        print("="*40)
    
    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.
        
        Returns:
            str: The user's choice
        """
        return input("Enter your choice (1-6): ").strip()
    
    def add_task(self):
        """
        Handle adding a new task.
        """
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()
        if not title:
            print("Error: Task title cannot be empty.")
            return
        
        description = input("Enter task description: ").strip()
        if not description:
            description = "No description provided"
        
        task = self.task_manager.add_task(title, description)
        print(f"Task added successfully with ID {task.id}")
    
    def list_tasks(self):
        """
        Handle listing all tasks.
        """
        print("\n--- Task List ---")
        tasks = self.task_manager.list_tasks()
        
        if not tasks:
            print("No tasks found.")
            return
        
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"{task.id}. [{status}] {task.title}")
            print(f"    {task.description}\n")
    
    def update_task(self):
        """
        Handle updating an existing task.
        """
        print("\n--- Update Task ---")
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return
        
        task = self.task_manager.get_task(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        print(f"Current task: {task.title}")
        new_title = input(f"Enter new title (or press Enter to keep '{task.title}'): ").strip()
        
        print(f"Current description: {task.description}")
        new_description = input(f"Enter new description (or press Enter to keep current): ").strip()
        
        # Use None to indicate no change if user presses Enter
        updated_title = new_title if new_title else None
        updated_description = new_description if new_description else None
        
        if self.task_manager.update_task(task_id, updated_title, updated_description):
            print("Task updated successfully.")
        else:
            print("Error: Failed to update task.")
    
    def delete_task(self):
        """
        Handle deleting a task.
        """
        print("\n--- Delete Task ---")
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return
        
        if self.task_manager.delete_task(task_id):
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    
    def mark_task_status(self):
        """
        Handle marking a task as complete/incomplete.
        """
        print("\n--- Mark Task Status ---")
        try:
            task_id = int(input("Enter task ID: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return
        
        task = self.task_manager.get_task(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        print(f"Current status: {'Completed' if task.completed else 'Pending'}")
        print("1. Mark as Complete")
        print("2. Mark as Incomplete")
        
        choice = input("Select option (1 or 2): ").strip()
        
        if choice == "1":
            if self.task_manager.mark_task_complete(task_id):
                print("Task marked as complete.")
            else:
                print("Error: Failed to update task status.")
        elif choice == "2":
            if self.task_manager.mark_task_incomplete(task_id):
                print("Task marked as incomplete.")
            else:
                print("Error: Failed to update task status.")
        else:
            print("Error: Invalid choice. Please select 1 or 2.")
    
    def run(self):
        """
        Run the main application loop.
        """
        print("Welcome to the Todo CLI Application!")
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_status()
            elif choice == "6":
                print("Thank you for using the Todo CLI Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
    
    def start(self):
        """
        Start the CLI application.
        """
        self.run()


def main():
    """
    Main entry point for the CLI application.
    """
    cli = TodoCLI()
    cli.start()


if __name__ == "__main__":
    main()