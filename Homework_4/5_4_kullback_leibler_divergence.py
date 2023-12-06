import numpy as np
from scipy.stats import norm

# Function to compute KL divergence between two normal distributions
def kl_divergence(mu1, sigma1, mu2, sigma2, sample_size=100000):
    # Generate samples from the two normal distributions
    samples_f = np.random.normal(mu1, sigma1, sample_size)

    # Evaluate the PDFs of the normal distributions
    pdf_f = norm.pdf(samples_f, mu1, sigma1)
    pdf_g = norm.pdf(samples_f, mu2, sigma2)

    # Compute the sample-based estimate of the KL divergence
    kl_estimate = np.mean(np.log(pdf_f / pdf_g))

    return kl_estimate

# Parameters of the normal distributions
mu1, sigma1 = 1.0, 1.0
mu2, sigma2 = 2.0, 3.0

# Theoretical result of KL divergence
theoretical_kl = 0.5 * ((sigma1**2) / (sigma2**2) + ((mu1 - mu2)**2) / (sigma2**2) - 1 + np.log(sigma2**2 / sigma1**2))

# Monte Carlo estimate of KL divergence
mc_estimate = kl_divergence(mu1, sigma1, mu2, sigma2)

# Print the results
print(f"Theoretical KL Divergence: {theoretical_kl}")
print(f"Monte Carlo Estimate: {mc_estimate}")

# Results
# Theoretical KL Divergence: 0.7097233997792209
# Monte Carlo Estimate: 0.7089208434002601