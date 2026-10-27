from rplidar import RPLidar
from breezyslam.algorithms import RMHC_SLAM
from breezyslam.sensors import RPLidarA1

PORT_NAME = "/dev/ttyUSB0"

MAP_SIZE_PIXELS = 500
MAP_SIZE_METERS = 10

MAP_FILE = "slam_map.pgm"


def save_map(slam):
    # Retrieve the current map from BreezySLAM
    map_bytes = bytearray(
        MAP_SIZE_PIXELS * MAP_SIZE_PIXELS
    )
    slam.getmap(map_bytes)

    # Save as a grayscale PGM image
    with open(MAP_FILE, "wb") as file:
        file.write(
            f"P5\n{MAP_SIZE_PIXELS} "
            f"{MAP_SIZE_PIXELS}\n255\n".encode()
        )
        file.write(map_bytes)

    print(f"Map saved to {MAP_FILE}")


def main():
    lidar = None

    try:
        print("Connecting to RPLIDAR...")

        lidar = RPLidar(PORT_NAME)

        # Create the SLAM algorithm
        slam = RMHC_SLAM(
            RPLidarA1(),
            MAP_SIZE_PIXELS,
            MAP_SIZE_METERS
        )

        print("SLAM started.")
        print("Move the robot slowly to build a map.")
        print("Press Ctrl+C to stop and save the map.")

        scans = lidar.iter_scans()

        # Ignore the first scan, as in the official example
        next(scans)

        scan_count = 0

        for scan in scans:
            # Keep valid distances and their matching angles
            measurements = [
                (angle, distance)
                for quality, angle, distance in scan
                if distance > 0
            ]

            if len(measurements) < 5:
                continue

            angles = [
                measurement[0]
                for measurement in measurements
            ]

            distances = [
                measurement[1]
                for measurement in measurements
            ]

            # Update SLAM using the actual scan angles
            slam.update(
                distances,
                scan_angles_degrees=angles
            )

            scan_count += 1

            # Print progress occasionally, not every measurement
            if scan_count % 10 == 0:
                x, y, theta = slam.getpos()

                print(
                    f"Scans: {scan_count} | "
                    f"Position: x={x / 1000:.2f} m, "
                    f"y={y / 1000:.2f} m, "
                    f"heading={theta:.1f} degrees"
                )

                save_map(slam)

    except KeyboardInterrupt:
        print("\nStopping SLAM...")

    finally:
        if lidar is not None:
            try:
                lidar.stop()
                lidar.stop_motor()
            except Exception:
                pass

            try:
                lidar.disconnect()
            except Exception:
                pass

        if "slam" in locals():
            save_map(slam)

        print("SLAM program ended.")


if __name__ == "__main__":
    main()
