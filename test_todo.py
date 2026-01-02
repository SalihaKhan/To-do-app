"""
Test script to verify the Todo CLI application functionality without user interaction.
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

# Add the src directory to the path so imports work correctly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from models.task import Task
from services.task_service import TaskService


def test_task_creation():
    """Test the Task model creation and properties."""
    print("Testing Task creation...")
    
    task = Task(1, "Test Title", "Test Description", False)
    
    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed == False
    
    print("SUCCESS: Task creation test passed")

    # Test string representation
    task_str = str(task)
    assert "[O] 1. Test Title - Test Description" in task_str
    print("SUCCESS: Task string representation test passed")

    # Test completed task representation
    task.completed = True
    task_str_completed = str(task)
    assert "[X] 1. Test Title - Test Description" in task_str_completed
    print("SUCCESS: Task completed representation test passed")


def test_task_service():
    """Test the TaskService functionality."""
    print("\nTesting TaskService...")
    
    ts = TaskService()
    
    # Test adding a task
    task1 = ts.add_task("Task 1", "Description 1")
    assert task1.id == 1
    assert task1.title == "Task 1"
    assert task1.description == "Description 1"
    assert task1.completed == False
    print("SUCCESS: Add task test passed")

    # Test adding another task
    task2 = ts.add_task("Task 2", "Description 2")
    assert task2.id == 2
    print("SUCCESS: Sequential ID generation test passed")

    # Test getting all tasks
    tasks = ts.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[1].id == 2
    print("SUCCESS: Get all tasks test passed")

    # Test getting a specific task
    retrieved_task = ts.get_task_by_id(1)
    assert retrieved_task is not None
    assert retrieved_task.id == 1
    assert retrieved_task.title == "Task 1"
    print("SUCCESS: Get specific task test passed")

    # Test updating a task
    update_result = ts.update_task(1, "Updated Title", "Updated Description")
    assert update_result == True
    updated_task = ts.get_task_by_id(1)
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"
    print("SUCCESS: Update task test passed")

    # Test marking task as complete
    complete_result = ts.mark_task_complete(1)
    assert complete_result == True
    completed_task = ts.get_task_by_id(1)
    assert completed_task.completed == True
    print("SUCCESS: Mark task complete test passed")

    # Test marking task as incomplete
    incomplete_result = ts.mark_task_incomplete(1)
    assert incomplete_result == True
    incomplete_task = ts.get_task_by_id(1)
    assert incomplete_task.completed == False
    print("SUCCESS: Mark task incomplete test passed")

    # Test deleting a task
    delete_result = ts.delete_task(2)
    assert delete_result == True
    assert ts.get_task_by_id(2) is None
    assert len(ts.get_all_tasks()) == 1
    print("SUCCESS: Delete task test passed")

    # Test operations on non-existent task
    assert ts.get_task_by_id(999) is None
    assert ts.update_task(999, "New Title", "New Description") == False
    assert ts.delete_task(999) == False
    assert ts.mark_task_complete(999) == False
    assert ts.mark_task_incomplete(999) == False
    print("SUCCESS: Non-existent task operations test passed")


def run_tests():
    """Run all tests for the Todo CLI application."""
    print("Running tests for Todo CLI application...\n")
    
    try:
        test_task_creation()
        test_task_service()
        
        print("\nALL TESTS PASSED SUCCESSFULLY!")
        return True
    except AssertionError as e:
        print(f"\nTEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\nUNEXPECTED ERROR DURING TESTS: {e}")
        return False


if __name__ == "__main__":
    success = run_tests()
    if not success:
        sys.exit(1)