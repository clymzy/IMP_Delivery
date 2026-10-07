# Motor Driver and Wheel Movement Test

## Objective

Test the Raspberry Pi's ability to control both DC motors through the L298N motor driver, including forward and backward movement.

## Reference Video

[**Watch: Raspberry Pi, L298N Motor Driver and DC Motor Connection Showcase on YouTube**](https://youtu.be/nwEZIJhWeDg)

## Hardware Connections

### L298N to Raspberry Pi GPIO

| L298N Pin | Raspberry Pi GPIO (BCM) |
| --------- | ----------------------- |
| IN1       | GPIO 17                 |
| IN2       | GPIO 27                 |
| IN3       | GPIO 22                 |
| IN4       | GPIO 23                 |
| GND       | Raspberry Pi GND        |

### Motors to L298N

| Motor       | L298N Output Pins |
| ----------- | ----------------- |
| Left motor  | OUT1 and OUT2     |
| Right motor | OUT3 and OUT4     |

## Testing Results

* Successfully established GPIO control of the L298N motor driver.
* Tested forward movement for 2 seconds.
* Tested backward movement for 2 seconds.
* Confirmed that both motors respond to the Raspberry Pi's GPIO outputs.

## Python Script

The motor control test is implemented in [`Motor_Testing.py`](Motor_Testing.py).

## Next Steps

* Integrate LiDAR distance measurements.
* Implement basic obstacle detection and avoidance.
* Integrate wheel encoders for wheel-speed and distance feedback.
* Develop autonomous navigation and SLAM capabilities.
