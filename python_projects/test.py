import os

def organize_files(directory):
    try:
        for filename in os.listdir(directory):
            try:
                if os.path.isfile(os.path.join(directory, filename)):
                    name, extension = os.path.splitext(filename)  # Corrected line
                    extension = extension[1:]  # Remove the leading dot

                    if extension:
                        folder_path = os.path.join(directory, extension)
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)

                        source_path = os.path.join(directory, filename)
                        destination_path = os.path.join(folder_path, filename)
                        os.rename(source_path, destination_path)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    except FileNotFoundError:
        print(f"Error: Directory 'c:\\Users\\renem\\Documents' not found.")
    except PermissionError:
        print(f"Error: Permission denied to access 'c:\\Users\\renem\\Documents'.") #Removed extra quotes

# Example usage:
directory_to_organize = r"c:\Users\renem\Down"
organize_files(directory_to_organize)