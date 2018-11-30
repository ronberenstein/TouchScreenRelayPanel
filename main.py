from guizero import App, PushButton, Slider, Text
from PIL import Image
import rpi_backlight as bl

#path = '/home/ron/TouchScreenRelayPanel/'
path = '/home/pi/TouchScreenRelayPanel/'
rear_light_state = 0
front_light_state = 0
water_pump_state = 0
winch_state = 0

def rear_light_callback():
    global rear_light_state, rear_light_button
    if rear_light_state == 0:
        rear_light_state = 1
        rear_light_button.image = path + 'rear_lights_on.png'
    else:
        rear_light_state = 0
        rear_light_button.image = path + 'rear_lights_off.png'

def front_light_callback():
    global front_light_state, front_light_button
    if front_light_state == 0:
        front_light_state = 1
        front_light_button.image = path + 'front_lights_on.png'
    else:
        front_light_state = 0
        front_light_button.image = path + 'front_lights_off.png'

def water_pump_callback():
    global water_pump_state, water_pump_button
    if water_pump_state == 0:
        water_pump_state = 1
        water_pump_button.image = path + 'water_pump_on.png'
    else:
        water_pump_state = 0
        water_pump_button.image = path + 'water_pump_off.png'

def winch_callback():
    global winch_state, winch_button
    if winch_state == 0:
        winch_state = 1
        winch_button.image = path + 'winch_on.png'
    else:
        winch_state = 0
        winch_button.image = path + 'winch_off.png'

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
slider = Slider(app, command=screen_brightness, grid=[0,2,3,2], align='left', start=30, end=255)
slider.value='255'
slider.resize(320, 40)
slider.text_color='white'
slider.bg='black'

def main():
    app.tk.attributes("-fullscreen",True)
    app.tk.config(cursor='none')
    app.display()

if __name__ == '__main__':
    main()
