import sys
sys.path.insert(0, 'src')

from models.task import Task
from services.task_service import TaskService

def test_implementation():
    print("Testing Task model...")
    task = Task(1, 'Test Title', 'Test Description')
    assert task.id == 1
    assert task.title == 'Test Title'
    assert task.description == 'Test Description'
    assert task.completed == False
    print("SUCCESS: Task model test passed")

    print("Testing TaskService...")
    service = TaskService()
    added_task = service.add_task('Test Task', 'Test Description')
    assert added_task.id == 1
    assert added_task.title == 'Test Task'
    assert added_task.description == 'Test Description'
    assert added_task.completed == False
    print("SUCCESS: Add task test passed")

    print("Testing update task...")
    result = service.update_task(1, 'Updated Title', 'Updated Description')
    assert result == True
    updated_task = service.get_task_by_id(1)
    assert updated_task.title == 'Updated Title'
    assert updated_task.description == 'Updated Description'
    print("SUCCESS: Update task test passed")

    print("Testing mark complete...")
    result = service.mark_task_complete(1)
    assert result == True
    completed_task = service.get_task_by_id(1)
    assert completed_task.completed == True
    print("SUCCESS: Mark complete test passed")

    print("Testing mark incomplete...")
    result = service.mark_task_incomplete(1)
    assert result == True
    incomplete_task = service.get_task_by_id(1)
    assert incomplete_task.completed == False
    print("SUCCESS: Mark incomplete test passed")

    print("Testing delete task...")
    result = service.delete_task(1)
    assert result == True
    assert service.get_task_by_id(1) is None
    print("SUCCESS: Delete task test passed")

    print("\nAll tests passed! Implementation is working correctly.")

if __name__ == "__main__":
    test_implementation()