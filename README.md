# Algoritmo de Dijkstra

Implementacion del algoritmo de Dijkstra para calcular los caminos minimos desde un vertice origen hacia todos los demas vertices de un grafo dirigido con pesos positivos.

## Lenguaje

Python 3

## Descripcion

El programa utiliza:

- Lista de adyacencia para representar el grafo.
- Cola de prioridad (heapq) para seleccionar el vertice con menor distancia.
- Medicion del tiempo de ejecucion mediante la libreria time.

## Entrada

La entrada debe tener el siguiente formato:

```
n m
u1 v1 w1
u2 v2 w2
...
um vm wm
s
```

Donde:

- n = numero de vertices
- m = numero de aristas
- u = vertice origen
- v = vertice destino
- w = peso de la arista
- s = vertice origen para Dijkstra

## Ejemplo de entrada

```
5 6
0 1 10
0 2 3
1 2 1
2 1 4
2 3 2
3 4 7
0
```

## Ejemplo de salida

```
0 -> 0: 0
0 -> 1: 7
0 -> 2: 3
0 -> 3: 5
0 -> 4: 12

Tiempo de ejecucion: 0.000123 segundos
```

## Complejidad

Utilizando lista de adyacencia y cola de prioridad:

```
O((V + E) log V)
```

donde:

- V = numero de vertices
- E = numero de aristas

Ingenieria Informatica
Universidad Tecnica de Oruro
