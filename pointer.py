from machine import Pin, PWM
from config import Config
import random
import time


class Pointer:
    def __init__(self):
        self.horizontal_servo = PWM(Pin(Config.HORIZONTAL_SERVO_PIN))
        self.vertical_servo = PWM(Pin(Config.VERTICAL_SERVO_PIN))
        self.pointer = Pin(Config.POINTER_PIN, Config.LED_PIN_TYPE)
        self.running = False

        self.init_servos()
        self.down_servos()

    def init_servos(self):
        self.horizontal_servo.freq(50)
        self.vertical_servo.freq(50)

    def down_servos(self):
        self.vertical_servo.duty_u16(0)
        self.horizontal_servo.duty_u16(0)

    def switch_state(self):
        if self.running:
            self.pointer.value(0)
        else:
            self.pointer.value(1)
            self.down_servos()

        self.running = not self.running

    def get_direction_pwm(self, direction):
        if direction == Config.DIRECTION_FORWARD:
            pwm = random.randint(Config.FORWARD_SERVO_PWM_MIN, Config.FORWARD_SERVO_PWM_MAX)
        else:
            pwm = random.randint(Config.BACKWARD_SERVO_PWM_MIN, Config.BACKWARD_SERVO_PWM_MAX)

        return pwm

    def move(self):
        if self.running:
            horizontal_pwm = self.get_direction_pwm(random.uniform(Config.DIRECTION_FORWARD, Config.DIRECTION_BACKWARD))
            vertical_pwm = self.get_direction_pwm(random.uniform(Config.DIRECTION_FORWARD, Config.DIRECTION_BACKWARD))

            wait = random.uniform(Config.SERVO_MIN_WAIT, Config.SERVO_MAX_WAIT)

            self.horizontal_servo.duty_u16(horizontal_pwm)
            self.vertical_servo.duty_u16(vertical_pwm)

            time.sleep(wait)

            self.down_servos()
