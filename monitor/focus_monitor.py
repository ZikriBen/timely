from threading import Thread
import time
from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer, byref
import psutil
from imonitor import IMonitor

# apps = {
#     "chrome.exe": {
#         "total_usage": 0,
#         "titles": {
#             "Google Search": {
#                 "usage": 0,
#                 "start_time": "",
#                 "end_time": ""
#             }
#         }
#     }
# }


class FocusMonitor(IMonitor):

    def __init__(self, total: int) -> None:
        self.__running = False
        self.__total = total
        
        self.timeout = None
        self.apps = {}
        self.thread = None


    def running(self):
        return self.__running
    
    def total(self):
        return self.__total

    def getForegroundWindowTitle(self) -> Optional[str]:
        hWnd = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(hWnd)
        buf = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(hWnd, buf, length + 1)

        return buf.value if buf.value else None


    def getProcessName(self) -> Optional[str]:
        # time.sleep(3)
        hWnd = windll.user32.GetForegroundWindow()
        pid = wintypes.DWORD()
        windll.user32.GetWindowThreadProcessId(hWnd, byref(pid))
        process = psutil.Process(pid.value)
        
        return process.name()


    def add_to_apps(self, app: str, title: str, focus_time: int, start: int, stop: float) -> None:
        # print(" ## " + app + " ## " + title + " ## " + str(focus_time) + " ## " + str(start) + " ## " + str(stop))
        if app not in self.apps:
            self.apps[app] = {
                "total_usage": 0,
                "start_time": start,
                "end_time": stop,
                "titles": {
                    title: {
                        "usage": focus_time,
                    }
                }
            }
        else:
            if start == self.apps[app]['end_time']:
                self.apps[app]['end_time'] = stop
            if title not in self.apps[app]['titles']:
                self.apps[app]['titles'][title] = {
                    "usage": focus_time,
                }

            else:
                self.apps[app]['titles'][title]['usage'] += focus_time

    def start_monitor(self) -> dict:
        self.reset_monitor()
        self.thread = Thread(target=self.monitoring_loop, args=())
        self.thread.start()
        self.__running = True
        

    def stop_monitor(self) -> dict:
        self.__running = False
        self.thread.join()
        self.calculate()
        return self.apps

    def reset_monitor(self):
        self.timeout = time.time() + self.__total
        self.__running = False
        self.thread = None
        

    def calculate(self) -> dict:
        for app in self.apps.keys():
            total_app = 0
            for title in self.apps[app]['titles'].keys():
                total_app += self.apps[app]['titles'][title]['usage']
            self.apps[app]['total_usage'] = total_app
        


    def monitoring_loop(self) -> None:
        start_time = int(time.time())
        before_title, before_proc = self.getForegroundWindowTitle(), self.getProcessName()

        while self.__running:
            current_title, current_proc = self.getForegroundWindowTitle(), self.getProcessName()

            if current_title != before_title:
                now = int(time.time())
                delta = now - start_time

                self.add_to_apps(before_proc, before_title, delta, start_time, now)
                start_time = now

            before_title = current_title
            before_proc = current_proc
            time.sleep(1)
            
            if time.time() > self.timeout:
                break

        now = int(time.time())
        self.add_to_apps(current_proc, current_title, now - start_time, start_time, now)

if __name__ == "__main__":
    fm = FocusMonitor(total=10)
    fm.start_monitor()
    time.sleep(5)
    fm.stop_monitor()
    print(fm.apps)