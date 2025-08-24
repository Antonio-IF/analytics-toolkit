import kagglehub
import shutil
import os

def kaggle_dataset(path_name,dest_path): 
    path = kagglehub.dataset_download(path_name)
    for file_name in os.listdir(path):
        full_file_name = os.path.join(path, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_path)
    return print("Files copy complete on:", dest_path)

kaggle_dataset("adilshamim8/predict-calorie-expenditure", "data/raw/calories-expenditure")
