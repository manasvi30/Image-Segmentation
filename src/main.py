import cv2
import numpy as np
from graph_utils import create_graph, compute_mst
#from segmentation import segment_graph
from segmentation import segment_with_threshold
from visualization import create_segmented_image, display_image

# Load the image
image_path = "D:/6thsem/graph/data/images/test/35049.jpg"  
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError(f"Image not found at {image_path}")
print(f"Original Image loaded with shape: {image.shape}.")
# Resize the image
scale_factor = 2  # Adjust this factor as needed
height, width = image.shape
image = cv2.resize(image, (width // scale_factor, height // scale_factor))
print(f"Resized Image Shape: {image.shape}.")

# Load synthetic image
#image_path = "D:/6thsem/graph/data/vertical_stripes.jpg"
#image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#if image is None:
#    raise FileNotFoundError(f"Image not found at {image_path}")
#print(f"Image loaded with shape: {image.shape}.")

# Normalize the image
image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Proceed with graph creation
print("Image Normalized.")

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
'''
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
    '''

try:
    k = int(input("Enter a value for k(segmentation parameter): "))
    print(f"Segmenting graph with k={k}...")
    segments = segment_with_threshold(mst, k)
    segmented_image = create_segmented_image(image.shape, segments)
     # Display segment details
    print(f"Number of segments created: {len(segments)}")
    for idx, segment in enumerate(segments):
        print(f"Segment {idx + 1}: Size = {len(segment)} pixels")

    display_image(image, title="Original Image")
    display_image(segmented_image, title=f"Segmented Image (k={k})")

    segment_labels = np.zeros(segmented_image.shape, dtype=np.int32)

    for label, segment in enumerate(segments, start=1):
        for pixel in segment:
            segment_labels[pixel] = label


    # Optional: Save segmented image
    save_option = input("Save segmented image? (y/n): ").strip().lower()
    if save_option == 'y':
        save_path = f"segmented_image_k_{k}.png"
        cv2.imwrite(save_path, segmented_image)
        print(f"Segmented image saved at {save_path}")
        # Save segment labels
        save_path_labels = f"segment_labels_k_{k}.npy"
        np.save(save_path_labels, segment_labels)
        print(f"Segment labels saved at {save_path_labels}")

except ValueError:
    print("Invalid input for k.")
