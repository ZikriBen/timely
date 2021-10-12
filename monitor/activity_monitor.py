import time
from pynput import mouse
from pynput import keyboard
from threading import Thread


class ActivityMonitor():
    def __init__(self, min_stop=2, total=15) -> None:
        self.total = total
        self.min_stop = min_stop
        self.mouse_c = mouse.Controller()
        self.keyboard_c = keyboard.Controller()

        self.timeout = time.time() + self.total
        self.stops = []
        self.start_time = time.time()
        self.running = False
        self.activity = False

        self.k_listener = None
        self.m_listener = None
        
        
    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(key.char))
            self.activity = True
            return self.running
        except AttributeError:
            self.activity = True
            print('special key {0} pressed'.format(key))

            return self.running

    def on_release(self, key):
        print('{0} released'.format(key))
        return self.running
                  

    def on_move(self, x, y):
        print('Pointer moved to {0}'.format((x, y)))
        self.activity = True
        return self.running


    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        self.activity = True
        return self.running


    def on_scroll(self, x, y, dx, dy):
        print('Scrolled {0}'.format((x, y)))
        self.activity = True
        return self.running

    @staticmethod        
    def percentage(part, whole):
        percentage = 100 * float(part) / float(whole)
        return str(int(percentage)) + "%"

    def thread_monitoring(self):
        while self.running:
            if self.activity:
                current_time = time.time()
                delta = current_time - self.start_time
                if delta > self.min_stop:
                    self.stops.append((delta, self.start_time, current_time))

                self.start_time = time.time()

            self.activity = False
            time.sleep(0.5)

            if time.time() > self.timeout:
                self.running = False
                break

        current_time = time.time()
        delta = current_time - self.start_time
        if delta > self.min_stop:
            self.stops.append((delta, self.start_time, current_time))

    def start_monitor(self):
        self.running = True
        self.stops = []
        self.start_time = time.time()
        self.activity = False

        self.k_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release).start()
        self.m_listener = mouse.Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll).start()
        
        Thread(target=self.thread_monitoring, args=()).start()
    
    def stop_monitor(self):
        self.running = False

    def get_active_time(self):
        return self.total - sum([delta[0] for delta in self.stops])

    def get_percentage_str(self):
        return f"From {str(self.total)}, you have worked: {str(round(self.get_active_time(), 2))}  which is {self.percentage(self.get_active_time(), self.total)}"


if __name__ == "__main__":
    active_monitor = ActivityMonitor()
    active_monitor.start_monitor()
    time.sleep(3)
    active_monitor.stop_monitor()