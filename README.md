# 📡 Minagri Satellite Image Scraper - La Libertad Region

This repository contains automated scripts for handling satellite imagery from Peru's Ministry of Agriculture (MINAGRI), specifically focused on the La Libertad region:

1. 📥 **Download** satellite mosaics from MINAGRI's web portal
2. ☁️ **Upload** extracted images to Google Drive
3. ✅ **Verify** missing or extra images in each folder
4. 🗃️ **Organize** by moving unexpected or duplicate files to separate folders

## 📋 Project Structure

```
minagri_satelital_libertad/
│
├── data/                            # Downloaded and extracted images
│   ├── ENERO_2024/
│   ├── FEBRERO_2024/
│   └── ...
│
├── src/                            # Source code organized by task
│   ├── extract_images.py           # Download satellite images from MINAGRI portal
│   ├── upload_drive.py             # Upload TIF files to Google Drive
│   ├── verify_images.py            # Verify expected image codes are present
│   ├── move_unexpected.py          # Process unexpected image codes
│
├── logs/                           # Execution and error logs
│
├── .gitignore                      # Ignore large files and credentials
├── requirements.txt                # Required libraries
└── README.md                       # Project documentation
```

## 🛠️ Setup & Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/minagri_satelital_libertad.git
   cd minagri_satelital_libertad
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Google Drive API credentials:
   - Download your `client_secret.json` from Google Cloud Console
   - Place it in a secure location referenced in the scripts

## 📋 Requirements

- Python 3.7+
- Chrome browser (for Selenium)
- Google Drive account with sufficient storage
- Stable screen resolution (scripts use PyAutoGUI)

## 🚀 Usage

### 1. Extract satellite images

```bash
python src/extract_images.py
```

This script automates:
- Navigating to the MINAGRI geospatial portal
- Selecting time periods (month/year)
- Clicking on predefined coordinates to download image tiles
- Saving downloaded zip files to organized folders

### 2. Upload to Google Drive 

```bash
python src/upload_drive.py
```

Features:
- Authenticates with Google Drive
- Creates organized folder structure by year and month
- Extracts TIF files from downloaded ZIPs
- Uploads files with appropriate naming

### 3. Verify image integrity

```bash
python src/verify_images.py
```

This script:
- Checks each monthly folder against a predefined list of expected image codes
- Reports missing or unexpected image codes
- Provides summary statistics

### 4. Process unexpected files

```bash
python src/move_unexpected.py
```

Functionality:
- Identifies files with unexpected codes or duplicates
- Moves these files to a subfolder for manual review
- Logs all moved files

## 🗂️ Image Code System

The project manages satellite image tiles using a standardized code system:
- Format: `IRCXXXX` (e.g., IRC2208)
- 187 unique codes representing specific geographic coordinates
- Images follow naming pattern: `PLANET_IR:CXXXX_MONTH_YEAR`

## ⚠️ Important Notes

- The extraction script uses PyAutoGUI, so don't move your mouse during execution
- Screen resolution should match what the script expects (default: 1366x768)
- Avoid interrupting the Chrome automation process
- Excluded from git: image files (.tif, .zip), credentials, logs

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributors

- [Your Name] - Initial work and development
