#visualizing results
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import mark_boundaries

def create_segmented_image(image_shape, segments):
    """Creates a segmented image from the segments."""
    segmented_image = np.zeros(image_shape, dtype=np.uint8)

    for idx, segment in enumerate(segments):
        for pixel in segment:
            segmented_image[pixel] = int((idx + 1) * 255 / len(segments))  # Scale intensity

    #unique_intensities = np.unique(segmented_image)
    #print("Unique intensities in segmented image:", unique_intensities)

    return segmented_image

def display_image(image, title="Image"):
    """Displays an image using matplotlib."""
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def display_segmented_boundaries(original_image, segments):
    """Displays the original image with segment boundaries overlaid."""
    boundary_image = mark_boundaries(original_image, segments)
    plt.imshow(boundary_image)
    plt.title("Segmented Boundaries")
    plt.axis('off')
    plt.show()

