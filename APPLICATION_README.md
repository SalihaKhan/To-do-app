# Todo CLI Application

This is a Phase-I Todo CLI application that manages tasks in memory only. It implements all 5 required actions with a clean, user-friendly command-line interface.

## Features

- **Add Task**: Create new tasks with title and description
- **List Tasks**: View all tasks with their status
- **Update Task**: Modify existing tasks
- **Delete Task**: Remove tasks
- **Mark Task Complete/Incomplete**: Update task completion status

## Architecture

The application follows the specified folder structure:
```
src/
├── main.py
├── models/
│   └── task.py
├── services/
│   └── task_service.py
└── utils/
    └── helpers.py
```

## Components

- `main.py`: Main entry point with CLI interface
- `models/task.py`: Defines the Task model with id, title, description, and completion status
- `services/task_service.py`: Handles in-memory storage and CRUD operations for tasks
- `utils/helpers.py`: Contains helper functions for the application

## Usage

To run the application:
```bash
python src/main.py
```

## Validation

The implementation follows all Phase-I constraints:
- Python 3.13+ compatible
- In-memory only (no persistence)
- No external libraries
- No async or cloud features
- Single Responsibility and Separation of Concerns principles
- All 5 required actions implemented
- Deterministic task IDs
- Clear CLI menu
- Input validation and error messages

## Testing

Run the tests with:
```bash
python test_todo.py
```

Run the demo with:
```bash
python demo_app.py
```