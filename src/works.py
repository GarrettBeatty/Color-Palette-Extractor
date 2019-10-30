from sklearn.cluster import KMeans
from skimage import data, io, filters, color
import numpy as np
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d import Axes3D


image = io.imread(str(sys.argv[1]))
n_clusters = int(sys.argv[2])

image_xyz = color.rgb2xyz(image)
image_rgb = image
image_xyz = np.reshape(image_xyz, (-1, 3))
image_rgb = np.reshape(image_rgb, (-1, 3))
colors = image_rgb / 255
points = np.arange(0, image_rgb.shape[0], 50)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(image_xyz[points, 0], image_xyz[points, 1], image_xyz[points, 2], c=colors[points])

plt.show()