from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Opciones (opcional)
options = Options()
options.add_argument("--start-maximized")

# Crear driver sin descargar ChromeDriver
driver = webdriver.Chrome(options=options)  # Selenium 4 busca automáticamente el driver compatible
driver.get("https://www.saucedemo.com/")
driver.quit()
