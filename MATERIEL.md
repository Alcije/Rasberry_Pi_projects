# Material list

This file gives a general idea of the material used in the projects.

## Basic material

- Raspberry Pi with Raspberry Pi OS
- MicroSD card
- Power supply
- Breadboard
- Jumper wires
- LEDs
- 220 ohm resistors
- Push buttons

## Sensors

- PIR motion sensor
- HC-SR04 ultrasonic sensor
- Soil moisture sensor
- Temperature sensor if you want to replace fake test values
- Optional DHT11 or DHT22 sensor for weather projects

## Camera projects

- Raspberry Pi camera module, or
- USB webcam

Some camera code uses OpenCV. Install it with:

```bash
pip3 install opencv-python
```

On some Raspberry Pi setups, the package may be easier to install with:

```bash
sudo apt install python3-opencv
```

## Web projects

Install Flask:

```bash
pip3 install flask
```

## Robotics projects

- 2 DC motors
- Motor driver module, for example L298N or TB6612FNG
- Wheels
- Robot chassis
- Battery pack
- Ultrasonic sensor
- Optional camera for the video rover

## Automation projects

- Relay module
- Small pump for plant watering
- RFID RC522 module
- LCD screen if you want a real display

## Safety notes

GPIO pins are fragile. Do not connect motors, pumps or heavy loads directly to them.

Use resistors with LEDs. Check voltage levels before connecting modules. If a sensor uses 5V output, use a voltage divider or a proper level shifter when needed.
