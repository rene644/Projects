import shutil
import os

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"File moved from {source} to {destination}")
    except FileNotFoundError:
        print(f"Error: Source file '{source}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{source} or '{destination}'.")
    except Exception as e:
        print(f"Error moving file: {e}")

move_file(r"C:\Users\renem\Documents\Python with AI\python_projects\python_projects\Function_to_Move_Files.py", r"C:\Users\renem\Pictures\Screenshots")