import os

def getProjectFiles(path):
    file_paths_with_folder = []
    for current_dir, folders, files in os.walk(path):
        folder_name = os.path.basename(current_dir)
        for file_name in files:
            full_path = os.path.join(current_dir, file_name)
            path_with_folder = f"{folder_name} - {full_path}"
            file_paths_with_folder.append(path_with_folder)

    return file_paths_with_folder

# Specify the path of the directory you want to explore
directory_to_explore = 'prueba'

# Call the function and get the list of file paths with folder
paths_in_directory_with_folder = getProjectFiles(directory_to_explore)

# Print the list of file paths with folder
for path_with_folder in paths_in_directory_with_folder:
    print(path_with_folder)


