"""a) Find the probability distribution of X and
     the cumulative distribution of X;
 (b) Find mean, mode and median of
    the number of cars arriving in a minute; 
(c) mean E[X 2], variance E[X3], standard deviation, skewness
    coefficient and kurtosis
    
    """

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Number of cars arriving in a minute
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#Probability corresponding to X
p = np.array([0.025, 0.075, 0.125, 0.150, 0.200, 0.275, 0.100, 0.050])

#Calculating all measures from task:
cdf=np.cumsum(p)
arithmetic_mean_x=np.sum(x)/len(x)
expected_value_x=np.sum(x*p)
mode_x=x[np.argmax(p)]
median_x=  x[np.where(cdf >= 0.5)[0][0]]

expected_value_x2=np.sum(x**2*p)
variance=expected_value_x2-expected_value_x**2
standard_deviation=np.sqrt(variance)
expected_value_x3=np.sum(x**3*p)
skewness=np.sum(((x - expected_value_x)**3) * p) / np.sqrt(variance)**3
kurtosis=np.sum(((x - expected_value_x)**4) * p) / np.sqrt(variance)**4

#Plotting
plt.figure(figsize=(10, 6))
plt.bar(x, p, color="skyblue", label="P(X)", alpha=0.8)
plt.bar(x, cdf,  label="CDF", width=0.4,color='purple', alpha=0.7)

# Add vertical lines for statistical measures
plt.axvline(arithmetic_mean_x, color='green', linestyle='--', label=f'Arithmetic Mean ≈ {arithmetic_mean_x:.2f}')
plt.axvline(expected_value_x, color='blue', linestyle='--', label=f'Expected Value ≈ {expected_value_x:.2f}')
plt.axvline(mode_x, color='orange', linestyle='--', label=f'Mode = {mode_x}')
plt.axvline(median_x, color='red', linestyle='--', label=f'Median = {median_x}')
# Display rest of values
stats_text = f"Expected Value X^2 ≈ {expected_value_x2:.2f}\nExpected Value X^3 ≈ {expected_value_x3:.2f}\nVariance ≈ {variance:.2f}\nSkewness ≈ {skewness:.2f}\nKurtosis ≈ {kurtosis:.2f}\nStandard deviation ≈ {standard_deviation:.2f}"
plt.text(0.7, 0.75, stats_text,
        fontsize=10,
        verticalalignment='top',
        horizontalalignment='left',
        bbox=dict(boxstyle='round', facecolor='white',edgecolor='lightGrey', alpha=0.8))


plt.title("Probability Distribution of Cars Arriving per Minute")
plt.xlabel("Number of Cars (X)")
plt.ylabel("Probability P(X)")
plt.xticks(x)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()