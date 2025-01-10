#creating graph and computing MST
import networkx as nx
import numpy as np

def create_graph(image):
    """Converts a grayscale or RGB image into a graph."""
    height, width = image.shape
    graph = nx.Graph()

    for i in range(height):
        for j in range(width):
            graph.add_node((i, j), intensity=image[i, j])

            # Add edges to neighbors (4-connectivity)
            if i > 0:  # Top neighbor
                weight = abs(int(image[i, j]) - int(image[i - 1, j]))  # Use RGB or intensity difference
                graph.add_edge((i, j), (i - 1, j), weight=weight)
            if j > 0:  # Left neighbor
                weight = abs(int(image[i, j]) - int(image[i, j - 1]))
                graph.add_edge((i, j), (i, j - 1), weight=weight)

    for u, v, data in graph.edges(data=True):
        print(f"Edge: {u} -> {v}, Weight: {data['weight']}")
    
    print(f"Graph created with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")
    return graph


def compute_mst(graph):
    """Computes the Minimum Spanning Tree (MST) of the graph."""
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    print(f"MST computed with {mst.number_of_edges()} edges.")
    return mst 
