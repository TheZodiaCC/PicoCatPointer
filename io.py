from config import Config
from machine import Pin


class IO:
    def __init__(self):
        self.red_led = Pin(Config.RED_LED_PIN, Config.LED_PIN_TYPE)
        self.green_led = Pin(Config.GREEN_LED_PIN, Config.LED_PIN_TYPE)
        self.button = Pin(Config.BUTTON_PIN, Config.BUTTON_PIN_IN_TYPE, Config.BUTTON_PIN_UP_TYPE)
        self.init()

    def init(self):
        self.red_led.value(1)
        self.green_led.value(0)

    def check_button(self):
        return self.button.value()

    def switch_led(self):
        self.red_led.value(not self.red_led.value())
        self.green_led.value(not self.green_led.value())
