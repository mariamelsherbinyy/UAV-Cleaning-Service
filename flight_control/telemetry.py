from pymavlink import mavutil

# Create a MAVLink connection
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

# Wait for the heartbeat message
master.wait_heartbeat()

# Main loop for telemetry communication
while True:
    # Receive messages from the drone
    msg = master.recv_match()
    if msg:
        print(f"Received message: {msg}")

    # Send commands to the drone (e.g., arm/disarm)
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)