cultivos = [
    {"nombre": "Café", "hectareas": 5, "produccion_toneladas": 3.2},
    {"nombre": "Caña", "hectareas": 10, "produccion_toneladas": 8.5},
    {"nombre": "Maíz", "hectareas": 3, "produccion_toneladas": 1.8},
    {"nombre": "Plátano", "hectareas": 4, "produccion_toneladas": 5.0},
    {"nombre": "Frijol", "hectareas": 2, "produccion_toneladas": 1.2}
]

def calcular_rendimiento(cultivo):
    return cultivo["produccion_toneladas"] / cultivo["hectareas"]

def mostrar_cultivos(lista_cultivos):
    for cultivo in lista_cultivos:
        rendimiento = calcular_rendimiento(cultivo)
        print(f"Cultivo: {cultivo['nombre']} - Rendimiento: {rendimiento:.2f} ton/ha")

def cultivo_mayor_rendimiento(lista_cultivos):
    mejor_cultivo = ""
    max_rendimiento = 0
    for cultivo in lista_cultivos:
        rend = calcular_rendimiento(cultivo)
        if rend > max_rendimiento:
            max_rendimiento = rend
            mejor_cultivo = cultivo["nombre"]
    return mejor_cultivo

print("--- Datos de Cultivos ---")
mostrar_cultivos(cultivos)
mejor = cultivo_mayor_rendimiento(cultivos)
print(f"\nEl cultivo con mayor rendimiento es: {mejor}")