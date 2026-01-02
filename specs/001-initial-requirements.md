# 001-initial-requirements.md — Overall Todo CLI Requirements

## Purpose
This specification defines the overall requirements for the Phase-I In-Memory Python CLI Todo application. The application will provide a command-line interface for users to manage their tasks efficiently without any persistence beyond the current session.

## In-Scope Items
- Command-line interface for task management
- In-memory storage of tasks during runtime
- Support for the 5 core operations: Add, List, Update, Delete, Mark Complete/Incomplete
- Task model with ID, title, description, and completion status
- User-friendly menu system
- Input validation and error handling
- Sequential task ID generation starting from 1

## Out-of-Scope Items
- Database or file persistence
- Web interface or GUI
- User authentication or accounts
- Task categories or tagging system
- Task due dates or scheduling
- Cloud synchronization
- Mobile application
- API endpoints
- Async or concurrent operations

## Acceptance Criteria
1. Users can start the application and see a main menu
2. Users can add tasks with title and description
3. Users can list all tasks with their ID, title, and completion status
4. Users can update existing tasks
5. Users can delete tasks by ID
6. Users can mark tasks as complete or incomplete
7. All operations work correctly with in-memory storage
8. The application handles invalid inputs gracefully
9. Sequential task IDs are generated correctly
10. The application exits cleanly when requested