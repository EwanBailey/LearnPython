from gpiozero import LED
import time
red_led = LED(3)
yellow_led = LED(4)
green_led = LED(18)

def stop_light(_stop_light):
    red,yellow,green = _stop_light
    while(True):
        green_led.on()
        time.sleep(5)
        yellow_led.on()
        green_led.off()
        time.sleep(2)
        red_led.on()
        yellow_led.off()
        time.sleep(5)
        red_led.off()
    
#     if(_stop_light[red]):
#         red_led.on()
#     else:
#         red_led.off()
#         
#     if(_stop_light[yellow]):
#         yellow_led.on()
#     else:
#         yellow_led.off()
#         
#     if(_stop_light[green]):
#         green_led.on()
#     else:
#         green_led.off()
    
    
def main():
    traffic_light = {'red_LED':1									, 'yellow_LED':1, 'green_LED':1}
    stop_light(traffic_light)
    
    
main()
