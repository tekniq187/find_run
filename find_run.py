import subprocess
import os

# Define a dictionary of file extensions and corresponding commands to run the files
commands = {
    ".py": ["python"],    # For Python files, run using the Python interpreter
    ".js": ["node"],      # For JavaScript files, run using the Node.js interpreter
    ".sh": ["bash"],      # For shell script files, run using the Bash shell
    ".html": ["open"]     # For HTML files, open them in the default web browser
}

# Prompt the user to enter the filename to run
filename = input("Enter the filename to run: ")

# Search for the file in the current directory and subdirectories
for root, dirs, files in os.walk("."):
    if filename in files:
        file_path = os.path.join(root, filename)
        ext = os.path.splitext(filename)[1]
        if ext in commands:
            command = commands[ext] + [file_path]  # Construct the command to run the file
            subprocess.run(command)  # Execute the command
            break
else:
    print(f"Error: file {filename} not found in current directory or subdirectories")
