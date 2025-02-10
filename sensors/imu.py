import time
import board
import busio
import adafruit_bno055

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize IMU sensor
sensor = adafruit_bno055.BNO055_I2C(i2c)

# Main loop for IMU data reading
while True:
    # Read orientation data
    orientation = sensor.euler
    print(f"Orientation: {orientation}")

    # Read acceleration data
    acceleration = sensor.linear_acceleration
    print(f"Acceleration: {acceleration}")

    time.sleep(1)