import json
import csv
import os

def save_csv(inventary, file_path, header=True):

    if not file_path.strip(): # filtro para ruta vacia, esto quiero decir que si la funcion strip no se ejecuta parar
        print('Error: Debes ingresar un nombre o ruta válida para el archivo')
        return -1
    
    # Debe terminar en .csv o algun formato aqui abajo
    formats = ('.csv','.txt', '.xls', '.xlsx', '.pdf', '.json', '.tsv', '.dat')
    if not file_path.lower().endswith(formats):
        print("Error: el archivo debe terminar en:", formats)
        return -1
    
    # filtro para ubicacion
    file = os.path.dirname(file_path) # esto me permite guardar en la misma ruta
    if file and not os.path.exists(file): # me aseguro de que la carpeta exista
        print('Error: La carpeta indicada no existe')
        return -1
    # filtro por si olvido poner el inventario
    if not inventary:  # aseguro que el inventario sea guardado
        print('Error: Inventario vacio')
        return -1
    
    try:  # intento abrir el archivo
        with open(file_path, 'w', newline='', encoding='utf-8') as archivo: # 3er para que no haya espacio entre linea
            guardar = csv.writer(archivo)                                   # 4to para formato de texto o caracteres
            
            if header:   # verifico si el usuario indicó que no tiene encabezado
                guardar.writerow(['nombre', 'precio', 'cantidad'])  # por defecto los mete si no se indica lo contrario
            
            for invent in inventary:  # recorremos el inventario
                guardar.writerow([invent['nombre'], invent['precio'], invent['cantidad']])  # guardo cada linea en guardar
        print(f'\nEl inventario se guardó exitosamente en la ruta => {file_path}')
        print(guardar)

    # Manejo de errores
    except PermissionError:
        print('Error: No tienes permido para usar esta ruta')
        return -1

    except FileNotFoundError:
        print('Error: La ruta ingresada no existe')
        return -1
    
    except OSError:
        print('Error: La ruta tiene caracteres invalidos')
        return -1
    
    except Exception:
        print('Error inesperado. Intentelo nuevamente')
        return -1


# Funcion para cargar datos
def upload_csv(file_path):
    try:
        with open(file_path, 'r') as archi:
            archivo = csv.reader(archi) # el detalle con reader es que la informacion se consume con cada iteracion

            # todo esto lo voy a returnar
            archivos_filtrados = []
            filas_omitidas_tamaño = [] 
            filas_omitidas_datos = []
            datos_originales = []   # captura todos los datos

            #contador_1 = 0  # filas omitidas por columnas incompatibles
            #contador_2 = 0  # filas omitidas por datos incompatibles

            try:
                encabezado_archivo = next(archivo)
                # next solo hace una iteracion, justo lo que necesito para mi comparar encabezados
                # el problema con next es que ya hace una iteracion sobre archivo y los for por debajo ya comienzan en la posicion 1
                encabezado_minusculas = [enc.strip().lower() for enc in encabezado_archivo] #la primera linea es una lista
                if encabezado_minusculas != ['nombre', 'precio', 'cantidad']:
                    print("Error: El encabezado no es válido.")
                    print("Se espera: nombre, precio, cantidad")
                    return -1 

            except StopIteration:
                print("Error: El archivo está vacío.")
                return -1  # estos valores serán tomados por variables al llamar la funcion

            
            for i, ar in enumerate(archivo): # archivo ya se iteró una vez
                datos_originales.append(ar)  # guardo todos los datos
                ar = [col.strip() for col in ar]   # esto limpia de espacios no desaeados en cada iteracion los elementos de la lista
                if len(ar) != 3:  # comparacion de tamaño en cada fila
                    filas_omitidas_tamaño.append(i)  # guardo cada fila omitida por tamño
                    #contador_1 += 1
                    continue
                try:
                    ar[1] = float(ar[1])
                    ar[2] = int(ar[2])
                    if ar[1] < 0 or ar[2] < 0:
                        filas_omitidas_datos.append(i)
                        #contador_2 += 1
                        continue
                except (ValueError, TypeError):
                    filas_omitidas_datos.append(i)
                    #contador_2 += 1
                    continue
                
                archivos_filtrados.append(ar)

            archivo_cargado = []
            for a in archivos_filtrados:
                dict_ar_fi = {
                    'nombre': a[0],
                    'precio': a[1],
                    'cantidad': a[2],
                }
                archivo_cargado.append(dict_ar_fi)

            # resultados
            print('\n--- RESUMEN ----')
            print(f'Filas omitidas por columnas incompatibles => {filas_omitidas_tamaño} => total : {len(filas_omitidas_tamaño)}')
            print(f'Filas omitidas por columnas incompatibles => {filas_omitidas_datos} => total : {len(filas_omitidas_datos)}')
            print(f'Total filas omitidas : {len(filas_omitidas_datos) + len(filas_omitidas_tamaño)}')
            
            return archivo_cargado

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file_path}'.")
        return -1
    except UnicodeDecodeError:
        print("Error: No se puede decodificar el archivo. Use UTF-8.")
        return -1
    except Exception as e:
        print(f"Error inesperado: {e}")
        return -1

#cargar = upload_csv('archivo.csv')
#print(cargar)
