import networkx as nx
import matplotlib.pyplot as plt

print(nx.__version__)

class Graf:
    def __init__(self):
        self.graph = nx.Graph()
        self.pos = None  

    def add_node(self, node):
        """Menambah node ke graf."""
        self.graph.add_node(node)

    def add_edge(self, u, v, weight=1):
        """Menambah edge dengan bobot (default = 1)."""
        self.graph.add_edge(u, v, weight=weight)

    def visualize_graph(self):
        """Menampilkan visualisasi graf."""
        if self.pos is None:
            self.pos = nx.spring_layout(self.graph) 
        weights = nx.get_edge_attributes(self.graph, 'weight')
        plt.figure("Graph Visualization")
        nx.draw(self.graph, self.pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12)
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=weights)
        plt.show()

    def shortest_path(self, start, end):
        """Menghitung jalur terpendek berdasarkan bobot."""
        try:
            return nx.shortest_path(self.graph, source=start, target=end, weight='weight')
        except nx.NetworkXNoPath:
            return f"Tidak ada jalur antara {start} dan {end}."

    def visual_shortest_path(self, start, end):
        """Menampilkan visualisasi jalur terpendek."""
        try:
            path = self.shortest_path(start, end)

            if isinstance(path, str):  
                print(path)
                return

            edges_in_path = list(zip(path[:-1], path[1:]))

            if self.pos is None:
                self.pos = nx.spring_layout(self.graph)  
            weights = nx.get_edge_attributes(self.graph, 'weight')
            
            plt.figure("Shortest Path Visualization")
            nx.draw(self.graph, self.pos, with_labels=True, node_color='lightblue', node_size=700, font_size=12)
            nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=weights)

            nx.draw_networkx_edges(self.graph, self.pos, edgelist=edges_in_path, edge_color='red', width=2)
            plt.show()
        except nx.NetworkXNoPath:
            print(f"Tidak ada jalur antara {start} dan {end}.")

    # Metode tambahan
    def node_degrees(self):
        """Menampilkan derajat semua node."""
        return dict(self.graph.degree())

    def is_connected(self):
        """Check if the graph is connected (all nodes are reachable)."""
        return nx.is_connected(self.graph)

    def is_directed(self):
        """Mengecek apakah graf berarah."""
        return self.graph.is_directed()

    def are_adjacent(self, u, v):
        """Mengecek apakah dua node bertetangga langsung."""
        return self.graph.has_edge(u, v)

    def neighbors(self, node):
        """Menemukan semua tetangga dari node tertentu."""
        return list(self.graph.neighbors(node))

# Implementasi
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
