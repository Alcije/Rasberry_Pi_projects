# Rasberry_Pi_projects

This repository is a collection of Raspberry Pi projects made to practice Python, GPIO, sensors, cameras, small web servers, automation and robotics.

The projects start with very simple exercises, then move step by step toward more complete ideas like dashboards, robot control, camera monitoring and autonomous rover experiments.

## Projects included

### Beginner projects

- LED controlled with a button
- CPU temperature reader
- Camera photo capture
- Basic Flask web server
- GPIO light sequence
- Simple temperature graph

### Intermediate projects

- Camera motion monitor
- LED control from a web page
- Small home assistant dashboard
- PIR motion notifier
- RGB button light
- Flask sensor dashboard
- LCD-style system monitor

### Robotics and automation projects

- Web controlled robot
- Obstacle avoidance robot
- Video rover with camera streaming
- Smart plant watering system
- RFID door lock
- Basic local assistant
- Rover data logger

## Goal

The goal is not to make everything perfect at once. The idea is to learn by testing real things:

- reading sensors;
- controlling LEDs, motors and relays;
- using GPIO pins safely;
- creating small Flask interfaces;
- using a camera with Python;
- building simple robotics projects;
- saving data into files for later analysis.

## Hardware

Depending on the project, you may need:

- Raspberry Pi
- Breadboard
- Jumper wires
- LEDs and resistors
- Push buttons
- PIR sensor
- Ultrasonic sensor HC-SR04
- Camera module or USB webcam
- Motor driver module
- DC motors
- Servo motor
- Relay module
- Soil moisture sensor
- RFID module RC522
- LCD screen
- External battery pack

More details are available in `MATERIEL.md`.

## How to run a project

Go inside the project folder, then run the Python file:

```bash
python3 file_name.py
```

For Flask projects, install Flask if needed:

```bash
pip3 install flask
```

Then open the Raspberry Pi address in a browser:

```text
http://raspberrypi.local:5000
```

or use the Pi IP address:

```text
http://YOUR_PI_IP:5000
```

## Important notes

Some projects need real components connected to the Raspberry Pi. Always check the wiring before powering the circuit.

For motors, pumps and relays, do not power everything directly from the Raspberry Pi GPIO pins. Use a proper driver, relay module or external power supply.

These projects are made for learning and can be improved in many ways.


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


(This repository reflects my own learning journey. AI was used as writing assistant to help structure an improve the README.)
