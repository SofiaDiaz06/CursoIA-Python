# IA - Python

Proyecto académico de Inteligencia Artificial.

## Tecnologías

- Python
- Docker
- Docker Compose
- Git
- GitHub

## Ejecución

```bash
docker compose build
docker compose up
```

## Detener

```bash
docker compose down
```

# Sistema de recomendacion de productos de autocuidado

## Problematica Local
En Cartago, no hay una herramienta o guia accesible para consultar productos de cuidado personal según el presupuesto y la efectividad real. Esto lleva a las personas a comprar a ciegas, gastando de mas en productos poco adecuados para sus necesidades.

## Objetivo del Proyecto
Desarrollar un sistema en python que procese un catalogo de productos de autocuidado disponibles, permitiendo analizar precios, calificaciones de usuarios y recomendar las mejores opciones para el presupuesto de cada persona.

## Estructura de Datos
El proyecto utiliza un archivo CSV (`datos_autocuidado.csv`) con las columnas:
- `id_producto`: Identificador.
- `nombre`
- `precio`
- `calificacion_cliente`: Calificacion de 1 a 5

## Estado del Proyecto
- Archivo `cargar_datos.py` funcional con lectura de CSV y generación de estadisticas basicas (promedios,minimos y maximos).
