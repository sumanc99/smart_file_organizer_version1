# Provides operating system dependent functionality (file paths, environment variables, etc.)
import os
# Offers high-level file operations (copying, moving, archiving entire directories)
import shutil
# Object-oriented path manipulation that works across different operating systems
from pathlib import Path
# importing the settings and method for finding catergorys
from core.utils import get_category




# using the given folder path it look in it and organize the content
def organize_folder(folder,file_types):
    # hold the folder path 
    target = Path(folder)

    # going through the folder
    for item in target.iterdir():
        # cehcking if item is a file not folder
        if item.is_file():
            # holding the file extension
            ext = item.suffix

            # getting the category of each file
            category = get_category(ext,file_types)

            # create file path
            destination = target/category

            # checking if catergory folder exist if yes do not create if no create
            destination.mkdir(exist_ok=True)

            # protecting the program in case of crash
            try:
                # moving the file to new folder
                shutil.move(item, destination/item.name)
                print(f"Move {item.name} to {category}")
            except Exception as e:
                print(f"Faile to Move {item.name}:{e}")
