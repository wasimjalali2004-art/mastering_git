# ============================================
# TODO LIST APP - Python Fundamentals Edition
# ============================================
# This is a simple todo list program.
# It helps you learn basic Python concepts while building something useful!

# Import built-in modules (these come with Python)
import json      # For saving/loading data as JSON format
import sys       # For reading command line arguments
import os        # For checking if files exist

# This is the file where we save our todos
DATA_FILE = "todos.json"


def load_todos():
    """
    Read todos from the file and return them as a list.
    If the file doesn't exist yet, return an empty list.
    
    This teaches: file reading, json module, error handling basics
    """
    # Check if the file exists
    if not os.path.exists(DATA_FILE):
        # If file doesn't exist, return empty list
        return []
    
    # Open the file in read mode
    with open(DATA_FILE, "r") as file:
        # Load the JSON data and convert to Python list
        todos = json.load(file)
    
    return todos


def save_todos(todos):
    """
    Save a list of todos to the file.
    
    This teaches: file writing, json module
    """
    # Open file in write mode (this creates it if it doesn't exist)
    with open(DATA_FILE, "w") as file:
        # Convert Python list to JSON and save it
        # indent=2 makes it readable (pretty-printed)
        json.dump(todos, file, indent=2)


def add_todo(title):
    """
    Add a new todo item to the list.
    
    This teaches: functions, lists, dictionaries, variables
    
    Parameters:
        title (string): The task description
    """
    # Step 1: Get the current list of todos
    todos = load_todos()
    
    # Step 2: Create a new todo as a dictionary
    # A dictionary stores key-value pairs
    new_todo = {
        "id": len(todos) + 1,        # ID is the next number (1, 2, 3...)
        "title": title,               # The task description
        "completed": False            # New todos start as not done
    }
    
    # Step 3: Add the new todo to the list
    # append() adds to the end of the list
    todos.append(new_todo)
    
    # Step 4: Save the updated list back to file
    save_todos(todos)
    
    # Step 5: Tell the user what happened
    print(f"✓ Added: {title}")


def list_todos():
    """
    Display all todos in a nice format.
    
    This teaches: loops, if-else, string formatting
    """
    # Get the list of todos
    todos = load_todos()
    
    # Check if the list is empty
    # len() tells us how many items are in the list
    if len(todos) == 0:
        print("Your list is empty!")
        print("Add a todo: python todo.py add 'Buy milk'")
        return
    
    # Print a header
    print("")
    print("YOUR TODO LIST:")
    print("-" * 30)
    
    # Loop through each todo in the list
    # This is a "for loop" - it repeats for each item
    for todo in todos:
        # Check if completed and pick the right symbol
        if todo["completed"]:
            symbol = "✓"  # Checkmark for done
        else:
            symbol = "○"  # Circle for not done
        
        # Print the todo
        # This uses f-strings (formatted strings)
        id_num = todo["id"]
        title = todo["title"]
        print(f"  {symbol} {id_num}. {title}")
    
    print("")


def mark_done(todo_id):
    """
    Mark a todo as completed.
    
    This teaches: loops, conditionals, modifying data
    
    Parameters:
        todo_id (int): The ID number of the todo to complete
    """
    # Get the current list
    todos = load_todos()
    
    # Create a variable to track if we found the todo
    found = False
    
    # Loop through all todos
    for todo in todos:
        # Check if this is the todo we're looking for
        if todo["id"] == todo_id:
            # Mark it as completed
            todo["completed"] = True
            found = True
            
            # Tell the user
            print(f"✓ Completed: {todo['title']}")
            break  # Stop the loop - we found it!
    
    # If we didn't find the todo
    if not found:
        print(f"Sorry, no todo with ID {todo_id}")
        return
    
    # Save the changes
    save_todos(todos)


def delete_todo(todo_id):
    """
    Remove a todo from the list.
    
    This teaches: list operations (remove), loop with index
    
    Parameters:
        todo_id (int): The ID number of the todo to delete
    """
    # Get the current list
    todos = load_todos()
    
    # Create a variable to track if we found it
    found = False
    
    # Loop with index (we need the position to delete)
    # enumerate gives us: index, value
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            # Remove this item from the list
            # pop(index) removes and returns the item at that position
            removed = todos.pop(index)
            found = True
            
            print(f"✓ Deleted: {removed['title']}")
            break
    
    # If we didn't find the todo
    if not found:
        print(f"Sorry, no todo with ID {todo_id}")
        return
    
    # Fix the IDs so they stay in order (1, 2, 3...)
    # Loop through remaining todos and reassign IDs
    for new_index, todo in enumerate(todos, start=1):
        todo["id"] = new_index
    
    # Save the updated list
    save_todos(todos)


def show_help():
    """
    Display help information about how to use the app.
    """
    help_text = """
TODO LIST APP - How to Use
===========================

Add a new task:
    python todo.py add "Buy groceries"

See all tasks:
    python todo.py list

Mark a task as done:
    python todo.py done 1

Delete a task:
    python todo.py delete 1

Help:
    python todo.py help

What you'll learn:
- Functions and how to call them
- Variables and data types
- Lists and dictionaries
- If-else statements
- For loops
- Reading and writing files
    """
    print(help_text)


def main():
    """
    This is the main function that runs when you start the program.
    It reads what command you typed and calls the right function.
    
    This teaches: command line arguments, if-elif-else chains
    """
    # sys.argv is a list of words you typed in the command line
    # Example: python todo.py add "Buy milk"
    # sys.argv[0] = "todo.py"
    # sys.argv[1] = "add"
    # sys.argv[2] = "Buy milk"
    
    # Check if user typed any command
    if len(sys.argv) < 2:
        show_help()
        return
    
    # Get the command (first word after program name)
    command = sys.argv[1]
    
    # Check which command was typed and run the right function
    if command == "add":
        # Check if user gave a task description
        if len(sys.argv) < 3:
            print("Error: Please provide a task")
            print('Example: python todo.py add "Buy milk"')
        else:
            # Get the task description and add it
            task = sys.argv[2]
            add_todo(task)
    
    elif command == "list":
        list_todos()
    
    elif command == "done":
        # Check if user gave an ID number
        if len(sys.argv) < 3:
            print("Error: Please provide a todo number")
            print("Example: python todo.py done 1")
        else:
            # Convert the ID from string to integer
            # int() converts "1" to 1
            try:
                todo_id = int(sys.argv[2])
                mark_done(todo_id)
            except ValueError:
                print("Error: Please use a number")
                print("Example: python todo.py done 1")
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Please provide a todo number")
            print("Example: python todo.py delete 1")
        else:
            try:
                todo_id = int(sys.argv[2])
                delete_todo(todo_id)
            except ValueError:
                print("Error: Please use a number")
                print("Example: python todo.py delete 1")
    
    elif command == "help":
        show_help()
    
    else:
        # Unknown command
        print(f"Unknown command: {command}")
        show_help()


# This is a special Python pattern
# It means: only run main() if this file is run directly
# Don't run main() if this file is imported by another file
if __name__ == "__main__":
    main()
