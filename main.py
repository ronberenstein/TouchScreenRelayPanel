from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton


def rear_light_callback(instance, value):
    print('rear light is ', value)

def front_light_callback(instance, value):
    print('front light is', value)

def winch_callback(instance, value):
    print('winch is ', value)

def slider_callback(instance, value):
    print('slider value is ', value)

def water_pump_callback(instance, value):
    print('water pump value is ', value)

class MyApp(App):

    def build(self):
        SV = 3  # Spacing Value
        Config.set('graphics', 'width', '480')
        Config.set('graphics', 'height', '320')
        Config.set('graphics', 'Color', '[200,200,0]')  # doesn't work...

        layout = BoxLayout(orientation='vertical')
        top_row = BoxLayout(orientation='horizontal')
        mid_row = BoxLayout(orientation='horizontal')
        bottom_row = BoxLayout(orientation='horizontal')
        layout.spacing = SV
        top_row.spacing = SV
        mid_row.spacing = SV
        bottom_row.spacing = SV

        rear_light = ToggleButton()
        rear_light.bind(state=rear_light_callback)
        rear_light.background_normal = 'rear_lights_off.png'
        rear_light.background_down = 'rear_lights_on.png'
        top_row.add_widget(rear_light)

        front_light = ToggleButton()
        front_light.bind(state = front_light_callback)
        front_light.background_normal = 'front_lights_off.png'
        front_light.background_down = 'front_lights_on.png'
        top_row.add_widget(front_light)

        winch = ToggleButton()
        winch.bind(state = winch_callback)
        winch.background_normal = 'winch_off.png'
        winch.background_down = 'winch_on.png'
        top_row.add_widget(winch)

        water_pump = ToggleButton()
        water_pump.bind(state=water_pump_callback)
        water_pump.background_normal = 'water_pump_off.png'
        water_pump.background_down = 'water_pump_on.png'
        mid_row.add_widget(water_pump)

        not_function = ToggleButton()
        not_function2 = ToggleButton()
        # water_pump.bind(state=water_pump_callback)
        # water_pump.background_normal = 'water_pump_off.png'
        # water_pump.background_down = 'water_pump_on.png'
        mid_row.add_widget(not_function)
        mid_row.add_widget(not_function2)

        screenIntensity = Slider(min=0, max=100, value=50, value_track=True, value_track_color=[0, 0, 1, 1])
        screenIntensity.bind(value = slider_callback)
        bottom_row.add_widget(screenIntensity)
        layout.add_widget(top_row)
        layout.add_widget(mid_row)
        layout.add_widget(bottom_row)

        return layout


if __name__ == '__main__':
    MyApp().run()
