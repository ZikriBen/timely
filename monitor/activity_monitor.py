import sys
import time
import json
from pathlib import Path
from pynput import mouse, keyboard
from datetime import datetime
from threading import Thread

sys.path.append(r'.\monitor')
from imonitor import IMonitor

class ActivityMonitor(IMonitor):
    def __init__(self, min_stop:int, total:int) -> None:
        self.__running = False
        self.__total = total
        
        self.min_stop = min_stop
        self.mouse_c = mouse.Controller()
        self.keyboard_c = keyboard.Controller()
        
        self.timeout = None
        self.stops = []
        self.data = {}
        self.activity = False

        self.k_listener = None
        self.m_listener = None
        self.thread = None
        self.start_total_time = int(time.time())
        
    
    def running(self):
        return self.__running
    
    def total(self):
        return self.__total

    def on_press(self, key: keyboard.Key) -> bool:
        try:
            print('alphanumeric key {0} pressed'.format(key.char))
            self.activity = True
            return self.__running
        except AttributeError:
            self.activity = True
            print('special key {0} pressed'.format(key))

            return self.__running

    def on_release(self, key: keyboard.Key) -> bool:
        print('{0} released'.format(key))
        return self.__running
                  

    def on_move(self, x: int, y: int) -> bool:
        print('Pointer moved to {0}'.format((x, y)))
        self.activity = True
        return self.__running


    def on_click(self, x: int, y: int, button: mouse.Button, pressed: bool) -> bool:
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        self.activity = True
        return self.__running


    def on_scroll(self, x: int, y: int, dx: int, dy: int) -> bool:
        print('Scrolled {0}'.format((x, y)))
        self.activity = True
        return self.__running

    @staticmethod        
    def percentage(part: int, whole: int) -> bool:
        percentage = 100 * float(part) / float(whole)
        return int(percentage)

    def monitoring_loop(self, log_file: Path) -> None:
        start_time = time.time()

        while self.__running:
            if self.activity:
                current_time = time.time()
                delta = current_time - start_time
                if delta > self.min_stop:
                    self.stops.append((int(delta), int(start_time), int(current_time)))

                start_time = time.time()

            self.activity = False
            time.sleep(0.5)

            if time.time() > self.timeout:
                self.__running = False
                break

        current_time = time.time()
        delta = current_time - start_time
        if delta > self.min_stop:
            self.stops.append((int(delta), int(start_time), int(current_time)))
        
        with open(log_file, 'w') as f:
            json.dump(self.stops, f)
        

    def start_monitor(self) -> None:
        self.reset_monitor()
        log_dir = Path(r"./logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = Path(fr"./logs/activity_log{datetime.now().strftime('%d-%m-%Y_%I-%M-%S%p')}.json")

        self.k_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release).start()
        self.m_listener = mouse.Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll).start()
        
        self.thread = Thread(target=self.monitoring_loop, args=(log_file,))
        self.thread.start()

    
    def stop_monitor(self) -> None:
        self.__running = False
        self.thread.join()
        self.calculate()
        return self.data
        # Returning False from any callback to stop the listener as stated in https://pynput.readthedocs.io/en/latest/mouse.html

    def reset_monitor(self) -> None:
        self.stops = []
        self.timeout = time.time() + self.__total
        self.activity = False
        self.__running = True
        self.start_total_time = int(time.time())

    def get_active_time(self, total: int) -> int:
        if self.__running:
            return 0
        return total - sum([delta[0] for delta in self.stops])

    def get_percentage_str(self) -> str:
        if self.__running:
            return "Still Running!"
        return f"From {str(self.__total)}, you have worked: {str(round(self.get_active_time(), 2))}  which is {self.percentage(self.get_active_time(), self.__total)}"

    def calculate(self) -> dict:
        if self.__running:
            return 0
            
        end_time = int(time.time())
        total_time = int(time.time() - self.start_total_time)
        active_time = int(self.get_active_time(total_time))

        self.data =  {
            'min_stop': self.min_stop,
            'timeout': self.__total,
            'stops' : self.stops,
            'start_total_time': self.start_total_time,
            'end_total_time': end_time,
            'total_time': total_time,
            'active_time': active_time,
            'non_active_time': total_time - active_time,
            'percentage': self.percentage(active_time, total_time)
        }
        


if __name__ == "__main__":
    active_monitor = ActivityMonitor(min_stop=2, total=15)
    active_monitor.start_monitor()
