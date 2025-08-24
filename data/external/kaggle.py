import kagglehub
import shutil
import os

# Descargar dataset (se guarda en un directorio temporal)
path = kagglehub.dataset_download("adilshamim8/predict-calorie-expenditure")

# Definir carpeta destino
dest_path = "data/raw/calories-expenditure"

# Copiar todos los archivos descargados a "data/raw/predict-calorie-expenditure"
for file_name in os.listdir(path):
    full_file_name = os.path.join(path, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest_path)

print("Archivos copiados a:", dest_path)
