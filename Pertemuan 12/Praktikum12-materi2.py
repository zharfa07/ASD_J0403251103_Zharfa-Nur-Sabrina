# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Materi 2 : Implementasi Bellman Ford pada python
# ===================================================

def bellman_ford(graph, start): 
 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
 
    # Relaksasi berulang 
    for _ in range(len(graph) - 1): 
 
        for node in graph: 
 
            for neighbor, weight in graph[node].items(): 
 
                if distances[node] + weight < distances[neighbor]: 
 
                    distances[neighbor] = distances[node] + weight 
 
    return distances 

# Penjelasan :
# dalam algoritma Bellman Ford digunakan untuk mencari jarak terpendek dari satu titik ke semua titik lain
# dengan cara memeperbarui jarak secara berulang pada setiap jalur hingga mendapatkan hasil terkecil/terpendek