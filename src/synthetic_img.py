import numpy as np
import cv2
import matplotlib.pyplot as plt

# Create a synthetic checkerboard image
def create_checkerboard(size=8, square_size=1):
    pattern = np.indices((size, size)).sum(axis=0) % 2  # Alternating 0s and 1s
    pattern = pattern * 255  # Scale to 0-255
    image = np.kron(pattern, np.ones((square_size, square_size)))  # Enlarge squares
    return image.astype(np.uint8)

# Save the synthetic image
checkerboard = create_checkerboard()
cv2.imwrite("../data/synthetic_checkerboard.jpg", checkerboard)

# Display the image
plt.imshow(checkerboard, cmap='gray')
plt.title("Synthetic Checkerboard")
plt.axis('off')
plt.show()
