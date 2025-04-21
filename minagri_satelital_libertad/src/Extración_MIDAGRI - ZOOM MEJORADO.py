# %%
## Instalar las siguientes liberías si hacen falta:

#!pip install selenium pyautogui pydrive oauth2client
#!pip install webdriver-manager

# %%
import pyautogui

ancho, alto = pyautogui.size()
print(f"Resolución de pantalla: {ancho} x {alto}")

# %%


# %%
## Llamamos a las librerías y sus funciones
import os
import time
import re
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# %%
import os
import time
import re
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# %% [markdown]
# *Proceso de extrasión de los datos*

# %%
# Lista de meses y años a descargar
MESES_ANIOS = [
    ("ENERO", "2024"),
    ("FEBRERO", "2024"),
    ("MARZO", "2024"),
    ("ABRIL", "2024"),
    ("MAYO", "2024"),
    ("JUNIO", "2024"),
    ("JULIO", "2024"),
    ("AGOSTO", "2024"), 
    ("SETIEMBRE", "2024"),
    ("OCTUBRE", "2024"),
    ("NOVIEMBRE", "2024"),
    ("DICIEMBRE", "2024")
]

zoom_realizado = False  # Para hacer zoom solo una vez

# Iteración sobre cada mes y año
for mes, anio in MESES_ANIOS:
    # Definir carpetas de descarga y extracción
    download_folder = fr"C:\Users\Public\Downloads\{mes}_{anio}"
    extract_folder = fr"C:\Users\Public\Downloads\{mes}_{anio}_EXTRAIDO"

    # Crear carpetas si no existen
    os.makedirs(download_folder, exist_ok=True)
    os.makedirs(extract_folder, exist_ok=True)

    # Configurar opciones de Chrome
    chrome_options = Options()
    prefs = {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "safebrowsing.disable_download_protection": True,
        "profile.default_content_setting_values.automatic_downloads": 1,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Usar WebDriver Manager para gestionar ChromeDriver automáticamente
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Maximizar ventana y acceder al sitio web
    driver.maximize_window()
    driver.get("https://minagri-geoespacial.users.earthengine.app/view/mosaicosv3")
    
    wait = WebDriverWait(driver, 20)

    # Acercar pantalla solo una vez con doble doble clic
    if not zoom_realizado:
        time.sleep(10)  # Esperar a que cargue completamente el mapa
        pyautogui.moveTo(694, 408, duration=0.5)
        pyautogui.doubleClick()
        time.sleep(5)
        pyautogui.moveTo(694, 408, duration=0.5)
        pyautogui.doubleClick()
        zoom_realizado = False
        time.sleep(10)
    
        # Check Cuadrantes    
        try:
            # Esperar a que el checkbox de "Cuadrantes" esté presente
            wait = WebDriverWait(driver, 15)
            
            # Buscar el checkbox que está asociado al label "Cuadrantes"
            checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='label' and text()='Cuadrantes']/preceding-sibling::span[contains(@class, 'jfk-checkbox')]")))
            
            # Hacer clic en el checkbox
            checkbox.click()
            print("Checkbox de 'Cuadrantes' seleccionado correctamente.")
    
        except Exception as e:
            print(f"Error al hacer clic en el checkbox: {e}")
    
        # Seleccionar Mes y Año
        try:
            wait = WebDriverWait(driver, 10)
            boton_seleccionar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "jfk-select")))
            boton_seleccionar.click()
            
            wait.until(EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, "jfk-select"), "aria-expanded", "true"))
            opcion = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{mes}_{anio}')]")))
            opcion.click()
            print(f"Seleccionado {mes}_{anio} correctamente.")
        except Exception as e:
            print(f"Error al seleccionar la opción: {e}")
    
        time.sleep(5)
    
        # Check Cuadrantes    
        try:
            # Esperar a que el checkbox de "Cuadrantes" esté presente
            wait = WebDriverWait(driver, 10)
            
            # Buscar el checkbox que está asociado al label "Cuadrantes"
            checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='label' and text()='Cuadrantes']/preceding-sibling::span[contains(@class, 'jfk-checkbox')]")))
            
            # Hacer clic en el checkbox
            checkbox.click()
            print("Checkbox de 'Cuadrantes' seleccionado correctamente.")
    
        except Exception as e:
            print(f"Error al hacer clic en el checkbox: {e}")
    
        # Check Cuadrantes    
        try:
            # Esperar a que el checkbox de "Cuadrantes" esté presente
            wait = WebDriverWait(driver, 10)
            
            # Buscar el checkbox que está asociado al label "Cuadrantes"
            checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='label' and text()='Cuadrantes']/preceding-sibling::span[contains(@class, 'jfk-checkbox')]")))
            
            # Hacer clic en el checkbox
            checkbox.click()
            print("Checkbox de 'Cuadrantes' seleccionado correctamente.")
    
        except Exception as e:
            print(f"Error al hacer clic en el checkbox: {e}")
    
        time.sleep(10)
    
        # Expresión regular para encontrar el enlace
        pattern = re.compile(fr"PLANET_IR:C\d{{4}}_{mes}_{anio}")
    
        coordenadas = [
        (471, 262),  # IRC2208 (N° 3)
        (471, 332),  # IRC2205 (N° 6)
        (472, 356),  # IRC2204 (N° 7)
        (520, 263),  # IRC2510 (N° 17)
        (564, 355),  # IRC2808 (N° 33)
        (611, 583),  # IRC3100 (N° 60)
        (610, 333),  # IRC3111 (N° 49)
        (632, 608),  # IRC3250 (N° 73)
        (632, 561),  # IRC3252 (N° 71)
        (633, 539),  # IRC3253 (N° 70)
        (632, 332),  # IRC3262 (N° 61)
        (631, 630),  # IRC3249 (N° 74)
        (655, 355),  # IRC3412 (N° 75)
        (769, 492),  # IRC4161 (N° 133)
        (771, 469),  # IRC4162 (N° 132)
        (770, 444),  # IRC4163 (N° 131)
        (770, 422),  # IRC4164 (N° 130)
        (770, 403),  # IRC4165 (N° 129)
        (771, 379),  # IRC4166 (N° 128)
        (768, 309),  # IRC4169 (N° 127)
        (767, 284),  # IRC4170 (N° 126)
        (768, 263),  # IRC4171 (N° 125)
        (792, 356),  # IRC4318 (N° 138)
        (792, 333),  # IRC4319 (N° 137)
        (838, 491),  # IRC4614 (N° 161)
        (862, 538),  # IRC4763 (N° 169)
        (863, 514),  # IRC4764 (N° 168)
        (907, 537),  # IRC5065 (N° 179)
        (931, 536),  # IRC5216 (N° 184)
        (930, 512),  # IRC5217 (N° 183)
        (930, 493),  # IRC5218 (N° 182)
        (929, 467),  # IRC5219 (N° 181)
        (928, 446),  # IRC5220 (N° 180)
        (954, 513),  # IRC5368 (N° 187)
        (954, 490),  # IRC5369 (N° 186)
        (952, 470),  # IRC5370 (N° 185)
        ]		
    
        for x, y in coordenadas:
            # Mueve el cursor y hace clic en las nuevas coordenadas
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
            
            # Espera para que la página cargue el nuevo enlace
            time.sleep(30)
    
            try:
                # Buscar todos los enlaces en la página
                links = driver.find_elements(By.TAG_NAME, "a")
                
                # Filtrar los enlaces que coincidan con el patrón
                for link in links:
                    if pattern.match(link.text):
                        ActionChains(driver).move_to_element(link).click().perform()
                        print(f"Se hizo clic en el enlace: {link.text} en las coordenadas ({x}, {y}).")
                        break  # Salir del bucle una vez encontrado el enlace correcto
                else:
                    print(f"No se encontró un enlace con el formato esperado en ({x}, {y}).")
    
            except Exception as e:
                print(f"Error al hacer clic en el enlace en ({x}, {y}):", e)
    
            # Espera para que la descarga inicie
            time.sleep(30)

    # Espera un momento antes de cerrar el navegador
    time.sleep(5)

    # Cerrar el navegador
    driver.quit()
    print("Navegador cerrado exitosamente.")

# %%


# %%



