import time
from io import IO
from pointer import Pointer
from config import Config


def process():
    io = IO()
    pointer = Pointer()

    while True:
        if not io.check_button():
            io.switch_led()
            pointer.switch_state()
            time.sleep(Config.MAIN_LOOP_TRIGGER_WAIT)

        pointer.move()
        time.sleep(0.5)


def main():
    process()


if __name__ == '__main__':
    main()
