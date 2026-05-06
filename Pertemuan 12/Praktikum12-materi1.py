# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Materi 1 : Implementasi Dijkstra dalam Phyton
# ===================================================

import heapq 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 

def dijkstra(graph, start): 
    # Menyimpan jarak minimum 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak node awal = 0 
    distances[start] = 0 
 
    # Priority queue 
    pq = [(0, start)] 
 
    while pq: 
        current_distance, current_node = heapq.heappop(pq) 
 
        # Periksa semua tetangga 
        for neighbor, weight in graph[current_node].items(): 
 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak lebih kecil 
            if distance < distances[neighbor]: 
 
                distances[neighbor] = distance 
 
                heapq.heappush(pq, (distance, neighbor)) 
 
    return distances 
 
hasil = dijkstra(graph, 'A') 
print(hasil) 


# Penjelasan : 
# • Jarak dari A ke A = 0  
# • Jarak dari A ke B = 4  
# • Jarak dari A ke C = 2  
# • Jarak dari A ke D = 3 
# Karena A ➔  C ➔  D = 2 + 1 = 3 

# Penjelasan :
# Dalam penggunaan Dijkstra dalam Python digunakan untuk mencari jarak yang terpendek
# dari satu titik ke titik lainnya, dengan memulai dari node A lalu secara bertahap memilih jalur
# dengan jarak terkecil/terpendek hingga menemukan hasil akhir seperti A ke D lebih cepat jika melewati C
# :
