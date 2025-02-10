import RPi.GPIO as GPIO
import time

# GPIO pins for ultrasonic sensor
TRIG = 23
ECHO = 24

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Send a pulse to the sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Measure the echo duration
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate distance in cm
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

# Main loop for obstacle detection
try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)  # Sleep for 1 second
except KeyboardInterrupt:
    GPIO.cleanup()