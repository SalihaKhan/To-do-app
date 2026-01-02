"""
Tests for the Todo CLI skill.
Verifies that all 5 supported actions function correctly.
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from todo_cli.todo.task import Task
from todo_cli.todo.task_manager import TaskManager


def test_task_creation():
    """
    Test the Task model creation and properties.
    """
    print("Testing Task creation...")
    
    task = Task(1, "Test Title", "Test Description", False)
    
    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed == False
    
    print("PASS: Task creation test passed")

    # Test string representation
    task_str = str(task)
    assert "[O] 1. Test Title - Test Description" in task_str
    print("PASS: Task string representation test passed")

    # Test completed task representation
    task.completed = True
    task_str_completed = str(task)
    assert "[X] 1. Test Title - Test Description" in task_str_completed
    print("PASS: Task completed representation test passed")


def test_task_manager():
    """
    Test the TaskManager functionality.
    """
    print("\nTesting TaskManager...")
    
    tm = TaskManager()
    
    # Test adding a task
    task1 = tm.add_task("Task 1", "Description 1")
    assert task1.id == 1
    assert task1.title == "Task 1"
    assert task1.description == "Description 1"
    assert task1.completed == False
    print("✓ Add task test passed")
    
    # Test adding another task
    task2 = tm.add_task("Task 2", "Description 2")
    assert task2.id == 2
    print("PASS: Sequential ID generation test passed")

    # Test listing tasks
    tasks = tm.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[1].id == 2
    print("PASS: List tasks test passed")

    # Test getting a specific task
    retrieved_task = tm.get_task(1)
    assert retrieved_task is not None
    assert retrieved_task.id == 1
    assert retrieved_task.title == "Task 1"
    print("PASS: Get specific task test passed")

    # Test updating a task
    update_result = tm.update_task(1, "Updated Title", "Updated Description")
    assert update_result == True
    updated_task = tm.get_task(1)
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"
    print("PASS: Update task test passed")

    # Test marking task as complete
    complete_result = tm.mark_task_complete(1)
    assert complete_result == True
    completed_task = tm.get_task(1)
    assert completed_task.completed == True
    print("PASS: Mark task complete test passed")

    # Test marking task as incomplete
    incomplete_result = tm.mark_task_incomplete(1)
    assert incomplete_result == True
    incomplete_task = tm.get_task(1)
    assert incomplete_task.completed == False
    print("PASS: Mark task incomplete test passed")

    # Test deleting a task
    delete_result = tm.delete_task(2)
    assert delete_result == True
    assert tm.get_task(2) is None
    assert len(tm.list_tasks()) == 1
    print("PASS: Delete task test passed")

    # Test operations on non-existent task
    assert tm.get_task(999) is None
    assert tm.update_task(999, "New Title", "New Description") == False
    assert tm.delete_task(999) == False
    assert tm.mark_task_complete(999) == False
    assert tm.mark_task_incomplete(999) == False
    print("PASS: Non-existent task operations test passed")


def run_all_tests():
    """
    Run all tests for the Todo CLI skill.
    """
    print("Running tests for Todo CLI skill...\n")
    
    try:
        test_task_creation()
        test_task_manager()
        
        print("\nALL TESTS PASSED SUCCESSFULLY!")
        return True
    except AssertionError as e:
        print(f"\nTEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\nUNEXPECTED ERROR DURING TESTS: {e}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    if not success:
        sys.exit(1)