# smart_file_organizer_version1
Smart File Organizer v1 is a Python-based tool that automatically sorts and organizes files in a specified folder based on their file types (e.g., images, documents, videos). It offers both a command-line automated scheduler and a user-friendly GUI.

Features

  - Automatically organizes files every few minutes (configurable).

  - Smart sorting based on file extensions (e.g., .jpg, .pdf, .mp4, etc.).

  - Customizable categories and paths via settings.yaml.

  - Graphical User Interface (GUI) for manual file organization.

  - Clean and minimal project structure.

Project Structure

    smart-file-organizer/
    ├── core/
    │   ├── organizer.py        # Main sorting logic
    │   └── utils.py            # Helper functions (e.g., get_extension_type)
    ├── config/
    │   └── settings.yaml       # Optional: define folder paths and categories
    ├── main.py                 # CLI version with scheduler (runs every X minutes)
    ├── gui_main.py             # GUI version (user-controlled interface)

How It Works

    main.py:
    Monitors a folder and sorts files into categories (e.g., Images, Documents) every few minutes using a scheduler.

    gui_main.py:
    Provides a graphical interface for manual sorting. It does not run on a schedule—it waits for user input.

    organizer.py:
    Contains the logic to determine the type of each file and move it to the appropriate folder.

    utils.py:
    Includes helper functions like getting the extension type.

    settings.yaml (optional):
    Lets you define folder paths and customize how file types are categorized.

Install the required dependencies:

  pip install -r requirements.txt

Built With
    Python

    Tkinter (for GUI)

    PyYAML (for config)

    schedule (for background job)

Author
    SULAIMAN SALEH YAHAYA
    https://github.com/sumanc99| https://www.linkedin.com/in/sulaiman-saleh-yahaya-maidoya-849b88299/