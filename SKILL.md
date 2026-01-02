# SKILL.md — Todo Evolution (Phase I)

## Skill Name
In-Memory Todo CLI Skill

## Purpose
Provide a reusable, spec-driven skill for managing Todo tasks in a
Python command-line application using in-memory data only.

This skill is strictly limited to Phase I of the Todo Evolution project.

## Scope

### In Scope
- Python CLI interaction
- In-memory task storage
- Basic CRUD operations
- Deterministic task IDs

### Out of Scope
- Databases or file persistence
- Web frameworks or APIs
- Async or concurrency
- Cloud, containers, or orchestration

## Supported Actions
1. Add Task (title, description)
2. List Tasks (id, title, status)
3. Update Task
4. Delete Task
5. Mark Task Complete / Incomplete

## Task Model
id: int  
title: str  
description: str  
completed: bool  

Rules:
- IDs are sequential
- Tasks exist only during runtime
- No additional fields allowed

## Inputs & Outputs

Inputs:
- CLI menu selection
- User-entered text and IDs

Outputs:
- Console messages
- Task lists with status indicators
- Error messages for invalid input

## Architecture
The skill follows a simple in-memory architecture with:
- A central task manager class that maintains tasks in a list/dictionary
- Sequential ID generation starting from 1
- Basic validation for user inputs
- Console-based user interface
- Simple command routing based on user menu selections

The architecture is designed to be:
- Stateless (no persistence between runs)
- Deterministic (same operations produce same results)
- Minimal dependencies (only standard Python libraries)
- Easy to integrate into larger CLI applications