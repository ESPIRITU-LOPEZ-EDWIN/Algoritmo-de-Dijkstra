import heapq
import sys
import time

input = sys.stdin.readline
INF = float('inf')

def dijkstra(adj, n, s):
    dist = [INF] * n
    dist[s] = 0
    cola = [(0, s)]

    while cola:
        d, u = heapq.heappop(cola)

        if d > dist[u]:
            continue

        for arista in adj[u]:
            v = arista[0]
            w = arista[1]

            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(cola, (dist[v], v))

    return dist


#inicio de medicion
inicio = time.perf_counter()

n, m = map(int, input().split())

adj = []
for i in range(n):
    adj.append([])

for i in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

s = int(input())

dist = dijkstra(adj, n, s)

for i in range(n):
    if dist[i] == INF:
        print(f"{s} -> {i}: INF")
    else:
        print(f"{s} -> {i}: {dist[i]}")

#fin de medicion
fin = time.perf_counter()

print(f"\nTiempo de ejecucion: {fin - inicio:.6f} segundos")
