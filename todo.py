"""CLI Todo List Application

A simple command-line todo list manager for learning Git and GitHub.

Usage:
    python todo.py add "Buy groceries"
    python todo.py list
    python todo.py done 1
    python todo.py delete 1
"""

import json
import sys
import os
from datetime import datetime

DATA_FILE = "todos.json"


def load_todos():
    """Load todos from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_todos(todos):
    """Save todos to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def add_todo(title):
    """Add a new todo item."""
    todos = load_todos()
    todo = {
        "id": len(todos) + 1,
        "title": title,
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✓ Added: {title}")


def list_todos():
    """List all todo items."""
    todos = load_todos()
    if not todos:
        print("No todos yet. Add one with: python todo.py add 'your task'")
        return
    
    print("\nYour Todos:")
    print("-" * 40)
    for todo in todos:
        status = "✓" if todo["completed"] else "○"
        print(f"  {status} {todo['id']}. {todo['title']}")
    print()


def mark_done(todo_id):
    """Mark a todo as completed."""
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = True
            save_todos(todos)
            print(f"✓ Completed: {todo['title']}")
            return
    print(f"✗ Todo with ID {todo_id} not found")


def delete_todo(todo_id):
    """Delete a todo item."""
    todos = load_todos()
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted = todos.pop(i)
            # Reassign IDs
            for idx, t in enumerate(todos, 1):
                t["id"] = idx
            save_todos(todos)
            print(f"✓ Deleted: {deleted['title']}")
            return
    print(f"✗ Todo with ID {todo_id} not found")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python todo.py add 'your task'")
            sys.exit(1)
        add_todo(sys.argv[2])
    
    elif command == "list":
        list_todos()
    
    elif command == "done":
        if len(sys.argv) < 3:
            print("Usage: python todo.py done <id>")
            sys.exit(1)
        try:
            mark_done(int(sys.argv[2]))
        except ValueError:
            print("Error: ID must be a number")
            sys.exit(1)
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python todo.py delete <id>")
            sys.exit(1)
        try:
            delete_todo(int(sys.argv[2]))
        except ValueError:
            print("Error: ID must be a number")
            sys.exit(1)
    
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
