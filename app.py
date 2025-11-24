import csv
from servicios import *
from files import *

inventary = [
    {"nombre": "Laptop", "precio": 899.99, "cantidad": 12},
    {"nombre": "Mouse", "precio": 24.50, "cantidad": 58},
    {"nombre": "Teclado", "precio": 79.90, "cantidad": 34},
    {"nombre": "Monitor", "precio": 159.99, "cantidad": 20},
    {"nombre": "Disco", "precio": 119.49, "cantidad": 15}
]

while True:
    print(msm_main())
    sel = filter_sel_main()

    if sel == 1:  # Agrepar producto
        add_product(inventary)
        
    elif sel == 2:  # Mostrar productos
        show_inventary(inventary)


    elif sel == 3:   # Buscar producto
        find_product = input('NOMBRE PRODUCTO: ')
        search_product(inventary, find_product )


    elif sel == 4: # actualizar
        while True:
            # Buscando antes de actualizar
            nombre_p = input('NOBRE PRODUCTO: ')
            r_busqueda = search_update_product(inventary, nombre_p)
            if r_busqueda == -1:
                p_update = input('\n¿Desea intentar actualizar producto nuevamente? => s/n : ')
                if p_update.strip().lower() == 's':
                    continue
                else:
                    break
            else:
                precio_act = input('¿Desea actualizar precio?, s/n : ')
                b_p = 0
                if precio_act.strip().lower() == 's':  # Pide precio
                    ing_precio = input('PRECIO: ')
                    b_p = 1   # bandera para saber como llamar la función
                    
                cantidad_act = input('\n¿Desea actualizar cantidad?, s/n : ')
                b_c = 0
                if cantidad_act.strip().lower() == 's':
                    ing_cantidad = input('CANTIDAD: ')
                    b_c = 1
                # Diferentes llamados segun requiera el usuario
                if b_p == 1 and b_c == 0:
                    inventary = apdate_inventary(inventary, nombre_p, ing_precio)
                elif b_p == 1 and b_c == 1:
                    inventary = apdate_inventary(inventary, nombre_p, ing_precio, ing_cantidad)   
                else:
                    inventary = apdate_inventary(inventary, nombre_p, ing_cantidad)

                if inventary == -1:
                    p_update = input('\n¿Desea intentar actualizar producto nuevamente? => s/n : ')
                    if p_update.strip().lower() == 's':
                        continue
                    else:
                        break
                else:
                    break


    elif sel == 5: # Eliminar producto //
        while True:
                delate_p = input('PRODUCTO: ').strip() 
                if delate_p != '':  # Me aseguro de que ingrese un producto
                    break
                else:
                    print('\nError: Ingrese el nombre del producto a ELIMINAR')
        delate_product(inventary, delate_p)


    elif sel == 6: # Estadisticas  //
        calculate_statistics(inventary)


    elif sel == 7: # Cargar CSV
        bp = True
        while bp:
            while True:
                file_path = input('ingrese ruta o nombre del archivo: ')
                file_upload = upload_csv(file_path)
                if file_upload == -1:
                    p = input('\n¿Desea intentar cargar el archivo nuevamente? => s/n : ')
                    if p.strip().lower() != 's':
                        bp = False
                        break
                else:
                    break
            if not bp:
                break
            re_write = input('\n¿Desea sobreescribir inventario actual? => s/n : ')
            if re_write.strip().lower() == 'n':
                for file in file_upload:
                    price = file.get('precio')
                    quantity = file.get('cantidad')

                    found_it = False
                    
                    for inv in inventary:
                        if file['nombre'] == inv['nombre']:
                            inv['precio'] = price
                            inv['cantidad'] = quantity + inv['cantidad']
                            found_it = True
                            break
                    
                    if not found_it:
                        inventary.append(file)

                print('\nSe mantuvo el inventario Actual, se actualizó el precio y se sumaron las cantidades de ambos inventarios')
                print(inventary)
                bp = False
                break
            else:
                inventary = file_upload
                break


    elif sel == 8: # Guardar CSV
        while True:
            file_path = input('Ingrese la ruta o nombre del archivo donde desea guardar el inventario: ')
            enc_inv = input('¿Desea agregar encabezado a los datos? => s/n : ')
            if enc_inv.strip().lower() == 'n':
                header = False
                r_save = save_csv(inventary, file_path, header)
            else:
                r_save = save_csv(inventary, file_path)
            # Verificacion de si salio bien o no el proceso de guardar
            if r_save is -1:
                p = input('\n¿Desea intentar guardar el archivo nuevamente? => s/n : ')
                if p.strip().lower() != 's':
                    break
                else:
                    continue
            else:
                break


    elif sel == 9: # Salir
        print('\nSe cierra el programa. ¡Hazta pronto!\n')
        break


    else:  # Por seguridad
        print('\nError: Por favor ingrese una opción válida')
        
