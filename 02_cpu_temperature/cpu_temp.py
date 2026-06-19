from pathlib import Path

TEMP_FILE = Path("/sys/class/thermal/thermal_zone0/temp")


def read_cpu_temp():
    # Raspberry Pi gives the temperature in millidegrees.
    raw_value = TEMP_FILE.read_text().strip()
    return int(raw_value) / 1000


if __name__ == "__main__":
    try:
        temperature = read_cpu_temp()
        print(f"CPU temperature: {temperature:.1f} °C")
    except FileNotFoundError:
        print("Temperature file not found. Are you running this on a Raspberry Pi?")
