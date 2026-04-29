# lifo tumpukan stack# ===================================================
# Nama  : Zharfa Nur Sabrina
# NIM   : J0403251103
# Kelas : TPL B2
# ===================================================

# ===================================================
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur)
# ===================================================

graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
} 

def dfs(graph, node, visited):
    # fungsi untuk melakukan penelusuran graph menggunakan DFS
    # graph : dictionary yang menyimpan graph
    # node : menyimpan node yang sedang dikunjungi
    # visited : menyimpan node yang sudah dikunjungi


    # tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    # tampilkan node yang sedang dikunjungi 
    print(node, end=" ")

    # periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

        # jika tetangga belum pernah dikunjungi
        if neighbor not in visited :
            # lakukan dfs sevcara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

# set visited 
visited = set()

# menjalankan dfs dari A 
print("DFS dari A:") 
dfs(graph, 'A', visited) 


# Pertanyaan Analisis 
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
#     -> Karena DFS menggunakan konsep rekursi (stack), jadi melanjutkan ke node berikutnya sampai tidak ada cabang lagi 
#        (masuk sedalam mungkin terlebih dahulu)
# 2. Apa yang terjadi jika urutan neighbor diubah?  
#     -> Jika urutan neighbor diubah, maka hasil urutan DFS akan berubah mengikuti urutan neighbor yang diubah
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama. 
#     -> DFS: menelusuri sampai dalam dulu 
#        ==> DFS: A B D E C F
#     -> BFS: menelusuri per level 
#        ==> BFS: A B C D E F