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


# Funcion para pedir productos
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
    
    print('-'*40)
    print(f'{'INVENTARIO':<15}')
    print('-'*40)
    print(F'{'NOMBRE':<11} | {'PRECIO':<11} | {'CANTIDAD':<11}')

    for invent in (inventary):
        print(f'{invent['nombre']:<11} | {invent['precio']:<11} | {invent['cantidad']:<11}')
    print('-'*40)



# Funcion Buscar producto
def searc_product():
    pass
    print('-'*40)
    print(f'{'INVENTARIO':<15}')
    print('-'*40)

