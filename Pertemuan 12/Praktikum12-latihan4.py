# Nama : Zharfa Nur Sabrina
# NIM : J0403251103
# Kelas : TPL B
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# ========================================================== 

import heapq 

# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
    'Perpustakaan': {'Lab': 3}, 
    'Kantin': {'Lab': 4, 'Aula': 7}, 
    'Lab': {'Aula': 1}, 
    'Aula': {} 
} 
def dijkstra(graph, start): 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
    
    priority_queue = [(0, start)] 
    
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
        
        if current_distance > distances[current_node]: 
            continue 
        
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
        
        if distance < distances[neighbor]: 
            distances[neighbor] = distance 
            heapq.heappush(priority_queue, (distance, neighbor)) 
    return distances 

hasil = dijkstra(graph, 'Gerbang') 

print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit") 


# Pertanyaan Analisis 
# Tuliskan jawaban sebagai komentar di bagian bawah program. 
# Jawaban Analisis: 
# 1. Lokasi mana yang paling dekat dari Gerbang? 
#    -> kantin (2 menit)
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? 
#    -> gerbang - kantin - lab - aula = 2 + 4 + 1 = 7 menit
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. 
#    -> tidak, karena jalur langsung belum tentu menghasilkan jarak paling kecil jika total waktunya lebih besar dibanding dengan jalur lain
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini? 
#    -> karena semua bobot berupa waktu (positif), sehingga dijkstra bisa menghitung jalur tercepat dengan akurat dan efisien