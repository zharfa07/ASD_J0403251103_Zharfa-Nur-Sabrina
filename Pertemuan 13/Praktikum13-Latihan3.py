# ========================================================== 
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B
# Praktikum 13 - Graph III: Spanning Tree
# ========================================================== 

# ========================================================== 
# Latihan 3 : Implementasi Algorima Prim
# ========================================================== 

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])

    edges = []
    
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    
    mst = []
    total_weight = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v)
            
            mst.append((u, v, weight))
            total_weight += weight
            
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# Pertanyaan Analisis:
# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    ==> node A

# 2. Edge mana yang dipilih pertama kali?
#    ==> (A, C, 2) karena bobot terkecil dari node A

# 3. Bagaimana Prim menentukan edge berikutnya?
#    ==> Prim menentukan edge berikutnya dengan memilih edge yang berbobot paling kecil 
#        yang menghubungkan dengan node yang sudah dikunjungi ke node yang belum dikunjungi

# 4. Berapa total bobot MST yang dihasilkan?
#    ==> 6, (2 + 1 + 3 = 6)

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    ==> Prim memulai dari satu node (node awal) lalu menambahkan edge terdekat secara bertahap, 
#        sedangkan kruskal langsung memilih edge terkecil dari seluruh graph tanpa melihat node awal