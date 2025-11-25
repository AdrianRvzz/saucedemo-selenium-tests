from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime

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
    # LOGIN
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    log_text += "Login exitoso.\n"

    # Abrir menú
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_button.click()

    # Click en logout
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_button.click()
    log_text += "Logout exitoso.\n"

    # Captura
    screenshot_path = "evidencias/logout/logout_exitoso.png"
    os.makedirs("evidencias/logout", exist_ok=True)
    driver.save_screenshot(screenshot_path)
    log_text += f"Captura guardada en {screenshot_path}\n"

except Exception as e:
    log_text += f"Error: {str(e)}\n"

finally:
    save_log(log_text, "evidencias/logout")
    print(log_text)
    driver.quit()
