
# Sistema de Inventario en Python

Este es un sistema de gestión de inventario básico hecho en Python. Permite registrar productos, consultarlos, actualizar precios, eliminar productos y calcular el valor total del inventario. Además, guarda un registro de los productos eliminados.

## Características

- Añadir productos con ID único, nombre, precio y cantidad.
- Evita nombres duplicados al registrar productos.
- Muestra información de productos específicos.
- Actualiza el precio de productos existentes.
- Elimina productos del inventario (se guarda un registro en otra lista).
- Calcula el valor total del inventario.
- Muestra todos los productos del inventario, incluyendo los eliminados si el usuario lo desea.
- Requiere ingresar al menos 5 productos antes de comenzar.

## Estructura del Código

- `inventory_product`: Diccionario principal donde se guarda el inventario.
- `deleted_products`: Lista donde se guardan los productos eliminados.
- `current_id`: Lleva el control de los IDs únicos asignados a cada producto.


## Funciones Principales

| Función | Descripción |
|--------|-------------|
| `get_id(name_product)` | Devuelve el ID del producto a partir de su nombre. |
| `add_products(name, price, quantity)` | Agrega un producto nuevo al inventario. |
| `search_product(name)` | Busca un producto por nombre e imprime su información. |
| `update_price(name, new_price)` | Cambia el precio de un producto existente. |
| `deleted_product(name)` | Elimina un producto y lo guarda en la lista de eliminados. |
| `list_product_deleted()` | Muestra la lista de productos que fueron eliminados. |
| `calculate_total_inventory()` | Muestra el valor total del inventario. |
| `ask_price_quantity(msg)` | Pide al usuario ingresar un número mayor que 0. |
| `initial_inventory_setup()` | Obliga al usuario a registrar al menos 5 productos válidos al iniciar. |
| `show_menu()` | Muestra el menú principal del programa. |

## Cómo usar el programa

1. Corre el archivo Python (`.py`).
2. Ingresa 5 productos válidos con nombre, precio y cantidad.
3. Luego, accede al menú donde podrás elegir entre varias opciones para gestionar el inventario.

## Requisitos

- Python 3.x
- Funciona en terminales como CMD, PowerShell, Bash o la terminal de tu editor de código (VS Code, PyCharm, etc.).


## Notas importantes

- El nombre de los productos se guarda en mayúsculas para evitar duplicados y facilitar las búsquedas.
- Si intentas ingresar un producto con el mismo nombre, el sistema no lo permitirá.
- Los productos eliminados no se pierden: puedes verlos en la opción de inventario completo.
