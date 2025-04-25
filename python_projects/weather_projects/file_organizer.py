import os
import logging
import sys

CATEGORIES = {
    "Documents": {"docx", "pdf", "txt", "xlsx", "pptx"},
    "Images": {"jpg", "png", "gif", "bmp"},
    "Videos": {"mp4", "mkv", "avi", "mov"},
    "Audio": {"mp3", "wav", "flac"},
    "Archives": {"zip", "rar", "tar.gz"}
}

def get_category(extension):
    """Find the correct category folder for a file extension."""
    if not extension:  # Handle files with no extension
        return "No Extension"  

    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    
    return extension  # Default: Use the extension if no category exists

# Configure logging to write to a file
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def organize_files(directory, dry_run=False):
    """Organizes files into categorized folders. If dry_run=True, only shows actions."""
    
    if not os.path.exists(directory):
        logging.error(f"Directory '{directory}' does not exist.")
        print(f"Error: The directory '{directory}' does not exist.")
        return
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if not os.path.isfile(file_path):
            continue

        _, extension = os.path.splitext(filename)
        extension = extension[1:].lower()  # Remove dot and standardize lowercase

        category = get_category(extension)  
        folder_path = os.path.join(directory, category)  

        if os.path.dirname(file_path) == folder_path:
            continue  # ✅ Works efficiently without redundant processing

        if dry_run:
            logging.info(f"Dry Run: Would move '{filename}' → '{folder_path}/'")
            print(f"Dry Run: Would move '{filename}' → '{folder_path}/'")
            continue  # ✅ Prevents unnecessary execution in dry-run mode
        else:
            os.makedirs(folder_path, exist_ok=True)
            os.rename(file_path, os.path.join(folder_path, filename))
            logging.info(f"Moved: {filename} → {folder_path}/")
    
    print("\n✅ Organizing completed! Check 'log.txt' for details." if not dry_run else "\n✅ Dry-run complete! No actual changes were made.")

# ✅ Ask the user for the folder path **AFTER function definitions**
directory_to_organize = input("Enter the folder path to organize: ").strip()
organize_files(directory_to_organize)
