# ============================================
# TESTS FOR TODO APP - Learning Unit Testing
# ============================================
# This file teaches you how to test your code.
# Testing helps make sure your code works correctly!

# Import the testing tools that come with Python
import unittest

# Import the module we want to test
# (todo.py must be in the same folder)
import todo

# Import tools for file handling
import os
import tempfile


class TestTodoApp(unittest.TestCase):
    """
    A test class contains multiple tests.
    Each test checks one small part of the program.
    
    Think of tests like checking your homework:
    - Did I answer question 1 correctly? (test 1)
    - Did I answer question 2 correctly? (test 2)
    """
    
    def setUp(self):
        """
        setUp runs BEFORE each test.
        We use it to prepare a clean environment.
        
        This teaches: setUp method, temporary files
        """
        # Create a temporary file (like a scratch paper)
        # This file will be deleted after the test
        self.test_file = tempfile.NamedTemporaryFile(
            mode='w',     # Open in write mode
            delete=False, # Don't auto-delete (we'll clean up manually)
            suffix='.json' # File extension
        )
        self.test_file.close()  # Close the file so we can use it
        
        # Save the original data file name
        # So we can restore it later
        self.original_data_file = todo.DATA_FILE
        
        # Tell todo.py to use our test file instead
        todo.DATA_FILE = self.test_file.name
    
    def tearDown(self):
        """
        tearDown runs AFTER each test.
        We use it to clean up and restore things.
        
        This teaches: tearDown method, cleanup
        """
        # Restore the original data file
        todo.DATA_FILE = self.original_data_file
        
        # Delete our temporary test file
        if os.path.exists(self.test_file.name):
            os.unlink(self.test_file.name)  # unlink = delete file
    
    def test_add_todo(self):
        """
        Test: Can we add a new todo?
        
        What we check:
        - After adding, the list has 1 item
        - The title matches what we added
        - It's not completed yet
        """
        # Add a todo
        todo.add_todo("Test task")
        
        # Get the list of todos
        todos = todo.load_todos()
        
        # Check 1: List should have 1 item
        # len() gives us the count of items
        self.assertEqual(len(todos), 1)
        
        # Check 2: The title should be "Test task"
        # todos[0] means "first item in the list"
        self.assertEqual(todos[0]["title"], "Test task")
        
        # Check 3: Completed should be False
        # False means "not done yet"
        self.assertFalse(todos[0]["completed"])
    
    def test_mark_done(self):
        """
        Test: Can we mark a todo as done?
        
        What we check:
        - After marking done, completed is True
        """
        # First, add a todo
        todo.add_todo("Test task")
        
        # Mark it as done (ID is 1 for first item)
        todo.mark_done(1)
        
        # Get the updated list
        todos = todo.load_todos()
        
        # Check: completed should now be True
        # True means "done!"
        self.assertTrue(todos[0]["completed"])
    
    def test_delete_todo(self):
        """
        Test: Can we delete a todo?
        
        What we check:
        - After deleting, list has 1 item (not 2)
        - The remaining item is the second one we added
        - The ID is fixed to be 1 (not 2)
        """
        # Add two todos
        todo.add_todo("Task 1")  # ID will be 1
        todo.add_todo("Task 2")  # ID will be 2
        
        # Delete the first one (ID 1)
        todo.delete_todo(1)
        
        # Get the updated list
        todos = todo.load_todos()
        
        # Check 1: List should have 1 item left
        self.assertEqual(len(todos), 1)
        
        # Check 2: The remaining item should be "Task 2"
        self.assertEqual(todos[0]["title"], "Task 2")
        
        # Check 3: The ID should be fixed to 1 (not 2)
        # We renumber IDs after deletion
        self.assertEqual(todos[0]["id"], 1)


# ============================================
# HOW TO RUN THESE TESTS
# ============================================
# 
# In the terminal, type:
#     python -m unittest test_todo.py
# 
# You'll see something like:
#     ...
#     Ran 3 tests in 0.001s
#     OK
# 
# Each dot (.) means one test passed!
# 
# If a test fails, you'll see:
#     F
#     FAILED (failures=1)
#     And details about what went wrong

if __name__ == "__main__":
    # This runs all the tests when you run the file directly
    unittest.main()
