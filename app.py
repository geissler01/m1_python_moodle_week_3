import csv
from servicios import *
from files import *

inventary = [
    {"nombre": "Laptop", "precio": 899.99, "cantidad": 12},
    {"nombre": "Mouse inalámbrico", "precio": 24.50, "cantidad": 58},
    {"nombre": "Teclado mecánico", "precio": 79.90, "cantidad": 34},
    {"nombre": "Monitor 24 pulgadas", "precio": 159.99, "cantidad": 20},
    {"nombre": "Disco SSD 1TB", "precio": 119.49, "cantidad": 15}
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
        flag_main = True
        while flag_main:
            while True:
                product = input('NOMBRE PRODUCTO: ').strip()
                if product != '':
                    break
                else:
                    print('Error: Ingrese el nombre del producto a ACTUALIZAR')
            while True:
                price = input('PRECIO: ').strip()
                quantity = input('CANTIDAD: ').strip()
                if price == '' or quantity == '':
                    print('Error: ingrese valores de precio o cantidad válidos')
                    continue
                else:
                    break
            
            while True:
                inventary_copy = apdate_inventary(inventary, product, price, quantity)   # corro con una copia para no dañar daños originales
                if inventary_copy is not None:
                    flag_main = False
                    inventary = apdate_inventary(inventary, product, price, quantity) 
                    break
                else:
                    following = input('¿Desea Coregir o Actualizar nuevo PRODUCTO? => s/n : ').strip()
                    if following != 's':
                        break             
                    else:
                        flag_main = False                     
                        break
                    
    elif sel == 5: # Eliminar producto //
        while True:
                delate_p = input('PRODUCTO: ').strip()
                if delate_p != '':
                    break
                else:
                    print('Error: Ingrese el nombre del producto a ACTUALIZAR')
        delate_product(inventary, delate_p)

    elif sel == 6: # Estadisticas  //
        calculate_statistics(inventary)

    elif sel == 7: # Cargar CSV
        pass
    elif sel == 8: # Guardar CSV
        pass
    elif sel == 9: # Salir
        print('Se cierra el programa. ¡Hazta pronto!')
        break
    else:  # Por seguridad
        print('Error: Vuelva a iniciar el programa')
        break
