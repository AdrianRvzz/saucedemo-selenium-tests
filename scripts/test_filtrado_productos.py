from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
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

    # Filtrado: Price low to high
    sort_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='product-sort-container']"))
    )
    select = Select(sort_select)
    select.select_by_value("lohi")
    log_text += "Filtro 'Price (low to high)' aplicado.\n"

    # Esperar a que se apliquen cambios
    WebDriverWait(driver, 5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    )

    # Captura
    screenshot_path = "evidencias/filtrado_productos/filtro_aplicado.png"
    os.makedirs("evidencias/filtrado_productos", exist_ok=True)
    driver.save_screenshot(screenshot_path)
    log_text += f"Captura guardada en {screenshot_path}\n"

except Exception as e:
    log_text += f"Error: {str(e)}\n"

finally:
    save_log(log_text, "evidencias/filtrado_productos")
    print(log_text)
    driver.quit()
