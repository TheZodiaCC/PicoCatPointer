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

    def move(self):
        if self.running:
            speed = random.randint(1, Config.SERVO_MAX_SPEED)
            direction = random.choice([-1, 1])
            distance = random.randint(10, Config.HORIZONTAL_SERVO_MAX)

            if direction > 0:
                for i in range(100, distance, speed):
                    self.horizontal_servo.duty_u16(i)
                    time.sleep(0.01)
            else:
                for i in range(distance, 0, -1 * speed):
                    self.horizontal_servo.duty_u16(i)
                    time.sleep(0.01)

            self.down_servos()
