import time
from pathlib import Path

try:
    import psutil
except ImportError:
    psutil = None

# This project prints the values first.
# If an LCD library is installed, the print part can be replaced by lcd.write().
TEMP_FILE = Path("/sys/class/thermal/thermal_zone0/temp")


def cpu_temp():
    try:
        return int(TEMP_FILE.read_text().strip()) / 1000
    except FileNotFoundError:
        return 0


try:
    while True:
        temp = cpu_temp()
        if psutil:
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
        else:
            cpu = 0
            ram = 0

        print(f"CPU: {cpu:4.1f}% | RAM: {ram:4.1f}% | Temp: {temp:4.1f}°C")
        time.sleep(2)

except KeyboardInterrupt:
    print("\nSystem monitor stopped.")
