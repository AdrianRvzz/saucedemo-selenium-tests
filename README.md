# Proyecto de Automatización Swag Labs

## Descripción
Este proyecto automatiza casos de prueba para el sitio https://www.saucedemo.com/ usando Selenium y Python.

Se incluyen pruebas para:
- Login
- Agregar producto al carrito
- Quitar producto del carrito
- Filtrado de productos
- Logout

## Estructura del repositorio
/scripts                  # Scripts de pruebas automatizadas
/evidencias               # Capturas y logs generados por cada prueba
/documentacion            # README específicos de cada caso de prueba
README.md                 # Este archivo

## Requisitos
- Python 3.x
- Selenium
- Chrome y ChromeDriver instalado y en PATH

Instalar Selenium:
```bash
pip install selenium
```

## Ejecución de pruebas

### Ejecutar pruebas individualmente
```bash
python scripts/test_login.py
python scripts/test_agregar_carrito.py
python scripts/test_quitar_carrito.py
python scripts/test_filtrado_productos.py
python scripts/test_logout.py
```

### Ejecutar todas las pruebas a la vez
```bash
python scripts/run_all_tests.py
```

## Evidencias
- Las capturas y logs se guardan automáticamente en la carpeta /evidencias correspondiente a cada caso.
