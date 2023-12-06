import numpy as np
from scipy.stats import pearsonr


num_experiments = 10
observed_corr = 0.3
num_samples = 100000

# Randomly generate data
random_data = np.random.rand(num_samples, num_experiments)

# Simulated correlation coefficients
simulated_corrs = [pearsonr(random_data[i], np.random.rand(num_experiments))[0] for i in range(num_samples)]

# Compute the simulated p-value
simulated_p_value = np.mean(np.abs(simulated_corrs) >= np.abs(observed_corr))

print(f"Simulated p-value: {simulated_p_value}")

# Results
# Simulated p-value: 0.39302