import numpy as np
import matplotlib.pyplot as plt

# File path to your band data file
file_path = 'band.dat'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.readlines()

# Initialize lists to store k-points and energy bands
k_points = []
energy_bands = []

# Parsing the file
for i, line in enumerate(content):
    # K-points are on every 6th line starting from the 2nd line
    if (i - 1) % 6 == 0:
        k_points.append([float(val) for val in line.split()])
    # Energy bands follow each k-point line, capture all band energies
    elif (i - 2) % 6 == 0 or (i - 3) % 6 == 0 or (i - 4) % 6 == 0 or (i - 5) % 6 == 0:
        energy_bands.extend([float(val) for val in line.split()])

# Reshape energy bands correctly (assuming 28 bands from metadata)
num_bands = 1488
energy_bands = np.array(energy_bands).reshape(-1, num_bands)

# Calculate the distances between consecutive k-points for the x-axis
k_distances = [np.linalg.norm(np.array(k_points[i]) - np.array(k_points[i-1])) for i in range(1, len(k_points))]
k_distances = np.insert(np.cumsum(k_distances), 0, 0)  # Insert 0 at the beginning

# Plot the band structure
plt.figure(figsize=(8, 6))
for band in range(num_bands):
    plt.plot(k_distances, energy_bands[:, band], color='blue', linewidth=1)

plt.xlabel('K-point distance')
plt.ylabel('Energy (eV)')
plt.title('Band Structure')
plt.grid(True)
plt.show()

