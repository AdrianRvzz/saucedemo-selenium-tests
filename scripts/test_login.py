from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import datetime

# Función para guardar logs
def save_log(text, folder):
    os.makedirs(folder, exist_ok=True)
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(folder, f"log_{now}.txt")
    with open(log_file, "w") as f:
        f.write(text)

log_text = ""

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

try:
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    log_text += "Usuario ingresado correctamente.\n"
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    log_text += "Contraseña ingresada correctamente.\n"
    driver.find_element(By.ID, "login-button").click()
    log_text += "Click en login realizado.\n"
    time.sleep(2)
    
    # Validación
    assert "inventory" in driver.current_url
    log_text += "Login exitoso, página inventory.html cargada.\n"

    # Captura
    screenshot_path = "evidencias/login/login_exitoso.png"
    os.makedirs("evidencias/login", exist_ok=True)
    driver.save_screenshot(screenshot_path)
    log_text += f"Captura guardada en {screenshot_path}\n"

except Exception as e:
    log_text += f"Error: {str(e)}\n"

finally:
    save_log(log_text, "evidencias/login")
    print(log_text)
    driver.quit()
