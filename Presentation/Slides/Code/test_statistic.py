import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the test statistic (TS) for a given dataset
def calculate_ts(data, null_hypothesis_mean):
    observed_mean = np.mean(data)
    ts = 2 * np.log(observed_mean / null_hypothesis_mean)
    return ts

# Function to simulate the null distribution
def simulate_null_distribution(null_hypothesis_mean, num_simulations, sample_size):
    ts_values = []
    for _ in range(num_simulations):
        simulated_data = np.random.poisson(null_hypothesis_mean, sample_size)
        ts = calculate_ts(simulated_data, null_hypothesis_mean)
        ts_values.append(ts)
    return np.array(ts_values)

# Function to compute the p-value from the observed TS and the null distribution
def compute_p_value(observed_ts, null_distribution):
    p_value = np.sum(null_distribution >= observed_ts) / len(null_distribution)
    return p_value

# Parameters
null_hypothesis_mean = 5
sample_size = 100
num_simulations = 10000
observed_data = np.random.poisson(6, sample_size)  # Example observed data with a mean different from null hypothesis

# Calculate the observed TS
observed_ts = calculate_ts(observed_data, null_hypothesis_mean)

# Simulate the null distribution
null_distribution = simulate_null_distribution(null_hypothesis_mean, num_simulations, sample_size)

# Compute the p-value
p_value = compute_p_value(observed_ts, null_distribution)

print(f"Observed TS: {observed_ts}")
print(f"P-value: {p_value}")

# Plotting the null distribution and observed TS
plt.hist(null_distribution, bins=50, alpha=0.75, label='Null Distribution')
plt.axvline(observed_ts, color='r', linestyle='dashed', linewidth=2, label='Observed TS')
plt.xlabel('Test Statistic (TS)')
plt.ylabel('Frequency')
plt.legend()
plt.title('Null Distribution of Test Statistic')
plt.show()
