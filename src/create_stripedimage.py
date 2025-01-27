import numpy as np
import cv2
import matplotlib.pyplot as plt

def create_striped_pattern(width, height, stripe_width, orientation='vertical'):
    """Creates a striped pattern."""
    if stripe_width <= 0 or width <= 0 or height <= 0:
        raise ValueError("Width, height, and stripe_width must be positive integers.")
    if orientation == 'vertical':
        # Create vertical stripes
        pattern = np.tile(np.arange(0, width, stripe_width) % 2, (height, stripe_width))
        pattern = (pattern[:height, :width] * 255).astype(np.uint8)
    elif orientation == 'horizontal':
        # Create horizontal stripes
        pattern = np.tile(np.arange(0, height, stripe_width) % 2, (stripe_width, width)).T
        pattern = (pattern[:height, :width] * 255).astype(np.uint8)
    else:
        raise ValueError("Orientation must be 'vertical' or 'horizontal'.")
    
    return pattern

# Generate patterns
vertical_stripes = create_striped_pattern(width=16, height=8, stripe_width=2, orientation='vertical')
horizontal_stripes = create_striped_pattern(width=8, height=16, stripe_width=2, orientation='horizontal')

# Save images
cv2.imwrite("D:/6thsem/graph/data/vertical_stripes.jpg", vertical_stripes)
cv2.imwrite("D:/6thsem/graph/data/horizontal_stripes.jpg", horizontal_stripes)

# Display patterns
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(vertical_stripes, cmap='gray')
plt.title("Vertical Stripes")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(horizontal_stripes, cmap='gray')
plt.title("Horizontal Stripes")
plt.axis('off')

plt.show()
