import os 
import sys
import dill
  
import numpy as np
import pandas as pd

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        # Extract the directory path from the file path
        dir_path = os.path.dirname(file_path)

        # Create the directory if it does not exist
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        # Open the file in binary write mode and save the object
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)