from servicios import *

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
    if sel == 1:
        add_product(inventary)
        
    elif sel == 2:
        show_inventary(inventary)

    elif sel == 3:
        find_product = input('NOMBRE PRODUCTO: ')
        search_product(inventary, find_product )

    elif sel == 4: # actualizar
        while True:
            product = input('NOMBRE PRODUCTO: ')
            if product != '':
                break
            else:
                print('Error: Ingrese el nombre del producto a ACTUALIZAR')
        while True:
            price = input('PRECIO: ')
            quantity = input('CANTIDAD: ')
            if price == '' or quantity == '':
                print('Error: ingrese valores de precio o cantidad válidos')
                continue
            inventary = apdate_inventary(inventary, product, price, quantity)
            if inventary != None:
                break
            inventary = inventary
            break


    elif sel == 5:

        pass
    elif sel == 6:
        pass
    elif sel == 7:
        pass
    elif sel == 8:
        pass
    elif sel == 9:
        pass
    else:
        pass
