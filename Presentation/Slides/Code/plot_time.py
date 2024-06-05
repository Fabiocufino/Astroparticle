import numpy as np
import matplotlib.pyplot as plt

# Define the function based on the given equation
def TS(t_i, T_0, T_W):
    return (1 / np.sqrt(2 * np.pi * (T_W / 2)**2)) * np.exp(-((t_i - T_0)**2) / (2 * (T_W / 2)**2))

# Generate data points
t_i = np.linspace(-10, 10, 400)  # Change the range and number of points as needed
T_0 = 0  # Center of the distribution
T_W = 4  # Width of the distribution

# Calculate the function values
TS_values = TS(t_i, T_0, T_W)

# Plot the function
plt.figure(figsize=(6, 3))
plt.plot(t_i, TS_values, label=r'$TS(t_i; T_0, T_W)$', linewidth=4)
plt.xlabel('$t_i$', fontsize=24)
plt.ylabel('TS$(t_i; T_0, T_W)$', fontsize=24)
plt.tight_layout()
plt.savefig('../Images/TS_plot_gauss.png')
plt.show()





# Define the piecewise function based on the given equation
def TS(t_i, T_0, T_W):
    TS_values = np.zeros_like(t_i)
    within_range = (t_i > T_0 - T_W / 2) & (t_i < T_0 + T_W / 2)
    TS_values[within_range] = 1 / T_W
    return TS_values

# Generate data points
t_i = np.linspace(-10, 10, 400)  # Change the range and number of points as needed
T_0 = 0  # Center of the distribution
T_W = 4  # Width of the distribution

# Calculate the function values
TS_values = TS(t_i, T_0, T_W)

# Plot the function
plt.figure(figsize=(6, 3))
plt.plot(t_i, TS_values, label=r'$TS(t_i; T_0, T_W)$', linewidth=4)
plt.xlabel(r'$t_i$', fontsize=24)
plt.ylabel(r'$TS(t_i; T_0, T_W)$', fontsize=24)
plt.tight_layout()
plt.savefig('../Images/TS_plot_box.png')
plt.show()
