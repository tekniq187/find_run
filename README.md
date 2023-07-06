# find_run
Run File, it searches directory and subdirectory and runs the code. py, js, sh, html

The code  provided is a Python script that allows you to run different types of files based on their extensions. It prompts the user to enter a filename, searches for the file in the current directory and subdirectories, and then runs the file using the appropriate command based on its extension.
Here's a breakdown of how the code works:

    It imports the subprocess and os modules, which are used for running commands and interacting with the operating system, respectively.
    It defines a dictionary called commands that maps file extensions to the corresponding commands needed to run those files.
    It prompts the user to enter the filename they want to run.
    It searches for the file in the current directory and subdirectories using the os.walk() function.
    If the file is found, it constructs the command to run the file based on its extension and the corresponding command from the commands dictionary.
    It uses the subprocess.run() function to execute the command and run the file.
    If the file is not found, it prints an error message.

Please note that this code assumes that the necessary interpreters or programs are installed on the system for running the different types of files.
