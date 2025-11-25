# Caso de prueba: Quitar producto del carrito

## Objetivo
Validar que un producto agregado pueda ser removido correctamente.

## Script
scripts/test_quitar_carrito.py

## Pasos ejecutados
1. Login con usuario standard_user.
2. Agregar "Sauce Labs Backpack" al carrito.
3. Hacer click en "Remove" sobre el producto.
4. Validar que el contador del carrito se actualice a 0.
5. Guardar captura de pantalla.

## Evidencias generadas
- Captura: evidencias/quitar_carrito/producto_quitado.png
- Log: evidencias/quitar_carrito/log_YYYYMMDD_HHMMSS.txt

## Resultados
- Producto removido correctamente y carrito actualizado.
