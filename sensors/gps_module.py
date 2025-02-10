import time
import board
import busio
import adafruit_gps

# Initialize UART for GPS
uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)

# Turn on the basic GGA and RMC info
gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')

# Set update rate to 1 Hz
gps.send_command(b'PMTK220,1000')

# Main loop for GPS data reading
while True:
    gps.update()
    if gps.has_fix:
        print(f"Latitude: {gps.latitude}, Longitude: {gps.longitude}")
    time.sleep(1)