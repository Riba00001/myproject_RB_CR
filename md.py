import numpy as np
import matplotlib.pyplot as plt

# Load data from the .xvg file
data = np.loadtxt("sasa.xvg", comments=['@', '#'])

# Extract residue numbers and corresponding average SASA values
residue_numbers = data[:, 0]
average_sasa = data[:, 1]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(residue_numbers, average_sasa, marker='o', color='purple', linestyle='None')
plt.xlabel('Residue Number')
plt.ylabel('Average SASA (nm²)')
plt.title('Average Solvent Accessible Surface Area (SASA) per Residue')
plt.show()
