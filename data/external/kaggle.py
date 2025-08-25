import kagglehub
import shutil
import os

def kaggle_dataset(path_name,dest_path, create_dir=False): 
    """
    Args:
        path_name (str): The name of the dataset on Kaggle to be downloaded, in the format 'username/dataset_name'.
        dest_path (str): The destination path where the downloaded files will be copied.
        create_dir (bool): A flag that determines whether to create the destination directory if it does not exist. 
                           Defaults to False.
    """

    if create_dir:
        os.makedirs(dest_path, exist_ok=True)
    else: 
        if not os.path.exists(dest_path):
            raise FileNotFoundError(f"The dest path in: {dest_path} doesn't exist & create_dir=False")     

    path = kagglehub.dataset_download(path_name)

    for file_name in os.listdir(path):
        full_file_name = os.path.join(path, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_path)
    return print("Files copy complete on:", dest_path)

# Using function......

# 1st Dataset;
# kaggle_dataset("adilshamim8/predict-calorie-expenditure", "data/raw/calories-expenditure")

# 2th DS; 
# kaggle_dataset("yashdevladdha/uber-ride-analytics-dashboard", "data/raw/uber-ride-analytics", create_dir=True)

