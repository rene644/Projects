import shutil
import os

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File copied from {source} to {destination}")
    except FileNotFoundError:
        print(f"Error: Source file '{source}' not found.")
    except Exception as e:
        print(f"Error copying file: {e}")

# Example usage:
copy_file(r"C:\Users\renem\Documents\Python with AI\python_projects\python_projects\functions_for_automation_tasks.py", r"C:\Users\renem\Pictures\Screenshots") # r prefix added