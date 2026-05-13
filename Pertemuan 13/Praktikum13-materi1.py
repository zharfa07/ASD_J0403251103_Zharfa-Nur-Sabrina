# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B
# Praktikum 13 - Graph III: Spanning Tree

# ========================================================== 
# Implementasi Kruskal
# ========================================================== 

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot (terkecil ke besar)
edges.sort()

mst = [] #menyimpan hasil mst
total_weight = 0 #total bobot mst

# Set sederhana untuk node yang sudah dipilih
connected = set() 

for weight, u, v in edges: #cek setiap edge

    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight)) #menambahkan edge ke mst
        total_weight += weight #menambahkan edge ke total

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)


# - penjelasan tambahan - 
# menggunakan MST dengan mengurutkan semua edge berdasarkan bobot terkecil, 
# lalu memilih edge satu per satu selama tidak membentuk cycle, 
# jadi semua node dapat terhubung dengan total bobt minimum sebesar 6
