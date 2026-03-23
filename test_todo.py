"""Tests for the todo.py application."""

import unittest
import json
import os
import tempfile
import todo


class TestTodoApp(unittest.TestCase):
    """Test cases for the Todo List application."""
    
    def setUp(self):
        """Create a temporary file for testing."""
        self.test_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.test_file.close()
        # Save original data file
        self.original_data_file = todo.DATA_FILE
        todo.DATA_FILE = self.test_file.name
    
    def tearDown(self):
        """Clean up temporary files."""
        todo.DATA_FILE = self.original_data_file
        if os.path.exists(self.test_file.name):
            os.unlink(self.test_file.name)
    
    def test_add_todo(self):
        """Test adding a todo item."""
        todo.add_todo("Test task")
        todos = todo.load_todos()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]["title"], "Test task")
        self.assertFalse(todos[0]["completed"])
    
    def test_mark_done(self):
        """Test marking a todo as completed."""
        todo.add_todo("Test task")
        todo.mark_done(1)
        todos = todo.load_todos()
        self.assertTrue(todos[0]["completed"])
    
    def test_delete_todo(self):
        """Test deleting a todo item."""
        todo.add_todo("Task 1")
        todo.add_todo("Task 2")
        todo.delete_todo(1)
        todos = todo.load_todos()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]["title"], "Task 2")
        self.assertEqual(todos[0]["id"], 1)


if __name__ == "__main__":
    unittest.main()
