# Python Todo App - Beginner Friendly! 🐍

Welcome! This is a simple todo list app made for **learning Python fundamentals**.

## What You'll Learn

By building and using this app, you'll learn:

- **Variables** - Storing data (like your todo list)
- **Functions** - Reusable blocks of code
- **Lists & Dictionaries** - Organizing multiple items
- **If-Else Statements** - Making decisions in code
- **For Loops** - Repeating actions
- **File I/O** - Saving data to files
- **Testing** - Making sure your code works

## Quick Start

Try these commands in your terminal:

```bash
# 1. Add a todo
python todo.py add "Learn Python"

# 2. See your todos
python todo.py list

# 3. Mark it as done
python todo.py done 1

# 4. Delete it
python todo.py delete 1

# 5. Run the tests
python -m unittest test_todo.py
```

## How The Code Works

### todo.py - The Main Program

Each function does one thing:

| Function | What It Does | Python Concept |
|----------|-------------|----------------|
| `load_todos()` | Reads saved todos from file | File reading, JSON |
| `save_todos()` | Saves todos to file | File writing |
| `add_todo()` | Creates a new todo | Dictionaries, lists |
| `list_todos()` | Shows all todos | For loops, if-else |
| `mark_done()` | Marks a todo complete | Finding items in lists |
| `delete_todo()` | Removes a todo | List operations |
| `main()` | Handles user commands | sys.argv, if-elif |

### test_todo.py - The Tests

Tests check that your code works correctly. Each test:
1. Sets up (creates test data)
2. Runs some code
3. Checks the result

**Example Test Flow:**
```
setUp() → test runs → check results → tearDown()
```

## Learning Path

### Step 1: Understand the Code
- Read `todo.py` line by line
- Each comment explains what the code does
- Try changing small things and see what happens

### Step 2: Run It
```bash
python todo.py help
python todo.py add "My first task"
python todo.py list
```

### Step 3: Run Tests
```bash
python -m unittest test_todo.py
```
Each `.` means a test passed!

### Step 4: Make It Better (Challenges!)

Try adding these features:

**Easy:**
- [ ] Add a `help` command
- [ ] Show how many todos are completed
- [ ] Add colors to the output

**Medium:**
- [ ] Add categories (Work, Home, School)
- [ ] Sort todos alphabetically
- [ ] Add search functionality

**Hard:**
- [ ] Add due dates
- [ ] Add priorities (High/Medium/Low)
- [ ] Export to a text file

## Git Learning (Optional)

Want to learn Git too? Try this:

```bash
# See what files changed
git status

# Save your changes
git add todo.py
git commit -m "Added my first feature!"

# See your history
git log --oneline
```

## Python Concepts Cheat Sheet

### Variables
```python
name = "Alice"      # String (text)
age = 25          # Integer (whole number)
price = 19.99     # Float (decimal)
is_done = False   # Boolean (True/False)
```

### Lists
```python
todos = ["Buy milk", "Walk dog", "Read book"]
print(todos[0])      # First item: "Buy milk"
todos.append("New")  # Add to end
len(todos)           # Count items: 3
```

### Dictionaries
```python
todo = {
    "id": 1,
    "title": "Buy milk",
    "completed": False
}
print(todo["title"])  # "Buy milk"
```

### If-Else
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

### For Loops
```python
for item in todos:
    print(item)
```

### Functions
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Prints: Hello, Alice!
```

## Need Help?

1. Run `python todo.py help` for usage info
2. Read the comments in the code
3. Try the tests to see examples
4. Experiment! You can't break anything.

## Keep Learning!

- **Python docs:** https://docs.python.org/3/tutorial/
- **Practice:** Try the challenges above
- **Share:** Show your modified app to a friend!
