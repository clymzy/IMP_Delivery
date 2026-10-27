import lgpio
from time import sleep

# Raspberry Pi GPIO pins
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

# Pi 5 RP1 GPIO controller
CHIP = 15

h = lgpio.gpiochip_open(CHIP)

# Claim the pins as outputs
lgpio.gpio_claim_output(h, IN1)
lgpio.gpio_claim_output(h, IN2)
lgpio.gpio_claim_output(h, IN3)
lgpio.gpio_claim_output(h, IN4)


def stop():
    lgpio.gpio_write(h, IN1, 0)
    lgpio.gpio_write(h, IN2, 0)
    lgpio.gpio_write(h, IN3, 0)
    lgpio.gpio_write(h, IN4, 0)


def forward():
    # Left motor
    lgpio.gpio_write(h, IN1, 1)
    lgpio.gpio_write(h, IN2, 0)

    # Right motor
    lgpio.gpio_write(h, IN3, 1)
    lgpio.gpio_write(h, IN4, 0)


def backward():
    # Left motor
    lgpio.gpio_write(h, IN1, 0)
    lgpio.gpio_write(h, IN2, 1)

    # Right motor
    lgpio.gpio_write(h, IN3, 0)
    lgpio.gpio_write(h, IN4, 1)


try:
    print("FORWARD")
    forward()
    sleep(2)

    print("STOP")
    stop()
    sleep(1)

    print("BACKWARD")
    backward()
    sleep(2)

    print("STOP")
    stop()

finally:
    stop()

    lgpio.gpio_free(h, IN1)
    lgpio.gpio_free(h, IN2)
    lgpio.gpio_free(h, IN3)
    lgpio.gpio_free(h, IN4)

    lgpio.gpiochip_close(h)

print("Test finished.")