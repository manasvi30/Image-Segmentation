# Graph-Based Image Segmentation

A Python implementation of the Felzenszwalb and Huttenlocher algorithm for image segmentation using graph-based methods. This project was part of COMP 323 coursework.

##  Project Objectives
- Implement and analyze a **graph-based image segmentation** method.
- Utilize **Minimum Spanning Tree (MST)** principles to group similar pixels.
- Evaluate segmentation results against ground truth using **Adjusted Rand Index (ARI)**.

##  How It Works
1. Each pixel is treated as a **node** in a graph.
2. Edges represent **pixel similarity** (based on intensity differences).
3. Construct MST using edge weights to connect similar pixels.
4. Apply a **dynamic threshold (k)** to control segmentation granularity.
5. Evaluate against BSDS500 dataset using ARI.

##  Setup Instructions

###  Python Environment
- Python 3.x
- Set up using `venv`

###  Dependencies
```bash
pip install numpy networkx scikit-learn matplotlib opencv-python scipy
