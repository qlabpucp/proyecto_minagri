# %%
!pip install PyDrive

# %%
#Importamos de la libreria
import os
import glob
import zipfile
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# %%
# Carpeta raíz en Google Drive
ROOT_FOLDER_ID = "1YcehIRJyA8z0N8d8cb0HCZcEZMKxzc4J"  # ID de la carpeta principal en Drive

#Función para autenticar con Google Drive
def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(r"D:\Users\u_sociales\Desktop\Extracción MINAGRI\client_secret_479070046140-73lf85vftkp4mp69edh0pa0rchp54ga1.apps.googleusercontent.com.json")  
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

drive = authenticate_drive()

# %%
#Listas de meses y año a iterar
ANIOS_DISPONIBLES = ["2021", "2022", "2023", "2024","2025"]
MESES = {
    "01": "ENERO",
    "02": "FEBRERO"
    "03": "MARZO"
    "04": "ABRIL"
    "05": "MAYO",
    "06": "JUNIO"
    "07": "JULIO"
    "08": "AGOSTO"
    "09": "SEPTIEMBRE"
    "10": "OCTUBRE"
    "11": "NOVIEMBRE"
    "12": "DICIEMBRE"
    }

ROOT_FOLDER_ID = "1plTbfdcORgnF1ECWN7RgMD5tUeBHoYw5" # ID de la carpeta principal en Drive


# %%
#Selección del año por el usuario
anio_usuario = input(f"Ingrese el año a procesar ({', '.join(ANIOS_DISPONIBLES)}): ")

if anio_usuario not in ANIOS_DISPONIBLES:
    print(f"⚠️ Año inválido. Debe ser uno de: {', '.join(ANIOS_DISPONIBLES)}")
    exit()

# %%
#Crear carpetas en Google Drive
def get_or_create_folder(drive, folder_name, parent_id):
    query = f"title = '{folder_name}' and '{parent_id}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    folder_list = drive.ListFile({'q': query}).GetList()
    if folder_list:
        return folder_list[0]['id']
    folder = drive.CreateFile({'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [{'id': parent_id}]})
    folder.Upload()
    return folder['id']

# Extraer archivos .tif desde zip
def extract_tif_files(download_folder, extract_folder):
    zip_files = glob.glob(os.path.join(download_folder, "*.zip"))
    extracted_tifs = []
    os.makedirs(extract_folder, exist_ok=True)
    
    for zip_file in zip_files:
        try:
            base_name = os.path.basename(zip_file)[:-4]
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                tif_files = [f for f in zip_ref.namelist() if f.lower().endswith('.tif')]
                for tif_file in tif_files:
                    tif_base_name = os.path.basename(tif_file)
                    new_tif_name = f"{base_name}_{tif_base_name}"
                    target_path = os.path.join(extract_folder, new_tif_name)
                    with zip_ref.open(tif_file) as source, open(target_path, "wb") as target:
                        target.write(source.read())
                    extracted_tifs.append(target_path)
        except Exception as e:
            print(f"Error al extraer {zip_file}: {e}")
    return extracted_tifs
    
# Subir archivos a Google Drive
def upload_tifs_to_drive(drive, tif_files, parent_folder_id):
    for tif_path in tif_files:
        file_name = os.path.basename(tif_path)
        file_metadata = {'title': file_name, 'parents': [{'id': parent_folder_id}]}
        file = drive.CreateFile(file_metadata)
        file.SetContentFile(tif_path)
        file.Upload()
        print(f"✅ Archivo subido: {file_name}")
        time.sleep(2)
        
# Bucle principal: Procesar meses del año seleccionado
for mes_num, mes_nombre in MESES.items():
    carpeta_drive = f"{anio_usuario}_{mes_num}"
    
    # Crear carpeta en Drive
    folder_id = get_or_create_folder(drive, carpeta_drive, ROOT_FOLDER_ID)

    # Rutas locales (ajusta si cambian)
    download_folder = fr"D:\Users\u_sociales\Desktop\Extracción MINAGRI\DATOS\{mes_nombre}_{anio_usuario}"
    extract_folder = fr"D:\Users\u_sociales\Desktop\Extracción MINAGRI\DATOS\{mes_nombre}_{anio_usuario}_EXTRAIDO"

    print(f"\n🟡 Procesando {mes_nombre} {anio_usuario}")
    time.sleep(2)

    extracted_tifs = extract_tif_files(download_folder, extract_folder)

    if extracted_tifs:
        print(f"✅ {len(extracted_tifs)} archivos extraídos.")
        upload_tifs_to_drive(drive, extracted_tifs, folder_id)
        print(f"☁️ Archivos subidos a carpeta: {carpeta_drive}")
    else:
        print(f"⚠️ No se encontraron archivos TIF en {mes_nombre} {anio_usuario}.")
    
    time.sleep(5)
    


