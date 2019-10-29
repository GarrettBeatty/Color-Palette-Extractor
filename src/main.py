from sklearn.cluster import KMeans
from skimage import data, io, filters, color
import numpy as np
import matplotlib.pyplot as plt


image = io.imread("et.jpeg")
image_xyz = color.rgb2xyz(image)
image_xyz = np.reshape(image_xyz, (-1, 3))
n_clusters = 4

kmeans = KMeans(n_clusters).fit(image_xyz)

palettes = []

for cluster in kmeans.cluster_centers_:
    img = np.tile(cluster, (100, 100, 1))
    img = color.xyz2rgb(img)
    palettes.append(img)

palettes = np.hstack(palettes)
plt.imshow(palettes)
plt.axis('off')
plt.tight_layout(True)
plt.show()