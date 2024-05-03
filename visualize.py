"""visualization of clusters"""
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import main

warnings.filterwarnings("ignore")
matplotlib.use('QtAgg', force=True)
kmeans = main.KMeans(main.read_file('test.csv'), 3)
kmeans.compute()
data_raw = kmeans.clusters
data = {}

for key, val in data_raw.items():
    data[key] = np.array(val, dtype=float)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each point
for key, value in data.items():
    ax.scatter(value[:,0], value[:,1], value[:,2], label=key)

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot')
ax.legend()

# Show plot
plt.show()
