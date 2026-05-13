# ========================================================== 
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B
# Praktikum 13 - Graph III: Spanning Tree
# ========================================================== 

# ========================================================== 
# Latihan 1 : Memahami Konsep Spanning Tree 
# ========================================================== 

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Pertanyaan Analisis
# Tuliskan jawaban sebagai komentar di bagian bawah program.
# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    ==> Pada graph awal memiliki semua edge yang ada, 
#        sedangkan spanning tree hanya mengambil beberapa edge yang cukup menguhubungkan semua node

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    ==> Spanning tree tidak boleh memiliki cycle yaitu agar lebih efisien, 
#        karena tujuannya adalah menghubungkan semua node dengan jalur paling sederhana tanpa perputaran

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    ==> karena pada spanning tree, edge yang tidak diperlukan akan dihapus agar tidak terbentuk cycle, 
#        untuk menjaga node agar tidak terjadi perputaran