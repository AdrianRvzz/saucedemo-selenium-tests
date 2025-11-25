import subprocess
import os
from datetime import datetime

# Carpeta donde se guardarán los logs
LOG_DIR = "evidencias/logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Lista de scripts a ejecutar
tests = [
    "scripts/test_login.py",
    "scripts/test_agregar_carrito.py",
    "scripts/test_quitar_carrito.py",
    "scripts/test_filtrado_productos.py",
    "scripts/test_logout.py"
]

# Ejecutar cada test
for test_script in tests:
    test_name = os.path.splitext(os.path.basename(test_script))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(LOG_DIR, f"{test_name}_log_{timestamp}.txt")
    
    print(f"Ejecutando {test_name}...")

    with open(log_file, "w") as lf:
        # Ejecutar script y redirigir salida a log
        process = subprocess.Popen(
            ["python", test_script],
            stdout=lf,
            stderr=subprocess.STDOUT
        )
        process.communicate()  # Esperar a que termine el test
    
    print(f"{test_name} finalizado. Log guardado en {log_file}\n")

print("Todas las pruebas han finalizado.")
