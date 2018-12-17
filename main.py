from guizero import App, PushButton, Slider, Text
from PIL import Image
import rpi_backlight as bl
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# path = '/home/ron/TouchScreenRelayPanel/'
path = '/home/pi/TouchScreenRelayPanel/'
rear_light_state = 0
front_light_state = 0
water_pump_state = 0
winch_state = 0
air_state = 0

def rear_light_callback():
    global rear_light_state, rear_light_button
    if rear_light_state == 0:
        rear_light_state = 1
        rear_light_button.image = path + 'rear_lights_on.png'
        GPIO.setup(40, GPIO.OUT)
        GPIO.output(40, GPIO.LOW)

    else:
        rear_light_state = 0
        rear_light_button.image = path + 'rear_lights_off.png'
        GPIO.setup(40, GPIO.OUT)
        GPIO.output(40, GPIO.HIGH)

def front_light_callback():
    global front_light_state, front_light_button
    if front_light_state == 0:
        front_light_state = 1
        front_light_button.image = path + 'front_lights_on.png'
        GPIO.setup(38, GPIO.OUT)
        GPIO.output(38, GPIO.LOW)
    else:
        front_light_state = 0
        front_light_button.image = path + 'front_lights_off.png'
        GPIO.setup(38, GPIO.OUT)
        GPIO.output(38, GPIO.HIGH)


def water_pump_callback():
    global water_pump_state, water_pump_button
    if water_pump_state == 0:
        water_pump_state = 1
        water_pump_button.image = path + 'water_pump_on.png'
        GPIO.setup(36, GPIO.OUT)
        GPIO.output(36, GPIO.LOW)
    else:
        water_pump_state = 0
        water_pump_button.image = path + 'water_pump_off.png'
        GPIO.setup(36, GPIO.OUT)
        GPIO.output(36, GPIO.HIGH)


def winch_callback():
    global winch_state, winch_button
    if winch_state == 0:
        winch_state = 1
        winch_button.image = path + 'winch_on.png'
        GPIO.setup(37, GPIO.OUT)
        GPIO.output(37, GPIO.LOW)
    else:
        winch_state = 0
        winch_button.image = path + 'winch_off.png'
        GPIO.setup(37, GPIO.OUT)
        GPIO.output(37, GPIO.HIGH)

def air_callback():
    global air_state, air_button
    if air_state == 0:
        air_state = 1
        air_button.image = path + 'AirSystem_on.png'
        GPIO.setup(35, GPIO.OUT)
        GPIO.output(35, GPIO.LOW)
    else:
        air_state = 0
        air_button.image = path + 'AirSystem_off.png'
        GPIO.setup(35, GPIO.OUT)
        GPIO.output(35, GPIO.HIGH)


def screen_brightness():
    global slider
    print(slider.value)
    bl.set_brightness(str(slider.value))


app = App(title="Keypad example", width=480, height=320, layout="grid")
app.bg='black'
rear_light_button = PushButton(app, command=rear_light_callback, grid=[0,0], align='left', image = path + 'rear_lights_off.png')
front_light_button = PushButton(app, command=front_light_callback, grid=[1,0], align='left',image = path + 'front_lights_off.png')
water_pump_button  = PushButton(app, command=water_pump_callback, grid=[2,0], align='left',image = path + 'water_pump_off.png')
winch_button  = PushButton(app, command=winch_callback, grid=[0,1], align='left',image = path + 'winch_off.png')
air_button  = PushButton(app, command=air_callback, grid=[1,1], align='left',image = path + 'AirSystem_off.png')

# slider = Slider(app, command=screen_brightness, grid=[0,2,3,2], align='left', start=30, end=255)
# slider.value='255'
# slider.resize(320, 40)
# slider.text_color='white'
# slider.bg='black'

def main():
    app.tk.attributes("-fullscreen",True)
    app.tk.config(cursor='none')
    app.display()

if __name__ == '__main__':
    main()
