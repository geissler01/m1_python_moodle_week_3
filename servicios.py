# Mensaje con el menú principal
def msm_main(menu = """
        *** MENÚ PRINCIPAL ***
        
        1. agregar
        2. Mostrar
        3. Buscar
        4. actualizar
        5. Eliminar
        6. Estadisticas
        7. Cargar Csv
        8. Guardar CSV
        9. Salir
        """):
    return menu


# Función para depurar entradas del menu principal
def filter_sel_main():
    while True:
        sel = input('Elija una opción listada: ')
        try:
            sel = int(sel)
            if sel > 0 and sel<10:
                return sel
            else:
                print('Error: Ingrese una opcion listada')
        except ValueError:
            print('Error: Ingrese una opción listada')
    


# Funcion para pedir productos y añadir productos
def add_product(inventary: list):

    name = input('NOMBRE: ')
    
    while True:
        price = input('PRECIO: ')
        try:
            price = float(price)
        except ValueError:
            print('Error: Ingrese un valor valido para precio')
            continue
        if price < 0:
            print('Error: Ingrese un valor valido para precio')
        else:
            break
        
    while True:
        quantity = input('CANTIDAD: ')
        try:
            quantity = int(quantity)
        except ValueError:
            print('Error: Ingrese un valor valido para precio')
            continue
        if quantity < 0:
            print('Error: Ingrese un valor valido para precio')
        else:
            break
    
    dict_inventary = {
        'nombre':name,
        'precio':price,
        'cantidad':quantity
    }
    inventary.append(dict_inventary)
    return inventary


# Funcion mostrar inventario
def show_inventary(inventary):
    
    # tabla dinamica, medidas
    len_name = max(len(l['nombre']) for l in inventary)
    len_price = max(len(str(l['precio'])) for l in inventary)
    len_quantity = max(len(str(l['cantidad'])) for l in inventary)
    # Encabezado
    print('-'*(len_name + len_price + len_quantity + 13))
    print(f'{'INVENTARIO':>15}')
    print('-'*(len_name + len_price + len_quantity + 13))
    print(F'{'NOMBRE':<{len_name}} | {'PRECIO':<{len_price}} | {'CANTIDAD':<{len_quantity}}')
    print('-'*(len_name + len_price + len_quantity + 13))
    for inv in (inventary):
        print(F'{inv['nombre']:<{len_name}} | {str(inv['precio']):<{len_price}} | {str(inv['cantidad']):<{len_quantity}}')
    print('-'*(len_name + len_price + len_quantity + 13))



# Funcion Buscar producto
def search_product(inventary, name):
    # tabla dinamica, medidas
    len_name = max(len(l['nombre']) for l in inventary)
    len_price = max(len(str(l['precio'])) for l in inventary)
    len_quantity = max(len(str(l['cantidad'])) for l in inventary)
    # Encabezado
    print('-'*(len_name + len_price + len_quantity + 10))
    print(F'{'NOMBRE':<{len_name}} | {'PRECIO':<{len_price}} | {'CANTIDAD':<{len_quantity}}')
    print('-'*(len_name + len_price + len_quantity + 10))
    none_found = False # bandera para averigar si encotramos algo
    for i in range(len(inventary)): # recorro la tabla
        if name == inventary[i]['nombre']: # comparo la busqueda
            print(f'{inventary[i]['nombre']:<{len_name}} | {str(inventary[i]['precio']):<{len_price}} | {str(inventary[i]['cantidad']):<{len_quantity}}')
            none_found = True
    if not none_found: # en caso de no encontrar nada
        print('El PRODUCTO no se encuentra en en INVENTARIO')
    print('-'*(len_name + len_price + len_quantity + 10)) # linea inferior


# Funcion Buscar para actualizar producto
def search_update_product(inventary, name):
    none_found = False
    for invent in inventary: # recorro la tabla
        if name == invent['nombre']: # comparo la busqueda
            none_found = True
    if not none_found: # en caso de no encontrar nada
        print('El PRODUCTO no se encuentra en en INVENTARIO')
        return -1 # para saber que el producto no se encuentra en la lista
    else:
        print('Producto encontrado')
        return 1


# Funcion actualizar inventario
def apdate_inventary(inventary, name, new_price = None, new_quantity = None):
    
    if new_price is not None:
        try:
            new_price = float(new_price)
            if new_price < 0:
                print('Error: Ingrese un valor valido para precio')
                return -1      # para saber si repetir o no
        except ValueError:
            print('Error: Ingrese un valor valido para precio')
            return -1

    if new_quantity != None:
        try:
            new_quantity = int(new_quantity)
            if new_quantity < 0:
                print('Error: Ingrese un valor valido para precio')
                return -1
        except ValueError:
            print('Error: Ingrese un valor valido para precio')
            return -1
    print(inventary)
    for invent in inventary[:]:
        if name == invent['nombre']:
                invent['precio'] = new_price
                invent['cantidad'] = new_quantity
    print(inventary)
    return inventary


# Funcion para eliminar producto
def delate_product(inventary, name):
    find_p = False
    for invent in inventary:
        if name == invent['nombre']:
            inventary.remove(invent)
            find_p = True
            print(f'Producto eliminado')
    if not find_p:
        print('PRODUCTO no encontrado en el INVENTARIO')
    return inventary


# Funcion para calcular estadisticas
def calculate_statistics(inventary):
    account = inventary # copia para no comprometer los datos originales
    for ac in account[:]: # uso la copia para recorrer, pero los cambios iran a la lista original
        precio = ac.get('precio')
        cantidad = ac.get('cantidad')
        if precio is None or cantidad is None: # si alguna de estas claves es none entonces no calcular
            ac['total'] = None
        else:
            ac['total'] = round(precio*cantidad, 2)
    #suma de productos
    quantity_products = len(account)  # simplemente suma los items del inventario, suponiendo que todos los registros tienen un producto
    total_price_inventary = round(sum(invent['total'] for invent in account if invent['total'] is not None)) # sumo totales de precios por producto
    higher_price = max(invent['precio'] for invent in account if invent['precio'] is not None) # precio mas alto
    for ac in account:  # determinando nombre del precio mas alto
        if higher_price == ac['precio']:
            name_product = ac['nombre']
            break

    higher_quantity_product = max(invent['cantidad'] for invent in account if invent['cantidad'] is not None) # producto con cantidad mas alta
    for ac in account:
        if higher_quantity_product == ac['cantidad']: # buscando nombre del producto con mayor stock
            name_product_q = ac['nombre']
            break

    # tabla dinamica, medidas
    len_name = max(len(l['nombre']) for l in account)
    len_price = max(len(str(l['precio'])) for l in account)
    len_quantity = max(len(str(l['cantidad'])) for l in account)
    len_total = max(len(str(l['total'])) for l in account)

    # Encabezado
    print('-'*(len_name + len_price + len_quantity + len_total + 13))
    print(f'{'INVENTARIO':>15}')
    print('-'*(len_name + len_price + len_quantity + len_total + 13))
    print(F'{'NOMBRE':<{len_name}} | {'PRECIO':<{len_price}} | {'CANTIDAD':<{len_quantity}} | {'TOTAL':<{len_total}}')
    print('-'*(len_name + len_price + len_quantity + len_total + 13))

    for inv in (account):
        print(F'{inv['nombre']:<{len_name}} | {str(inv['precio']):<{len_price}} | {str(inv['cantidad']):<{len_quantity + 5}} | {str(inv['total']):<{len_total}}')
    print('-'*(len_name + len_price + len_quantity + len_total + 13))

    print(f'Suma total precios =>           {total_price_inventary}') # suma se total precios
    print(f'Cantidad de productos =>        {quantity_products}')
    print(f'Producto mas caro =>            {name_product} | {higher_price}')
    print(f'Producto con mayor stock =>     {name_product_q} | {higher_quantity_product}')


    

