makey_bot = {
    'wave_pattern': [30, 0.5, 60, 0.5, 30, 0.5],
    'eyes_rgb_status': 1,
    'rgb_eye_color_1': '#FF0000',
    'rgb_eye_color_2': '#0000FF',
    '7seg_value': 5,
    'led_1_status': 1,
    'led_1_blink': 0.3,
    'led_2_status': 0,
    'led_2_blink': 0.5,
    'led_3_status': 1,
    'led_3_blink': 1.0
}

print("makey_bot Dictionary:")
for key, value in makey_bot.items():
    print(key,":", value)

key = input("Enter a key to look up: ")

if key in makey_bot:
    print("The value for", key, "is:",  {makey_bot[key]})
else:
    print("That key is not in the dictionary.")

