"""
Test script to run the todo application
"""
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the main function
from todo_app import main

if __name__ == "__main__":
    print("Attempting to run the todo application...")
    try:
        # Call main without any arguments to trigger help
        import sys
        original_argv = sys.argv[:]
        sys.argv = ['todo_app', '--help']  # Adding help argument to see if it works
        try:
            main()
        except SystemExit:
            # This is expected when help is printed
            print("Application help displayed successfully!")
    except Exception as e:
        print(f"Error running application: {e}")
        import traceback
        traceback.print_exc()
    finally:
        sys.argv = original_argv