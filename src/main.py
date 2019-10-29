from sklearn.cluster import KMeans
from skimage import data, io, filters, color
import numpy as np
import matplotlib.pyplot as plt
import sys


image = io.imread(str(sys.argv[1]))
n_clusters = int(sys.argv[2])

image_xyz = color.rgb2xyz(image)
image_xyz = np.reshape(image_xyz, (-1, 3))

kmeans = KMeans(n_clusters).fit(image_xyz)

palettes = []

for cluster in kmeans.cluster_centers_:
    img = np.tile(cluster, (100, 100, 1))
    img = color.xyz2rgb(img)
    palettes.append(img)

palettes = np.hstack(palettes)

f1 = plt.figure(figsize=(8, 6))
ax1 = f1.add_subplot(212, frameon=False)
ax2 = f1.add_subplot(211, frameon=False)
ax1.set_axis_off()
ax2.set_axis_off()
ax1.imshow(palettes)
ax2.imshow(image)
plt.show()