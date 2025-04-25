import os

def delete_file(filepath):
    try:
        os.remove(filepath)
        print(f"File '{filepath}' deleted.")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to delete '{filepath}'.")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Example usage:
delete_file(r"functions_for_automation_tasks.py") # Added parentheses