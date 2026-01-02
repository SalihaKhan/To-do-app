"""
Demo script to showcase the Todo CLI skill functionality without user interaction.
"""

from todo_cli.todo.task_manager import TaskManager

def demo_task_manager():
    """
    Demonstrate the TaskManager functionality.
    """
    print("=== Todo CLI Skill Demo ===\n")
    
    # Create a task manager instance
    tm = TaskManager()
    
    # Demo: Add tasks
    print("1. Adding tasks...")
    task1 = tm.add_task("Buy groceries", "Milk, bread, eggs, fruits")
    print(f"   Added: {task1}")
    
    task2 = tm.add_task("Complete project", "Finish the Todo CLI skill implementation")
    print(f"   Added: {task2}")
    
    # Demo: List tasks
    print("\n2. Listing all tasks...")
    tasks = tm.list_tasks()
    for task in tasks:
        print(f"   {task}")
    
    # Demo: Update a task
    print("\n3. Updating a task...")
    update_success = tm.update_task(1, "Buy groceries (updated)", "Milk, bread, eggs, fruits, vegetables")
    if update_success:
        updated_task = tm.get_task(1)
        print(f"   Updated: {updated_task}")
    else:
        print("   Update failed")
    
    # Demo: Mark task as complete
    print("\n4. Marking a task as complete...")
    complete_success = tm.mark_task_complete(1)
    if complete_success:
        completed_task = tm.get_task(1)
        print(f"   Marked as complete: {completed_task}")
    else:
        print("   Mark complete failed")
    
    # Demo: Mark task as incomplete
    print("\n5. Marking a task as incomplete...")
    incomplete_success = tm.mark_task_incomplete(2)
    if incomplete_success:
        incomplete_task = tm.get_task(2)
        print(f"   Marked as incomplete: {incomplete_task}")
    else:
        print("   Mark incomplete failed")
    
    # Demo: Delete a task
    print("\n6. Deleting a task...")
    delete_success = tm.delete_task(2)
    if delete_success:
        print("   Task with ID 2 deleted")
    else:
        print("   Delete failed")
    
    # Show remaining tasks
    print("\n7. Remaining tasks...")
    remaining_tasks = tm.list_tasks()
    if remaining_tasks:
        for task in remaining_tasks:
            print(f"   {task}")
    else:
        print("   No tasks remaining")
    
    print("\n=== Demo completed successfully! ===")


if __name__ == "__main__":
    demo_task_manager()