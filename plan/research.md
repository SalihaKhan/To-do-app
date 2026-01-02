# Research Document for Todo CLI Application

## Decision: Python 3.13+ Features
- **Rationale**: Using standard Python features compatible with 3.13+ ensures broad compatibility and maintainability. We'll avoid any bleeding-edge features that might not be stable.
- **Alternatives considered**: 
  - Using newer Python-specific features (not used to maintain compatibility)
  - Sticking to older Python versions (not necessary as 3.13+ is our requirement)

## Decision: CLI Framework
- **Rationale**: Using built-in Python input() and print() functions meets Phase-I constraints of no external libraries while providing the necessary functionality.
- **Alternatives considered**:
  - argparse (not used due to external library constraints)
  - click (not used due to external library constraints)
  - Plain input/print functions (selected)

## Decision: In-Memory Storage
- **Rationale**: Using Python lists and dictionaries for storage is simple, efficient, and meets the in-memory requirement perfectly.
- **Alternatives considered**:
  - Other data structures (not necessary for this scale)
  - Sets or tuples (lists and dicts provide better functionality for this use case)

## Decision: Task ID Generation
- **Rationale**: Sequential integer IDs starting from 1 provide a simple, deterministic approach that's easy to understand and implement.
- **Alternatives considered**:
  - UUIDs (overkill for this simple application)
  - Random integers (would complicate the "deterministic" requirement)
  - Sequential integers (selected)

## Decision: Error Handling
- **Rationale**: Graceful error handling with user-friendly messages improves the user experience while keeping the application stable.
- **Alternatives considered**:
  - Throwing exceptions to the user (not user-friendly)
  - Silent failure (not transparent)
  - Clear error messages (selected)