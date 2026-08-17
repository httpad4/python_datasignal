import numpy as np
import matplotlib.pyplot as plt

# Discrete time index
n = np.arange(-10, 11, 1)

# Unit impulse δ[n]
impulse = np.where(n == 0, 1, 0)

# Unit step u[n]
step = np.where(n >= 0, 1, 0)

# Ramp r[n]
ramp = np.where(n >= 0, n, 0)

# Exponential sequence (0.8^n)u[n]
expo = np.where(n >= 0, (0.8**n), 0)

# Sinusoidal cos(0.2πn)
sinusoid = np.cos(0.2 * np.pi * n)

# Plotting
signals = {
    "Unit Impulse δ[n]": impulse,
    "Unit Step u[n]": step,
    "Ramp r[n]": ramp,
    "Exponential (0.8^n)u[n]": expo,
    "Cosine cos(0.2πn)": sinusoid
}

for title, signal in signals.items():
    plt.figure()
    plt.stem(n, signal, basefmt=" ")
    plt.title(title)
    plt.xlabel("n (discrete time index)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
