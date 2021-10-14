from machine import Pin


class Config:
    POINTER_PIN = 17
    RED_LED_PIN = 27
    GREEN_LED_PIN = 28
    BUTTON_PIN = 18

    LED_PIN_TYPE = Pin.OUT
    BUTTON_PIN_IN_TYPE = Pin.IN
    BUTTON_PIN_UP_TYPE = Pin.PULL_UP

    HORIZONTAL_SERVO_PIN = 0
    VERTICAL_SERVO_PIN = 1
    HORIZONTAL_SERVO_MAX = 200
    VERTICAL_SERVO_MAX = 200
    SERVO_MAX_SPEED = 10

    MAIN_LOOP_TRIGGER_WAIT = 0.5
