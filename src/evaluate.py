import numpy as np
from scipy.io import loadmat
from skimage.transform import resize
from sklearn.metrics import adjusted_rand_score

# Load segmentation result
segmentation_path = "D:/6thsem/graph/segment_35049_k_100.npy"  # Update this path as needed
segmentation = np.load(segmentation_path)

# Ensure segmentation contains valid integer labels
segmentation = segmentation.astype(int)

# Load ground truth
ground_truth_path = "D:/6thsem/graph/data/ground_truth/test/35049.mat"
ground_truth_data = loadmat(ground_truth_path)

# Extract ground truth segmentations
# Each entry in "groundTruth" is a dictionary with "Segmentation" key
ground_truths = [entry[0][0][0]["Segmentation"] for entry in ground_truth_data["groundTruth"]]

results = []

for idx, ground_truth in enumerate(ground_truths):
    print(f"Processing ground truth {idx + 1}...")

    # Ensure ground truth is converted to a numpy array if not already
    if not isinstance(ground_truth, np.ndarray):
        ground_truth = np.array(ground_truth)

    # Check if ground truth contains valid integer labels
    if not np.issubdtype(ground_truth.dtype, np.integer):
        ground_truth = ground_truth.astype(int)

    # Ensure dimensions match
    if segmentation.shape != ground_truth.shape:
        print(f"Resizing segmentation to match ground truth {idx + 1} dimensions.")
        segmentation_resized = resize(
            segmentation,
            ground_truth.shape,
            order=0,  # Nearest neighbor interpolation
            preserve_range=True,
        ).astype(int)
    else:
        segmentation_resized = segmentation

    # Flatten arrays for ARI calculation
    segmentation_flat = segmentation_resized.flatten()
    ground_truth_flat = ground_truth.flatten()

    # Check for invalid values
    if np.isnan(segmentation_flat).any() or np.isnan(ground_truth_flat).any():
        print(f"Invalid values detected in ground truth {idx + 1}. Skipping...")
        continue

    # Compute ARI
    ari = adjusted_rand_score(ground_truth_flat, segmentation_flat)
    results.append(ari)
    print(f"Adjusted Rand Index with Ground Truth {idx + 1}: {ari}")

# Final results
if results:
    average_ari = sum(results) / len(results)
    print(f"Average Adjusted Rand Index across all ground truths: {average_ari}")
else:
    print("No valid evaluations could be performed.")
