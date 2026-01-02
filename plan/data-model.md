# Data Model for Todo CLI Application

## Task Entity

### Attributes
- **id**: int
  - Unique identifier for the task
  - Sequential, starting from 1
  - Read-only after creation
- **title**: str
  - Title of the task
  - Required field
  - Can be updated
- **description**: str
  - Detailed description of the task
  - Optional field (can be empty string)
  - Can be updated
- **completed**: bool
  - Completion status of the task
  - Defaults to False
  - Can be toggled between True and False

### Methods
- `__str__()`: Returns a formatted string representation of the task
- `__repr__()`: Returns a developer-friendly representation
- `to_dict()`: Converts the task to a dictionary representation

### State Transitions
- New Task: id, title, description, completed=False
- Update: Any attribute except id can be modified
- Complete: completed changes from False to True
- Incomplete: completed changes from True to False

## TaskService Entity

### Methods
- `add_task(title: str, description: str) -> Task`
  - Creates a new task with the next available ID
  - Returns the created Task object
- `get_all_tasks() -> List[Task]`
  - Returns a copy of all tasks
- `get_task_by_id(task_id: int) -> Optional[Task]`
  - Returns the task with the given ID or None if not found
- `update_task(task_id: int, title: str = None, description: str = None) -> bool`
  - Updates the specified task with new values
  - Returns True if successful, False if task not found
- `delete_task(task_id: int) -> bool`
  - Deletes the task with the given ID
  - Returns True if successful, False if task not found
- `mark_task_complete(task_id: int) -> bool`
  - Marks the specified task as complete
  - Returns True if successful, False if task not found
- `mark_task_incomplete(task_id: int) -> bool`
  - Marks the specified task as incomplete
  - Returns True if successful, False if task not found

### Internal Attributes
- `_tasks`: List[Task]
  - In-memory storage of all tasks
- `_next_id`: int
  - The next available ID for new tasks