# 📡 Extractor de Imágenes Satelitales Minagri - Región La Libertad

Este repositorio contiene scripts automatizados para gestionar imágenes satelitales del Ministerio de Agricultura (MINAGRI) de Perú, específicamente enfocados en la región La Libertad:

1. 📥 **Descargar** mosaicos satelitales desde el portal web de MINAGRI
2. ☁️ **Subir** imágenes extraídas a Google Drive
3. ✅ **Verificar** imágenes faltantes o sobrantes en cada carpeta
4. 🗃️ **Organizar** moviendo archivos inesperados o duplicados a carpetas separadas

## 📋 Estructura del Proyecto

```
minagri_satelital_libertad/
│
├── data/                            # Imágenes descargadas y extraídas
│   ├── ENERO_2024/
│   ├── FEBRERO_2024/
│   └── ...
│
├── referencias/               
│   ├── coordenadas.xlsx       # Coordenadas y cuadrantes
│   └── mapa_cuadrantes.png    
├── src/                            # Código fuente organizado por tarea
│   ├── extract_images.py           # Descarga imágenes satelitales del portal MINAGRI
│   ├── upload_drive.py             # Sube archivos TIF a Google Drive
│   ├── verify_images.py            # Verifica que los códigos de imagen esperados estén presentes
│   ├── move_unexpected.py          # Procesa códigos de imagen inesperados
│
├── logs/                           # Registros de ejecución y errores
│
├── .gitignore                      # Ignora archivos grandes y credenciales
├── requirements.txt                # Bibliotecas requeridas
└── README.md                       # Documentación del proyecto
```

## 🛠️ Configuración e Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/minagri_satelital_libertad.git
   cd minagri_satelital_libertad
   ```

2. Instala las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura las credenciales de la API de Google Drive:
   - Descarga tu `client_secret.json` desde Google Cloud Console
   - Colócalo en una ubicación segura referenciada en los scripts

## 📋 Requisitos

- Python 3.7+
- Navegador Chrome (para Selenium)
- Cuenta de Google Drive con almacenamiento suficiente
- Resolución de pantalla estable (los scripts utilizan PyAutoGUI)

## 🚀 Uso

### 1. Extraer imágenes satelitales

```bash
python src/extract_images.py
```

Este script automatiza:
- Navegación al portal geoespacial de MINAGRI
- Selección de períodos de tiempo (mes/año)
- Clic en coordenadas predefinidas para descargar mosaicos de imágenes
- Guardado de archivos zip descargados en carpetas organizadas

### 2. Subir a Google Drive 

```bash
python src/upload_drive.py
```

Características:
- Autenticación con Google Drive
- Creación de estructura de carpetas organizadas por año y mes
- Extracción de archivos TIF de los ZIPs descargados
- Carga de archivos con nombres apropiados

### 3. Verificar integridad de imágenes

```bash
python src/verify_images.py
```

Este script:
- Verifica cada carpeta mensual contra una lista predefinida de códigos de imagen esperados
- Informa sobre códigos de imagen faltantes o inesperados
- Proporciona estadísticas resumidas

### 4. Procesar archivos inesperados

```bash
python src/move_unexpected.py
```

Funcionalidad:
- Identifica archivos con códigos inesperados o duplicados
- Mueve estos archivos a una subcarpeta para revisión manual
- Registra todos los archivos movidos

## 🗂️ Sistema de Códigos de Imagen

El proyecto gestiona mosaicos de imágenes satelitales utilizando un sistema de códigos estandarizado:
- Formato: `IRCXXXX` (ej., IRC2208)
- 187 códigos únicos que representan coordenadas geográficas específicas
- Las imágenes siguen el patrón de nomenclatura: `PLANET_IR:CXXXX_MES_AÑO`

## ⚠️ Notas Importantes

- El script de extracción utiliza PyAutoGUI, así que no muevas el mouse durante la ejecución
- La resolución de pantalla debe coincidir con lo que espera el script (predeterminado: 1366x768)
- Evita interrumpir el proceso de automatización de Chrome
- Excluidos de git: archivos de imagen (.tif, .zip), credenciales, registros

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## 👥 Colaboradores

- [Tu Nombre] - Trabajo inicial y desarrollo
