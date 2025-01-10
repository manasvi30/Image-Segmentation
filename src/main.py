import cv2
import numpy as np
from graph_utils import create_graph, compute_mst
#from segmentation import segment_graph
from segmentation import segment_with_threshold
from visualization import create_segmented_image, display_image

# Load the image
#image_path = "../data/images/test/16068.jpg"  
#print("Loading image...")
#image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#print(f"Image loaded with shape: {image.shape}.")

# Load synthetic image
image_path = "D:/6thsem/graph/data/synthetic_checkerboard.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
print(f"Image loaded with shape: {image.shape}.")

# Step 1: Create a graph from the image
print("Creating graph...")
graph = create_graph(image)

# Step 2: Compute the Minimum Spanning Tree (MST)
print("Computing MST...")
mst = compute_mst(graph)

# Step 3: Segment the graph using a threshold
#threshold = 15  # Adjust this value for different results
#print("Segmenting graph...")
#segments = segment_graph(mst, threshold)

# Segment graph
for k in [400, 450, 475, 500]:
    print(f"Testing with k = {k}")
    segments = segment_with_threshold(mst, k)

    # Step 4: Visualize the results
    print("Creating segmented image...")
    segmented_image = create_segmented_image(image.shape, segments)
    print(f"Number of segments (k={k}): {len(segments)}")

    unique_intensities = np.unique(segmented_image)
    print("Unique intensities in segmented image:", unique_intensities)

    print("Displaying original and segmented images...")
    display_image(image, title="Original Image")
    display_image(segmented_image, title=f"Segmented Image (k={k})")
