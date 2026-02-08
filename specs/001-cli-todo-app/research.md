# Research: CLI Todo Application

**Feature**: 001-cli-todo-app
**Date**: 2026-02-08

## Decision: CLI Framework Choice
**Rationale**: For a simple CLI application with no external dependencies required, Python's built-in `argparse` module is ideal. It's part of the standard library, well-documented, and provides all necessary functionality for command parsing.
**Alternatives considered**: 
- Click: More feature-rich but introduces external dependency (against constraints)
- Plain sys.argv: Less structured, more error-prone

## Decision: In-Memory Data Structure
**Rationale**: Using a Python dictionary with integer keys for IDs and TodoItem objects as values provides O(1) lookup by ID and is simple to implement. This meets the in-memory storage requirement without complexity.
**Alternatives considered**:
- List of objects: Would require iteration for ID lookups (O(n))
- Dedicated in-memory database: Overkill for this simple application

## Decision: Unique ID Generation
**Rationale**: Using a simple counter that increments with each new item ensures uniqueness and is efficient. Starting from 1 and incrementing guarantees no collisions.
**Alternatives considered**:
- UUIDs: Would work but are overkill for a single-user application
- Random numbers: Risk of collisions

## Decision: Application State Management
**Rationale**: Using a single TodoService class to manage the collection of todo items provides a clean separation of concerns and encapsulates all business logic related to todo management.
**Alternatives considered**:
- Global variables: Poor practice, harder to test
- Multiple service classes: Unnecessary complexity for this scope

## Decision: Error Handling Approach
**Rationale**: Using Python exceptions for error conditions (e.g., item not found) and catching them at the CLI layer allows for clean separation of business logic from presentation concerns while providing clear feedback to users.
**Alternatives considered**:
- Return error codes: Less Pythonic, more complex to handle
- Print errors directly from business logic: Violates separation of concerns