from rplidar import RPLidar

PORT_NAME = '/dev/ttyUSB0'

lidar = RPLidar(PORT_NAME)

try:
    print("Starting LiDAR scan...")

    for scan in lidar.iter_scans():
        print(f"Detected {len(scan)} measurement points")

        # Display a few measurements
        for measurement in scan[:5]:
            quality, angle, distance = measurement

            if distance > 0:
                print(
                    f"Angle: {angle:.1f}°, "
                    f"Distance: {distance / 1000:.2f} m"
                )

        print("-" * 30)

except KeyboardInterrupt:
    print("LiDAR test stopped.")

finally:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()