import numpy as np
import matplotlib.pyplot as plt

# Step 2: Time base
t = np.arange(0, 1, 0.001)

# Step 3: Generate basic analog signals
f1 = 5  # frequency in Hz
sine_wave = np.sin(2 * np.pi * f1 * t)

f2 = 10
cosine_wave = np.cos(2 * np.pi * f2 * t)

# Step 4: Plot the signals
plt.figure(figsize=(10, 6))

# Sine wave
plt.subplot(3, 1, 1)
plt.plot(t, sine_wave)
plt.title("Sine Wave (5 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Cosine wave
plt.subplot(3, 1, 2)
plt.plot(t, cosine_wave, 'r')
plt.title("Cosine Wave (10 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Combined signal
combined = sine_wave + cosine_wave
plt.subplot(3, 1, 3)
plt.plot(t, combined, 'g')
plt.title("Combined Signal: Sine + Cosine")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()