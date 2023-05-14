import numpy as np
import matplotlib.pyplot as plt

# Define the signal as a list of voltage values over time
time = np.arange(0, 10, 0.1)
signal = np.sin(time)

# Plot the signal
plt.plot(time, signal)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()
