import lgpio
from time import sleep

IN1, IN2, IN3, IN4 = 17, 27, 22, 23
CHIP = 15

h = lgpio.gpiochip_open(CHIP)
for pin in (IN1, IN2, IN3, IN4):
    lgpio.gpio_claim_output(h, pin)

def stop():
    for pin in (IN1, IN2, IN3, IN4):
        lgpio.gpio_write(h, pin, 0)

def forward():
    lgpio.gpio_write(h, IN1, 1)
    lgpio.gpio_write(h, IN2, 0)
    lgpio.gpio_write(h, IN3, 1)
    lgpio.gpio_write(h, IN4, 0)

def backward():
    lgpio.gpio_write(h, IN1, 0)
    lgpio.gpio_write(h, IN2, 1)
    lgpio.gpio_write(h, IN3, 0)
    lgpio.gpio_write(h, IN4, 1)

def turn_left():
    lgpio.gpio_write(h, IN1, 0)
    lgpio.gpio_write(h, IN2, 1)
    lgpio.gpio_write(h, IN3, 1)
    lgpio.gpio_write(h, IN4, 0)

def turn_right():
    lgpio.gpio_write(h, IN1, 1)
    lgpio.gpio_write(h, IN2, 0)
    lgpio.gpio_write(h, IN3, 0)
    lgpio.gpio_write(h, IN4, 1)

if __name__ == "__main__":
    try:
        forward(); sleep(2); stop(); sleep(1)
        backward(); sleep(2); stop(); sleep(1)
        turn_left(); sleep(2); stop(); sleep(1)
        turn_right(); sleep(2); stop()
    finally:
        stop()
        for pin in (IN1, IN2, IN3, IN4):
            lgpio.gpio_free(h, pin)
        lgpio.gpiochip_close(h)