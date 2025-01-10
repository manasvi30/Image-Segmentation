#segmenting the image
import networkx as nx
import numpy as np

def segment_graph(mst, threshold):
    """Segments the graph by removing edges above the threshold."""
    edges_to_remove = []

    #collect edges to remove
    for u, v, data in mst.edges(data=True):
        if data['weight'] > threshold:
            edges_to_remove.append((u, v))

    #remove edges after iteration
    mst.remove_edges_from(edges_to_remove)
    print(f"Removed {len(edges_to_remove)} edges with weights above {threshold}.")
    # Extract connected components (segments)
    segments = list(nx.connected_components(mst))
    print(f"Number of segments created: {len(segments)}.")
    return segments

def compute_internal_difference(components, mst):
    """Computes the internal difference for each connected component."""
    internal_diff = {}
    for component in components:
        edges = [(u, v, data['weight']) for u, v, data in mst.edges(component, data=True)]
        max_weight = np.mean([data[2] for data in edges]) if edges else 0
        internal_diff[frozenset(component)] = max_weight
        print("Internal differences for components:")
        for component, diff in internal_diff.items():
            print(f"Component: {component}, Internal Difference: {diff}")
    return internal_diff

def segment_with_threshold(mst, k):
    """Segments the MST graph using a dynamic threshold."""
    components = list(nx.connected_components(mst))
    internal_diff = compute_internal_difference(components, mst)
    edges_to_remove = []
    scaled_k = k / np.max([data['weight'] for u, v, data in mst.edges(data=True)])


    for u, v, data in mst.edges(data=True):
        weight = data['weight']
        comp_u = next(comp for comp in components if u in comp)
        comp_v = next(comp for comp in components if v in comp)

        threshold_u = internal_diff[frozenset(comp_u)] + scaled_k / len(comp_u)
        threshold_v = internal_diff[frozenset(comp_v)] + scaled_k / len(comp_v)

        print(f"Edge: {u} -> {v}, Weight: {weight}, Threshold U: {threshold_u}, Threshold V: {threshold_v}")

        if weight > min(threshold_u, threshold_v):
            edges_to_remove.append((u, v))

    mst.remove_edges_from(edges_to_remove)
    segments = list(nx.connected_components(mst))
    print(f"Number of segments (k={k}): {len(segments)}")  # Expected: 64 for proper k

    return segments
