```markdown
# Visualisasi Graf dengan Python

Proyek ini adalah implementasi sederhana untuk memodelkan graf menggunakan pustaka **NetworkX** dan **matplotlib** di Python. Proyek ini menyediakan fitur untuk menambah node, menambah edge dengan bobot, memvisualisasikan graf, menghitung jalur terpendek, serta menyediakan fungsi tambahan seperti memeriksa konektivitas graf.

## Fitur

1. **Menambah Node dan Edge**  
   - Anda dapat menambahkan node ke graf.  
   - Anda juga dapat menambahkan edge antara dua node dengan bobot tertentu (default = 1).  

2. **Visualisasi Graf**  
   - Menampilkan graf dengan tata letak spring layout.  
   - Menampilkan bobot edge di dalam graf.  

3. **Jalur Terpendek**  
   - Menghitung jalur terpendek berdasarkan bobot edge menggunakan algoritma bawaan NetworkX.  
   - Memvisualisasikan jalur terpendek dengan menyorot edge yang termasuk jalur tersebut.

4. **Fungsi Tambahan**  
   - Menampilkan derajat tiap node.  
   - Mengecek apakah graf terhubung (connected).  
   - Mengecek apakah graf berarah (directed).  
   - Mengecek apakah dua node bertetangga langsung.  
   - Menemukan semua tetangga dari suatu node tertentu.  

## Instalasi

1. Pastikan Python versi 3.6 atau lebih baru sudah terinstal di sistem Anda.
2. Instal pustaka yang diperlukan:
   ```bash
   pip install networkx matplotlib
   ```

## Cara Penggunaan

1. Jalankan skrip Python berikut di editor atau terminal:
   ```python
   import networkx as nx
   import matplotlib.pyplot as plt

   print(nx.__version__)

   # Implementasi kelas Graf (lihat file `graph.py` untuk kode lengkap)
   graph = Graf()

   # Menambah node
   graph.add_node(1)
   graph.add_node(2)
   graph.add_node(3)
   graph.add_node(4)
   graph.add_node(5)

   # Menambah edge
   graph.add_edge(1, 2, weight=4.5)
   graph.add_edge(1, 3, weight=3.2)
   graph.add_edge(2, 4, weight=2.7)
   graph.add_edge(3, 4, weight=1.8)
   graph.add_edge(1, 4, weight=6.7)
   graph.add_edge(3, 5, weight=2.7)

   # Visualisasi graf
   graph.visualize_graph()

   # Jalur terpendek
   print("Jalur terpendek dari 1 ke 5:", graph.shortest_path(1, 5),"\n")

   # Visualisasi jalur terpendek
   graph.visual_shortest_path(1, 5)

   # Metode tambahan
   print("Derajat tiap node:", graph.node_degrees(),"\n")
   print("Apakah graf ini terhubung/connected?", graph.is_connected(),"\n")
   print("Apakah graf ini berarah?", graph.is_directed(),"\n")
   print("Apakah node 1 dan 3 bertetangga langsung?", graph.are_adjacent(1, 3),"\n")
   print("Tetangga node 3:", graph.neighbors(3),"\n")
   ```

2. Hasil eksekusi akan menampilkan visualisasi graf, informasi tentang jalur terpendek, dan berbagai detail tambahan tentang graf.

## Contoh Hasil Eksekusi

- **Visualisasi Graf**  
  Menampilkan graf dengan node dan edge, lengkap dengan bobot.  

- **Jalur Terpendek**  
  Jalur terpendek dari node 1 ke node 5 ditampilkan dalam bentuk daftar node yang dilalui, serta divisualisasikan di graf.  

- **Informasi Tambahan**  
  - Derajat tiap node.  
  - Konektivitas graf.  
  - Informasi tentang tetangga dari node tertentu.  

## Kebutuhan Sistem

- Python 3.6 atau lebih baru.  
- Pustaka Python:
  - `networkx`
  - `matplotlib`
