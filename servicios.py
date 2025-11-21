# Mensaje con el menú principal
def msm_main(menu = """
        *** MENÚ PRINCIPAL ***
        
        1. agregar
        2. Mostrar
        3. Buscar
        4. actualizar
        5. Eliminar
        6. Estadisticas
        7. Guardar CSV
        8. Cargar CSV
        9. Salir
        """):
    return menu


# Función para depurar entradas del menu principal
def filter_sel_main():
    sel = input('Elija una opción listada: ')
    try:
        sel = int(sel)
    except ValueError:
        print('Error: Ingrese una opción listada')
    if sel > 0 and sel<10:
        return sel
    else:
        print('Error: Ingrese una opcion listada')


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
    print('-'*(len_name + len_price + len_quantity + 10))
    print(f'{'INVENTARIO':<{len_name + 0.5*(len_price)}} {'':<{len_quantity + 0.5*(len_price)}}')
    print('-'*(len_name + len_price + len_quantity + 10))
    print(F'{'NOMBRE':<{len_name}} | {'PRECIO':<{len_price}} | {'CANTIDAD':<{len_quantity}}')
    print('-'*(len_name + len_price + len_quantity + 10))
    for inv in (inventary):
        print(F'{inv['nombre']:<{len_name}} | {inv['precio']:<{len_price}} | {inv['cantidad']:<{len_quantity}}')
    print('-'*(len_name + len_price + len_quantity + 10))



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
            print(F'{inventary[i]['nombre']:<{len_name}} | {inventary[i]['precio']:<{len_price}} | {inventary[i]['cantidad']:<{len_quantity}}')
            none_found = True
    if not none_found: # en caso de no encontrar nada
        print('El PRODUCTO no se encuentra en en INVENTARIO')
    print('-'*(len_name + len_price + len_quantity + 10)) # linea inferior


# Funcion actualizar inventario
def apdate_inventary(inventary, name, new_price = None, new_quantity = None):
    
    find_product = False # bandera para buscar
    find_price = False
    find_quantity = False
    for i in range(len(inventary)):
        if name == inventary[i]['nombre']:
            find_product = True
            if new_price != None:
                inventary[i]['precio'].append(new_price)
                find_price = True
            if new_quantity != None:
                inventary[i]['cantidad'].append(new_quantity)
                find_product = True
    # Revisando banderas
    if not find_product:
        print('El PRODUCTO ingresado no está en el INVENTARIO')
    elif find_price:
        print('No se actualizó el PRECIO')
    elif find_quantity:
        print('No se actualizó el CANTIDAD')
    return inventary # regreso inventario actualizado
    



