# Quickstart Guide for Todo CLI Application

## Prerequisites
- Python 3.13 or higher
- No external libraries required

## Setup
1. Clone or download the repository
2. Navigate to the project directory
3. Ensure you have Python 3.13+ installed

## Running the Application
1. Open a terminal/command prompt
2. Navigate to the project directory
3. Run the command: `python src/main.py`
4. The main menu will appear with numbered options

## Using the Application
1. **Add Task**: Select option 1, then enter the task title and description when prompted
2. **List Tasks**: Select option 2 to view all tasks with their status
3. **Update Task**: Select option 3, enter the task ID, and provide new title/description
4. **Delete Task**: Select option 4 and enter the task ID to delete
5. **Mark Complete/Incomplete**: Select option 5, enter task ID, and choose status
6. **Exit**: Select option 6 to quit the application

## Example Workflow
1. Run `python src/main.py`
2. Select "1" to add a task
3. Enter "Buy groceries" as title
4. Enter "Milk, bread, eggs" as description
5. Select "2" to list tasks and see your new task
6. Select "5" to mark the task as complete
7. Select "6" to exit the application

## Troubleshooting
- If you get a "module not found" error, ensure you're running from the project root directory
- If the application crashes, check that you're entering valid inputs (numbers for IDs, text for titles/descriptions)
- For any other issues, ensure Python 3.13+ is installed and in your PATH