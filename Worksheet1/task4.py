import numpy as np
import matplotlib.pyplot as plt

data=np.array([2.3, 1.8, 3.1, 2.5, 2.9, 1.5, 2.7, 2.2, 3.0, 2.4, 1.9, 2.6, 2.8, 2.1, 3.2, 2.0, 1.7, 2.5, 2.3, 2.9, 3.3, 1.6, 2.4, 2.7, 2.2, 2.8, 1.8, 3.0, 2.1, 2.5, 1.9, 2.6, 2.0, 3.1, 2.3, 2.7, 1.5, 2.4, 2.9, 2.2])
n=len(data)

mean=np.sum(data)/n
std_dev=np.sqrt(np.sum((data-mean)**2)/(n-1))


#using this table https://highered.mheducation.com/sites/dl/free/0070980357/684814/t_distribution_table.pdf, we obtain the critical value:
#degree of freedom in t-distribution is n-1 thus 39 in this case


crit_value_std=1.960
crit_value_t=2.023
margin_of_error_std=crit_value_std*(std_dev/np.sqrt(n)) #unklar, wie es richtig ist
margin_of_error_t=crit_value_t*(std_dev/np.sqrt(n))

#thus we can calulate lower and upper boundary as follows:
low_bound_std=mean-crit_value_std*(std_dev/np.sqrt(n))
upper_bound_std=mean+crit_value_std*(std_dev/np.sqrt(n))

low_bound_t=mean-crit_value_t*(std_dev/np.sqrt(n))
upper_bound_t=mean+crit_value_t*(std_dev/np.sqrt(n))


#plotting

plt.figure(figsize=(10, 6))
plt.hist(data, bins=40)

plt.axvline(mean, color='orange', linestyle='--', label=f'Mean ≈ {mean:.2f}')
plt.axvline(low_bound_std, color='red', linestyle='--', label=f'Lower bound using normal distribution ≈ {low_bound_std:.2f}')
plt.axvline(upper_bound_std, color='red', linestyle='--', label=f'Upper bound using normal distribution ≈ {upper_bound_std:.2f}')
plt.axvline(low_bound_t, color='green', linestyle='--', label=f'Lower bound using t-Distribution ≈ {low_bound_t:.2f}')
plt.axvline(upper_bound_t, color='green', linestyle='--', label=f'Upper bound using t-Distribution ≈ {upper_bound_t:.2f}')

plt.title("Average startup delay of video streaming, Samples")
plt.xlabel("Observed delay (in seconds)")
plt.ylabel("Frequency")
plt.xticks(data)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()