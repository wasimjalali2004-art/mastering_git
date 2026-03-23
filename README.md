# Todo CLI App - Learn Git & GitHub

A simple command-line todo list application designed for learning Git and GitHub fundamentals.

## Quick Start

```bash
# Add a todo
python todo.py add "Buy groceries"

# List all todos
python todo.py list

# Mark todo as complete
python todo.py done 1

# Delete a todo
python todo.py delete 1

# Run tests
python -m unittest test_todo.py
```

## Git Learning Roadmap

### Exercise 1: Initial Setup
```bash
# Initialize git repo
git init

# Check status
git status

# Stage files
git add .

# First commit
git commit -m "Initial commit: Add basic todo CLI app"
```

### Exercise 2: Create a Branch & Add Feature
```bash
# Create and switch to new branch
git checkout -b feature/priority

# Edit todo.py to add priority levels (High/Medium/Low)
# After making changes:
git add todo.py
git commit -m "Add priority levels to todos"

# Switch back to main
git checkout main

# Merge your feature
git merge feature/priority
```

### Exercise 3: Push to GitHub
```bash
# Create repo on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/todo-cli.git
git branch -M main
git push -u origin main
```

### Exercise 4: Pull Requests (on GitHub)
1. Create a new branch: `git checkout -b feature/due-dates`
2. Add due date functionality
3. Push branch: `git push origin feature/due-dates`
4. Open Pull Request on GitHub
5. Review and merge

### Exercise 5: Handling Conflicts
1. Create two branches from main
2. Modify the same line in both
3. Try merging - resolve the conflict
4. Use `git log --oneline --graph` to visualize

## Feature Ideas to Practice Git

- **Add categories/tags** to todos
- **Add due dates** with reminders
- **Add search/filter** functionality  
- **Add export** to CSV/JSON
- **Add statistics** (completion rate, etc.)
- **Add color output** for better UX
- **Add undo functionality**

## Common Git Commands Cheat Sheet

| Command | Description |
|---------|-------------|
| `git status` | Check current state |
| `git add <file>` | Stage changes |
| `git commit -m "msg"` | Save changes |
| `git log --oneline` | View commit history |
| `git branch` | List branches |
| `git checkout -b <name>` | Create & switch branch |
| `git merge <branch>` | Merge branch into current |
| `git push` | Push to remote |
| `git pull` | Fetch and merge from remote |
| `git diff` | See uncommitted changes |

## Next Steps

1. Set up a GitHub account
2. Create a repository on GitHub
3. Connect your local repo
4. Make regular commits as you add features
5. Try collaborating with a friend (fork/PR workflow)
