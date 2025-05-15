# importing the organize function
from core.organizer import organize_folder
# importing the loading settings function from utils
from core.utils import load_settings
import time
import schedule #type: ignore

# loading the settings and getting file types from it
settings = load_settings("config/settings.yaml")
# storing the file types
file_types = settings["file_types"]

# making sure that it will execute only if run directly 
if __name__ == "__main__":
    # accepting user folder path
    folder_name = input("Enter folder path to organize:")
    # removing any white spaces
    folder_name = folder_name.strip()

    #starting the organization process
    # organize_folder(folder_name,file_type)
    schedule.every(1).minutes.do(organize_folder,folder=folder_name,file_types=file_types)
    print("scheduler have starte press CTRL + C to stop")

    while True:
        schedule.run_pending()
        time.sleep(1)





