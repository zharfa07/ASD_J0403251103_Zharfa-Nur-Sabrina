# Nama : Zharfa Nur Sabrina
# NIM : J0403251103
# Kelas : TPL B
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 5: Studi Kasus dengan Program Shortest Path
# ========================================================== 

import heapq

graph = {
    'Bogor' : {'Jakarta' : 5, 'Depok' : 2},
    'Depok' : {'Jakarta' : 2, 'Bandung' : 6},
    'Jakarta' : {'Bandung' : 7},
    'Bandung' : {}
}

def dijkstra(graph, start):
    #inisialisasi jarak awal 
    distances = {node: float('inf') for node in graph}
    
    # jarak ke node awal = 0
    distances[start] = 0
    
    # priority queue
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # skip jika bukan jarak terbaik
        if current_distance > distances[current_node]:
            continue
        
        # cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # update jika lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# node awal
start_node = 'Bogor'

# menjalankan algoritma
hasil = dijkstra(graph, start_node)

# output
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")

# Pertanyaan Analisis 
# Jawaban Analisis: 
# 1. Node awal yang digunakan apa? 
#    -> Bogor
# 2. Node mana yang memiliki jarak paling kecil dari node awal? 
#    -> Depok : 2
# 3. Node mana yang memiliki jarak paling besar dari node awal? 
#    -> Bandung : 8
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat. 
#    -> dijkstra bekerja memilih jalur dari bogor yang terkecil dulu (ke arah depok),
#       lalu mengecek jlaur lainnya dan memperbarui jarak sampai semua kota mendapatkan jarak terpendek 