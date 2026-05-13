# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B
# Praktikum 13 - Graph III: Spanning Tree

# ========================================================== 
# Implementasi Prim 
# ========================================================== 

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    visited = set([start]) #menyimpan node yang sudah dikunjungi 

    edges = [] #menyimpan edge

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges) #(bobot terkecil)
        
        if v not in visited: #cek jika node tujuan belum dikunjungi
                
                visited.add(v)
                
                mst.append((u, v, weight))
                total_weight += weight
                
                # memasukkan edge ke node baru
                for neighbor, w in graph[v].items():
                    if neighbor not in visited:
                        heapq.heappush(edges, (w, v, neighbor))
        
        return mst, total_weight #mengembalikan hasil mst dan bobot total
    mst, total = prim(graph, 'A')

    print("Minimum Spanning Tree:")
    
    for edge in mst:
        print(edge)
    
    print("Total bobot =", total)


# - penjelasan tambahan - 
# program menggunakan algoritma prim untuk mencari mst dengan cara memilih edge bobot terkecil,
# dari node yang sudah dikunjungi ke node yang belum dikunjungi, 
# jadi semua node pada graph terhubung dengan bobot minimum