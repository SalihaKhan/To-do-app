# Todo CLI Application - Phase I

## Project Overview

This is a complete implementation of a command-line interface (CLI) Todo application built as part of the Todo Evolution Phase I project. The application provides a simple, efficient way to manage tasks directly from the command line with in-memory storage only.

## Features

- **Add Task**: Create new tasks with title and description
- **List Tasks**: View all tasks with their ID, title, and completion status
- **Update Task**: Modify existing task title and description
- **Delete Task**: Remove tasks by ID
- **Mark Complete/Incomplete**: Toggle task completion status
- **Sequential Task IDs**: Automatically generated unique IDs for each task
- **Input Validation**: Robust validation for all user inputs
- **Clear Menu Interface**: Intuitive command-line menu system

## Architecture

The application follows a clean, modular architecture with separation of concerns:

- **Models**: Contains the Task class definition
- **Services**: Implements the TaskService with all business logic
- **Utils**: Provides helper functions for CLI interactions
- **Main**: Contains the CLI interface and user interaction logic

## Project Structure

```
src/
├── main.py          # Main CLI application entry point
├── models/
│   └── task.py      # Task model definition
├── services/
│   └── task_service.py # Task service with CRUD operations
└── utils/
    └── helpers.py   # Helper functions for CLI utilities
```

## Implementation Details

- **Language**: Python 3.13+
- **Storage**: In-memory only (no persistence)
- **Dependencies**: None (pure Python standard library)
- **Design Principles**: Single Responsibility, Separation of Concerns, Readability over complexity
- **Constraints**: Phase-I compliant (no external libraries, no async, no cloud features)

## Usage

1. Ensure Python 3.13+ is installed on your system
2. Navigate to the project directory
3. Run the application with: `python src/main.py`
4. Follow the on-screen menu prompts to interact with the application

## Phase-I Compliance

This implementation strictly adheres to all Phase-I constraints:
- In-memory storage only (no file or database persistence)
- No external libraries used
- No async or concurrent operations
- No cloud or network features
- Clean, modular code following specified principles
- All 5 core features implemented as specified

## Components

### Task Model
- `id`: Sequential integer identifier
- `title`: String representing the task title
- `description`: String with detailed task description
- `completed`: Boolean indicating completion status

### Task Service
- `add_task()`: Creates new tasks with sequential IDs
- `list_tasks()`: Returns all tasks
- `get_task_by_id()`: Retrieves specific task
- `update_task()`: Modifies task title/description
- `delete_task()`: Removes tasks by ID
- `toggle_complete()`: Toggles completion status

### CLI Helpers
- Input validation functions
- Menu display utilities
- User interaction helpers

## Validation

The application has been thoroughly tested to ensure:
- All 5 core features work correctly
- Input validation handles edge cases
- Sequential ID generation works properly
- In-memory storage functions as expected
- Error handling is robust
- Phase-I constraints are fully satisfied