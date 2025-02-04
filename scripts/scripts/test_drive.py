from picarx import Picarx
import time

if __name__ == "__main__":
    try:
        px = Picarx()
        # Drive forward at speed 30
        px.forward(30)
        # Drive for 5 seconds
        time.sleep(5)
        # Stop the car
        px.forward(0)
    finally:
        # Ensure the car stops if an error occurs
        px.forward(0)
