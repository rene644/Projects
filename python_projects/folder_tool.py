import os

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            name, extension = os.path.splitext(filename)
            extension = extension[1:]  # Remove the leading dot

            if extension:  # Check if there's an extension
                folder_path = os.path.join(directory, extension)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                source_path = os.path.join(directory, filename)
                destination_path = os.path.join(folder_path, filename)
                os.rename(source_path, destination_path)

# Example usage:
directory_to_organize = r"c:\Users\renem\Documents"
organize_files(directory_to_organize)