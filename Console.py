# Inventory system using a dictionary to store products
inventory_product = {} # Dictionary of products
deleted_products = [] # List of deleted products
current_id = 1 # Counter for the id

# Get the ID of a product by name
def get_id(name_product): 
    for id, datas in inventory_product.items():
        if datas ["nombre"] == name_product:
            return id
    return None

# Add a new product to the inventory
def add_products(name_product, price, quantity):
    global current_id 
    if any(product["nombre"] == name_product for product in inventory_product.values()):
        print(f"\nEl producto {name_product} ya existe en el inventario.")
    else:
        inventory_product[current_id] = {
            "nombre": name_product,
            "precio": price,
            "cantidad": quantity
        }
        print(f"\n El producto {name_product} fue añadido al inventario con ID {current_id}.")
        current_id +=1

# Search for a product by name
def search_product(name_product):
    id_product = get_id(name_product)
    if id_product:
        datas = inventory_product[id_product]
        print(f"ID: {id_product} | {datas['nombre']} | Precio: ${datas['precio']:>10,.0f} | Cantidad: {datas['cantidad']:>10,.0f}")
    else:
        print("\n Producto no existe en el inventario.")

# Update the price of an existing product
def update_price(name_product, new_price):
    id_product = get_id(name_product)
    if id_product:
        inventory_product[id_product]["precio"] = new_price
        print(f"\n Precio del producto {name_product} actualizado a ${new_price}.")
    else:
        print("\n El producto no existe en el inventario.")

# Delete a product from the inventory and store it in deleted list
def deleted_product(name_product):
    global current_id
    id_product = get_id(name_product)
    if id_product:
        deleted_products.append({
            "id": id_product,
            "nombre": inventory_product[id_product]["nombre"],
            "precio": inventory_product[id_product]["precio"],
            "cantidad": inventory_product[id_product]["cantidad"]
        })
        del inventory_product[id_product]
        print(f"\n Producto {name_product} fue eliminado del inventario.")
    else:
        print("\n El producto no existe en el inventario.")

# List all deleted products
def list_product_deleted():
    if not deleted_products:
        print("\n No hay productos eliminados.")
    else:
        print("\n Productos eliminados:")
        print("\n")
        for product in deleted_products:
            print(f"ID: {product ['id']} | {product['nombre']} → Precio: ${product['precio']:>10,.0f} | Cantidad: {product['cantidad']:>10,.0f}")

# Calculate total inventory value
def calculate_total_inventory():
    total = sum(map(lambda p: p["precio"] * p["cantidad"], inventory_product.values()))
    print(f" Valor total del inventario: ${total:>10,.0f}")

# Ask the user to enter a valid number greater than 0
def ask_price_quantity(message):
    while True:
        entrada = input(message)
        try:
            amount = float(entrada)
            if amount <= 0:
                print("\n Ingresa un número mayor a 0.")
                print("\n")
            else:
                return amount
        except ValueError:
            print("\nValor inválido, ingresa uno nuevamente.")
            print("\n")

# Initial setup: require at least 5 products
def initial_inventory_setup():
    global current_id
    print("\n ¡ADVERTENCIA! Para debes ingresar al menos 5 productos para comenzar a usar el programa.")
    while len(inventory_product) < 5:
        print(f"\nProducto {len(inventory_product) + 1} de 5:")
        name_product = input("Nombre del producto: ").strip().upper()
        if not name_product:
            print("El nombre del producto no puede estar vacío.")
            continue
        if any(product["nombre"] == name_product for product in inventory_product.values()):
            print("El producto ya existe. Ingresa uno diferente.")
            continue
        price = ask_price_quantity("Precio del producto: $")
        quantity = ask_price_quantity("Cantidad disponible: ")
        print("\n")

        inventory_product[current_id] = {
            "nombre": name_product,
            "precio": price,
            "cantidad": quantity
        }
        print(f"Producto '{name_product}' agregado con ID {current_id}.")
        current_id += 1

# Main menu of the inventory program
def show_menu():
    initial_inventory_setup()
    while True:
        print("\n------ MENÚ DE INVENTARIO ------")
        print("\n")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total")
        print("6. Mostrar todos los productos")
        print("0. Salir")
        print("\n")

        option = input("Selecciona una opción (1-6 ó 0 PARA SALIR): ")

        if option == "1":
            name_product = input("Nombre del producto: ").strip().upper()
            price = ask_price_quantity("Precio del producto: $")
            quantity = ask_price_quantity("Cantidad disponible: ")
            print ("\n")
            add_products(name_product, price, quantity)

        elif option == "2":
            if not inventory_product:
                print("No hay productos en el inventario.")
                show_menu()
            else: 
                inventory_product
                name_product = input("Nombre del producto a consultar: ").strip().upper()
                search_product(name_product)

        elif option == "3":
            if not inventory_product:
                print("No hay productos en el inventario.")
                show_menu()
            else: 
                name_product = input("Nombre del producto a actualizar: ").strip().upper()
                new_price = ask_price_quantity("Nuevo precio: $")
                update_price(name_product, new_price)

        elif option == "4":
            if not inventory_product:
                print("No hay productos en el inventario.")
                show_menu()
            else: 
                name_product = input("Nombre del producto a eliminar: ").strip().upper()
                deleted_product(name_product)

        elif option == "5":
            calculate_total_inventory()

        elif option == "6":
            if len(inventory_product) < 5:
                print("\nDebes tener al menos 5 productos para mostrar el inventario.")
            else:
                print("\nInventario completo:")
                print ("\n")
                for id, datas in inventory_product.items():
                    print(f"ID: {id} | {datas['nombre'].title()} | Precio: ${datas['precio']:>10,.0f} | Cantidad: {datas['cantidad']:>10,.0f}")

                view_deleted = input("\n¿Deseas ver también los productos eliminados? (S/N): ").strip().upper()
                if view_deleted == "S":
                    list_product_deleted()

        elif option == "0":
            print("\n")
            print("Fuera de linea")
            enter_program =  input("\n¿Deseas ingresar al programa? (S/N): ").strip().upper()
            print ("\n")
            if enter_program == "S":
                show_menu()
            else:
                enter_program == "N"
                print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Run the program
show_menu()