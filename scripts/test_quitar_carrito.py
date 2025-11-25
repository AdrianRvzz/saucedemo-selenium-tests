from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime
import time

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

    # Agregar producto primero
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add_button.click()
    log_text += "Producto agregado al carrito.\n"

    # Quitar producto
    remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    )
    remove_button.click()
    log_text += "Producto removido del carrito.\n"

    # Validar carrito vacío
    badges = driver.find_elements(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    assert len(badges) == 0
    log_text += "Contador del carrito actualizado correctamente.\n"

    # Captura
    screenshot_path = "evidencias/quitar_carrito/producto_quitado.png"
    os.makedirs("evidencias/quitar_carrito", exist_ok=True)
    driver.save_screenshot(screenshot_path)
    log_text += f"Captura guardada en {screenshot_path}\n"

except Exception as e:
    log_text += f"Error: {str(e)}\n"

finally:
    save_log(log_text, "evidencias/quitar_carrito")
    print(log_text)
    driver.quit()
