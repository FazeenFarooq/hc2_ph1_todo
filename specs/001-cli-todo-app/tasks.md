---

description: "Task list for implementing the CLI Todo Application"
---

# Tasks: CLI Todo Application

**Input**: Design documents from `/specs/001-cli-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/
- [X] T002 Initialize Python project with proper directory structure
- [X] T003 [P] Create __init__.py files in all directories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Create TodoItem data model in src/models/todo_item.py
- [X] T005 [P] Create TodoService in src/services/todo_service.py
- [X] T006 [P] Setup CLI argument parser in src/cli/cli_interface.py
- [X] T007 Create main application entry point in src/todo_app.py
- [X] T008 Configure error handling and exception classes

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items with title and description

**Independent Test**: The application should allow a user to input a title and description for a new todo item, assign it a unique ID, store it in memory, and confirm successful addition.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T009 [P] [US1] Unit test for TodoItem creation in tests/unit/test_todo_item.py
- [X] T010 [P] [US1] Integration test for adding todo via CLI in tests/integration/test_add_todo.py

### Implementation for User Story 1

- [X] T011 [P] [US1] Implement TodoItem constructor with validation in src/models/todo_item.py
- [X] T012 [US1] Implement add_item method in TodoService in src/services/todo_service.py
- [X] T013 [US1] Implement CLI command for adding todo in src/cli/cli_interface.py
- [X] T014 [US1] Connect add command to main application in src/todo_app.py
- [X] T015 [US1] Add logging for add operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - List All Todo Items (Priority: P1)

**Goal**: Enable users to view all their todo items with unique IDs and status indicators

**Independent Test**: The application should display all stored todo items with their unique IDs, titles, descriptions, and completion status in a clear, readable format.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T016 [P] [US2] Unit test for listing todos in tests/unit/test_todo_service.py
- [X] T017 [P] [US2] Integration test for listing todos via CLI in tests/integration/test_list_todos.py

### Implementation for User Story 2

- [X] T018 [P] [US2] Implement list_items method in TodoService in src/services/todo_service.py
- [X] T019 [US2] Implement CLI command for listing todos in src/cli/cli_interface.py
- [X] T020 [US2] Connect list command to main application in src/todo_app.py
- [X] T021 [US2] Add formatting for readable output

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Existing Todo Item (Priority: P2)

**Goal**: Enable users to update an existing todo item's title or description

**Independent Test**: The application should allow a user to select an existing todo item by ID and update its title or description.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T022 [P] [US3] Unit test for updating todos in tests/unit/test_update_todo.py
- [X] T023 [P] [US3] Integration test for updating todos via CLI in tests/integration/test_update_todo.py

### Implementation for User Story 3

- [X] T024 [P] [US3] Implement update_item method in TodoService in src/services/todo_service.py
- [X] T025 [US3] Implement CLI command for updating todo in src/cli/cli_interface.py
- [X] T026 [US3] Connect update command to main application in src/todo_app.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Delete Todo Item by ID (Priority: P2)

**Goal**: Enable users to delete a todo item by its unique ID

**Independent Test**: The application should allow a user to select a todo item by ID and remove it from the list.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T027 [P] [US4] Unit test for deleting todos in tests/unit/test_delete_todo.py
- [X] T028 [P] [US4] Integration test for deleting todos via CLI in tests/integration/test_delete_todo.py

### Implementation for User Story 4

- [X] T029 [P] [US4] Implement delete_item method in TodoService in src/services/todo_service.py
- [X] T030 [US4] Implement CLI command for deleting todo in src/cli/cli_interface.py
- [X] T031 [US4] Connect delete command to main application in src/todo_app.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Mark Todo Item Complete/Incomplete (Priority: P1)

**Goal**: Enable users to mark a todo item as complete or incomplete by ID

**Independent Test**: The application should allow a user to toggle the completion status of a todo item by its ID.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T032 [P] [US5] Unit test for toggling completion status in tests/unit/test_mark_todo.py
- [X] T033 [P] [US5] Integration test for marking todos complete/incomplete via CLI in tests/integration/test_mark_todo.py

### Implementation for User Story 5

- [X] T034 [P] [US5] Implement mark_complete and mark_incomplete methods in TodoService in src/services/todo_service.py
- [X] T035 [US5] Implement CLI commands for marking complete/incomplete in src/cli/cli_interface.py
- [X] T036 [US5] Connect mark commands to main application in src/todo_app.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T037 [P] Documentation updates in README.md
- [X] T038 Code cleanup and refactoring
- [X] T039 Performance optimization across all stories
- [X] T040 [P] Additional unit tests (if requested) in tests/unit/
- [X] T041 Security hardening
- [X] T042 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for TodoItem creation in tests/unit/test_todo_item.py"
Task: "Integration test for adding todo via CLI in tests/integration/test_add_todo.py"

# Launch all models for User Story 1 together:
Task: "Implement TodoItem constructor with validation in src/models/todo_item.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence