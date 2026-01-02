<!-- 
Sync Impact Report:
  Version change: N/A (new file) → 1.0.0
  Added sections: All sections
  Templates requiring updates: N/A
  Follow-up TODOs: None
-->

# Todo Evolution — Phase I Spec Constitution

## Purpose
This constitution defines the **rules, principles, and workflow** for creating, managing, and implementing specifications for the Phase-I In-Memory Todo CLI application. It ensures **consistency, clarity, and spec-driven development** across the project.

---

## Scope
- Phase I only: In-memory Python CLI Todo application
- Covers all 5 core features:
  1. Add Task
  2. List Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
- Excludes:
  - Databases or file storage
  - Web frameworks or APIs
  - Async or cloud-native features
  - Features beyond Phase-I requirements

---

## Principles
- **Spec-First Workflow:** Specifications must be written before any implementation.
- **Versioning:** Each spec must be versioned and stored in `/specs/history`.
- **Clarity:** Specs must be precise, unambiguous, and testable.
- **Minimalism:** Only include what is necessary for Phase-I.
- **Reusability:** Specs should support future phases without violating Phase-I constraints.

---

## Spec Creation Rules
1. **Single Concern per Spec:** Each markdown file addresses only one feature or module.
2. **Structure:**
   - Purpose
   - In-scope
   - Out-of-scope
   - Acceptance Criteria
3. **Naming:** Use the format: `001-feature-name.md`, `002-feature-name.md`, etc.
4. **History Maintenance:** All previous versions must be stored in `/specs/history`.

---

## Implementation Rules
- Implementation must strictly follow approved specs.
- Code must follow **clean code principles**:
  - Single Responsibility
  - Separation of Concerns
  - Readability over complexity
- Phase-I constraints are absolute:
  - In-memory storage only
  - Python 3.13+
  - No external libraries
  - No async, DB, or cloud features

---

## Validation & Review
- Use the **Reviewer / Validator Sub-Agent** to validate all specs and code.
- Validation criteria:
  - All 5 actions implemented
  - CLI runs without errors
  - Code matches approved specs
  - No scope violations
- Rejected specs must be revised and re-submitted.

---

## Skill Alignment
- Specs serve as input for **Skill Creation Process**:
  1. Understand requirements
  2. Plan reusable scripts and references
  3. Implement resources and write SKILL.md
  4. Package skill
  5. Iterate based on real CLI usage

---

## Governance
- The **Product Architect (Main Agent)** oversees all spec and skill development.
- Sub-Agents are responsible for:
  - Spec Writing
  - Task Model Design
  - CLI Flow
  - Code Generation
  - Review / Validation
  - Skill Packaging

All agents must adhere strictly to this constitution.

---

## Enforcement
Any deviation from this constitution invalidates the Phase-I implementation and must be corrected before packaging or submission.