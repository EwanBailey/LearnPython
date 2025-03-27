from gpiozero import RGBLED, LED, Servo
from time import sleep

rgb1 = RGBLED(red=17, green=18, blue=27)  # RGB LED 1 pins
rgb2 = RGBLED(red=22, green=23, blue=24)  # RGB LED 2 pins

red_led = LED(5)
green_led = LED(6)
yellow_led = LED(13)

servo = Servo(12)


def get_rgb(led_name):
    while True:
        try:
            r = float(input(f"Enter red value for {led_name} (0 to 1): "))
            g = float(input(f"Enter green value for {led_name} (0 to 1): "))
            b = float(input(f"Enter blue value for {led_name} (0 to 1): "))
            
            if 0 <= r <= 1 and 0 <= g <= 1 and 0 <= b <= 1:
                return (r, g, b)
            else:
                print("Please enter a number between 0 and 1:")
        except ValueError:
            print("Please enter a valid number:")

color1 = get_rgb("RGB LED 1")
rgb1.color = color1
sleep(1)

color2 = get_rgb("RGB LED 2")
rgb2.color = color2
sleep(1)

def rotate_servo(servo, min_degree, max_degree, steps=5):
    minvalue = min_degree / 90.0
    maxvalue = max_degree / 90.0
    
    for i in range(3):
        for pos in range(steps + 1):
            servo.value = minvalue + (pos / steps) * (maxvalue - minvalue)
            sleep(0.5)
        
        for pos in range(steps + 1):
            servo.value = maxvalue - (pos / steps) * (maxvalue - minvalue)
            sleep(0.5)

try:
    min_degree = int(input("Enter the minimum (0-180): "))
    max_degree = int(input("Enter the maximum (0-180): "))

    if 0 <= min_degree < max_degree <= 180:
        rotate_servo(servo, min_degree, max_degree)
    else:
        print("Make sure 0 ≤ min < max ≤ 180.")

except ValueError:
    print("There has been an error")

