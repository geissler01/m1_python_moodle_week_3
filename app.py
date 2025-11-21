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
    elif sel == 4:
        product = input('NOMBRE PRODUCTO: ')
        price = input('PRECIO: ')
        quantity = input('CANTIDAD: ')
        inventary = apdate_inventary(inventary, product, price, quantity)

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
