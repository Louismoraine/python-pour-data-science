import subprocess
import sys
import pkg_resources

required_packages = ["selenium==4.6.0", "webdriver-manager", "pandas"]

def install_packages():
    """
    Vérifie si les packages requis sont installés.
    Si ce n'est pas le cas, ils seront installés automatiquement.
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    # Vérifie les packages installés
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    
    # Vérifie les packages manquants
    missing_packages = [pkg for pkg in required_packages if pkg.split('==')[0] not in installed_packages]
    
    if missing_packages:
        print(f"Installation des dépendances manquantes : {', '.join(missing_packages)}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_packages])
    else:
        print("Tous les packages nécessaires sont déjà installés.")

# Appel de la fonction pour installer les packages nécessaires
install_packages()

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service('/usr/bin/google-chrome')  # Remplacez par le chemin correct de ChromeDriver
browser = webdriver.Chrome(service=service, options=chrome_options)
print("Chromedriver lancé avec succès !")