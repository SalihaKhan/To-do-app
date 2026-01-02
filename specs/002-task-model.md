# 002-task-model.md — Task Data Model Specification

## Purpose
This specification defines the data model for tasks in the Phase-I In-Memory Python CLI Todo application. It establishes the structure and properties of a task entity that will be used throughout the application.

## In-Scope Items
- Task ID (integer, sequential)
- Task title (string)
- Task description (string)
- Task completion status (boolean)
- Task string representation
- Task initialization with default values

## Out-of-Scope Items
- Database schema
- File storage format
- Network serialization
- Task relationships or dependencies
- Task metadata (created date, modified date, etc.)
- Task priority levels
- Task categories or tags

## Acceptance Criteria
1. A Task object can be created with an ID, title, and description
2. A Task object has a completion status that defaults to False
3. A Task object provides a string representation showing status, ID, title, and description
4. The string representation uses 'X' for completed tasks and 'O' for incomplete tasks
5. Task properties (id, title, description, completed) are accessible as public attributes
6. The Task model supports all required operations in the application
7. Task IDs are sequential integers starting from 1
8. Task title and description are strings that can be modified
9. The Task model follows the single responsibility principle