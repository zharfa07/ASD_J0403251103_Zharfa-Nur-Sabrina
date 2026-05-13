# ========================================================== 
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B
# Praktikum 13 - Graph III: Spanning Tree
# ========================================================== 

# ========================================================== 
# Latihan 2 : Implementasi Sederhana Algoritma Kruskal
# ========================================================== 

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        
        mst.append((u, v, weight))
        total_weight += weight
        
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)


# Pertanyaan Analisis
# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    ==> 'C' dan 'D', karena memiliki bobot paling kecil yaitu 1

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    ==> karena agar total bobot MST menjadi minimum (terkecil)

# 3. Berapa total bobot MST yang dihasilkan?
#    ==> total bobot adalah 6 (1 + 2 + 3 = 6)

# 4. Mengapa edge tertentu tidak dipilih?
#    ==> karena dapat membentuk cycle atau siklus yang jalurnya sudah ada yang menghubungkan nodenya 