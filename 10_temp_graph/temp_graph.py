import random
from pathlib import Path
import matplotlib.pyplot as plt

OUTPUT = Path.home() / "temperature_graph.png"

# Test data first. Later this can be replaced with real sensor values.
temperatures = [random.randint(20, 30) for _ in range(12)]
minutes = list(range(len(temperatures)))

plt.plot(minutes, temperatures, marker="o")
plt.title("Temperature test graph")
plt.xlabel("Sample")
plt.ylabel("Temperature °C")
plt.grid(True)
plt.savefig(OUTPUT)
print(f"Graph saved to {OUTPUT}")
plt.show()
