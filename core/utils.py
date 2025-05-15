# to work with yaml files
import yaml # type: ignore
# Object-oriented path manipulation that works across different operating systems
from pathlib import Path

#loading the settings 
def load_settings(path="../config/settings.yaml"):

    with open(path,"r") as file:
        return yaml.safe_load(file)
    


# using the extension of file it get it category
def get_category(extension,file_types):

    for category,extensions in file_types.items():
        if extension.lower() in extensions:
            return category
    return "Others"

