"""
Demo script to showcase the Todo CLI application functionality without user interaction.
"""

from src.models.task import Task
from src.services.task_service import TaskService


def demo_task_service():
    """
    Demonstrate the TaskService functionality.
    """
    print("=== Todo CLI Application Demo ===\n")
    
    # Create a task service instance
    ts = TaskService()
    
    # Demo: Add tasks
    print("1. Adding tasks...")
    task1 = ts.add_task("Buy groceries", "Milk, bread, eggs, fruits")
    print(f"   Added: {task1}")
    
    task2 = ts.add_task("Complete project", "Finish the Todo CLI application implementation")
    print(f"   Added: {task2}")
    
    # Demo: Get all tasks
    print("\n2. Getting all tasks...")
    tasks = ts.get_all_tasks()
    for task in tasks:
        print(f"   {task}")
    
    # Demo: Update a task
    print("\n3. Updating a task...")
    update_success = ts.update_task(1, "Buy groceries (updated)", "Milk, bread, eggs, fruits, vegetables")
    if update_success:
        updated_task = ts.get_task_by_id(1)
        print(f"   Updated: {updated_task}")
    else:
        print("   Update failed")
    
    # Demo: Mark task as complete
    print("\n4. Marking a task as complete...")
    complete_success = ts.mark_task_complete(1)
    if complete_success:
        completed_task = ts.get_task_by_id(1)
        print(f"   Marked as complete: {completed_task}")
    else:
        print("   Mark complete failed")
    
    # Demo: Mark task as incomplete
    print("\n5. Marking a task as incomplete...")
    incomplete_success = ts.mark_task_incomplete(2)
    if incomplete_success:
        incomplete_task = ts.get_task_by_id(2)
        print(f"   Marked as incomplete: {incomplete_task}")
    else:
        print("   Mark incomplete failed")
    
    # Demo: Delete a task
    print("\n6. Deleting a task...")
    delete_success = ts.delete_task(2)
    if delete_success:
        print("   Task with ID 2 deleted")
    else:
        print("   Delete failed")
    
    # Show remaining tasks
    print("\n7. Remaining tasks...")
    remaining_tasks = ts.get_all_tasks()
    if remaining_tasks:
        for task in remaining_tasks:
            print(f"   {task}")
    else:
        print("   No tasks remaining")
    
    print("\n=== Demo completed successfully! ===")


if __name__ == "__main__":
    demo_task_service()