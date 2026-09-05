import csv


def leer_datos(ruta_archivo):
    """Lee el archivo CSV y convierte los datos en una lista de diccionarios."""
    datos = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            producto = {
                "id_producto": int(fila["id_producto"]),
                "nombre": fila["nombre"],
                "precio": float(fila["precio"]),
                "calificacion_cliente": float(fila["calificacion_cliente"])
            }

            datos.append(producto)

    return datos


def calcular_estadisticas(datos):
    """Calcula estadísticas relevantes del dataset."""

    precios = [producto["precio"] for producto in datos]
    calificaciones = [
        producto["calificacion_cliente"] for producto in datos
    ]

    total_productos = len(datos)

    precio_total = sum(precios)
    precio_promedio = precio_total / total_productos

    precio_maximo = max(precios)
    precio_minimo = min(precios)

    promedio_calificacion = (
        sum(calificaciones) / total_productos
    )

    calificacion_maxima = max(calificaciones)
    calificacion_minima = min(calificaciones)

    producto_mas_caro = max(
        datos,
        key=lambda producto: producto["precio"]
    )

    producto_mas_economico = min(
        datos,
        key=lambda producto: producto["precio"]
    )

    producto_mejor_calificado = max(
        datos,
        key=lambda producto: producto["calificacion_cliente"]
    )

    return {
        "total_productos": total_productos,
        "precio_total": precio_total,
        "precio_promedio": precio_promedio,
        "precio_maximo": precio_maximo,
        "precio_minimo": precio_minimo,
        "promedio_calificacion": promedio_calificacion,
        "calificacion_maxima": calificacion_maxima,
        "calificacion_minima": calificacion_minima,
        "producto_mas_caro": producto_mas_caro["nombre"],
        "producto_mas_economico": producto_mas_economico["nombre"],
        "producto_mejor_calificado": producto_mejor_calificado["nombre"]
    }


def generar_informe(estadisticas, archivo_salida):
    """Genera el informe del proyecto en formato Markdown."""

    with open(archivo_salida, "w", encoding="utf-8") as archivo:

        archivo.write("# Informe del Sistema de Recomendación de Autocuidado\n\n")

        archivo.write("## Descripción de los datos\n\n")

        archivo.write(
            "El dataset contiene información sobre productos de "
            "autocuidado, incluyendo el nombre del producto, su precio "
            "y la calificación otorgada por los clientes.\n\n"
        )

        archivo.write("## Estadísticas\n\n")

        archivo.write(
            f"- **Cantidad total de productos:** "
            f"{estadisticas['total_productos']}\n"
        )

        archivo.write(
            f"- **Precio total del catálogo:** "
            f"${estadisticas['precio_total']:,.2f}\n"
        )

        archivo.write(
            f"- **Precio promedio:** "
            f"${estadisticas['precio_promedio']:,.2f}\n"
        )

        archivo.write(
            f"- **Precio máximo:** "
            f"${estadisticas['precio_maximo']:,.2f}\n"
        )

        archivo.write(
            f"- **Precio mínimo:** "
            f"${estadisticas['precio_minimo']:,.2f}\n"
        )

        archivo.write(
            f"- **Promedio de calificación:** "
            f"{estadisticas['promedio_calificacion']:.2f}\n"
        )

        archivo.write(
            f"- **Calificación máxima:** "
            f"{estadisticas['calificacion_maxima']:.1f}\n"
        )

        archivo.write(
            f"- **Calificación mínima:** "
            f"{estadisticas['calificacion_minima']:.1f}\n"
        )

        archivo.write(
            f"- **Producto más caro:** "
            f"{estadisticas['producto_mas_caro']}\n"
        )

        archivo.write(
            f"- **Producto más económico:** "
            f"{estadisticas['producto_mas_economico']}\n"
        )

        archivo.write(
            f"- **Producto mejor calificado:** "
            f"{estadisticas['producto_mejor_calificado']}\n\n"
        )

        archivo.write("## Interpretación de los resultados\n\n")

        archivo.write(
            f"El catálogo analizado contiene "
            f"{estadisticas['total_productos']} productos. "
            f"El precio promedio es de "
            f"${estadisticas['precio_promedio']:,.2f}. "
            f"El producto más económico es "
            f"{estadisticas['producto_mas_economico']}, "
            f"mientras que el producto más caro es "
            f"{estadisticas['producto_mas_caro']}.\n\n"
        )

        archivo.write(
            f"La calificación promedio de los productos es de "
            f"{estadisticas['promedio_calificacion']:.2f} sobre 5. "
            f"El producto mejor calificado es "
            f"{estadisticas['producto_mejor_calificado']}. "
            f"Estas estadísticas pueden ayudar al sistema de "
            f"recomendación a identificar productos con buenas "
            f"calificaciones y diferentes rangos de precio.\n"
        )


if __name__ == "__main__":

    ruta = "datos_autocuidado.csv"

    datos = leer_datos(ruta)

    estadisticas = calcular_estadisticas(datos)

    generar_informe(
        estadisticas,
        "informe_proyecto.md"
    )

    print("Informe del proyecto generado correctamente.")