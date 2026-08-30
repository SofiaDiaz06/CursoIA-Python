import csv

def leer_datos(ruta_archivo):
    """Lee un archivo CSV y lo convierte en una lista de diccionarios."""
    datos = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convertimos los valores numéricos a tipos float/int
            fila['precio'] = float(fila['precio'])
            fila['calificacion_cliente'] = float(fila['calificacion_cliente'])
            datos.append(fila)
    return datos

def mostrar_resumen(datos):
    """Muestra la cantidad total de registros y 3 estadísticas básicas."""
    total_registros = len(datos)
    print(f"Cantidad total de registros: {total_registros}")

    if total_registros > 0:
        precios = [p['precio'] for p in datos]
        calificaciones = [p['calificacion_cliente'] for p in datos]
        promedio_precio = sum(precios) / total_registros
        max_calificacion = max(calificaciones)
        min_precio = min(precios)

        print(f"Promedio de precio de productos: ${promedio_precio:,.2f}")
        print(f"Calificación máxima de los clientes: {max_calificacion}")
        print(f"Precio mínimo en el catálogo: ${min_precio:,.2f}")

ruta = 'datos_autocuidado.csv'
productos = leer_datos(ruta)

print("--- Resumen del Sistema de Recomendación de Autocuidado ---")
mostrar_resumen(productos)