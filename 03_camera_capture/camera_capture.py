from pathlib import Path
from time import sleep

try:
    from picamera import PiCamera
except ImportError:
    PiCamera = None

SAVE_PATH = Path.home() / "pi_photo.jpg"


if PiCamera is None:
    print("picamera is not installed. This script is for older Raspberry Pi camera setups.")
else:
    camera = PiCamera()

    try:
        print("Camera preview starting...")
        camera.start_preview()
        sleep(3)
        camera.capture(str(SAVE_PATH))
        print(f"Photo saved here: {SAVE_PATH}")
    finally:
        camera.stop_preview()
        camera.close()
