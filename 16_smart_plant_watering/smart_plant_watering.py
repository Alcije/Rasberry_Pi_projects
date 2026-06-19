import time
import RPi.GPIO as GPIO

SOIL_SENSOR = 21
PUMP_RELAY = 20
WATERING_TIME = 4
CHECK_DELAY = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_SENSOR, GPIO.IN)
GPIO.setup(PUMP_RELAY, GPIO.OUT)
GPIO.output(PUMP_RELAY, GPIO.LOW)

try:
    print("Plant watering system started.")
    while True:
        soil_is_dry = GPIO.input(SOIL_SENSOR) == GPIO.HIGH

        if soil_is_dry:
            print("Soil is dry. Pump on.")
            GPIO.output(PUMP_RELAY, GPIO.HIGH)
            time.sleep(WATERING_TIME)
            GPIO.output(PUMP_RELAY, GPIO.LOW)
            print("Watering done.")
        else:
            print("Soil is still wet.")

        time.sleep(CHECK_DELAY)

except KeyboardInterrupt:
    print("\nWatering system stopped.")

finally:
    GPIO.output(PUMP_RELAY, GPIO.LOW)
    GPIO.cleanup()
