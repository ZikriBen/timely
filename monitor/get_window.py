import time
from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer, byref
import PIL.ImageGrab
import psutil

total = 15
timeout = time.time() + total

apps = {
    # "chrome.exe": {
    #     "total_usage": 0,
    #     "titles": {
    #         "Google Search": {
    #             "usage": 0,
    #             "start_time": "",
    #             "end_time": ""
    #         }
    #     }
    # }
}


def getForegroundWindowTitle() -> Optional[str]:
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    return buf.value if buf.value else None


def getProcessName() -> Optional[str]:
    # time.sleep(3)
    hWnd = windll.user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    windll.user32.GetWindowThreadProcessId(hWnd, byref(pid))
    process = psutil.Process(pid.value)
    
    return process.name()


def add_to_apps(app: str, title: str, focus_time: int, start: int, stop: float):
    print(" ## " + app + " ## " + title + " ## " + str(focus_time) + " ## " + str(start) + " ## " + str(stop))
    if app not in apps:
        apps[app] = {
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
        if start == apps[app]['end_time']:
            apps[app]['end_time'] = stop
        if title not in apps[app]['titles']:
            apps[app]['titles'][title] = {
                "usage": focus_time,
            }

        else:
            apps[app]['titles'][title]['usage'] += focus_time

        # apps[app] = apps.get(app, 0) + focus_time


# im = PIL.ImageGrab.grab()
# im.save(output_file)

start_time = int(time.time())
before_title = getForegroundWindowTitle()
before_proc = getProcessName()

while True:
    current_title = getForegroundWindowTitle()
    current_proc = getProcessName()
    if current_title != before_title:
        now = int(time.time())
        delta = now - start_time

        add_to_apps(before_proc, before_title, delta, start_time, now)
        start_time = now

    before_title = current_title
    before_proc = current_proc
    time.sleep(1)
    
    if time.time() > timeout:
        break

now = int(time.time())
add_to_apps(current_proc, current_title, now - start_time, start_time, now)


for app in apps.keys():
    total_app = 0
    for title in apps[app]['titles'].keys():
        total_app += apps[app]['titles'][title]['usage']
    apps[app]['total_usage'] = total_app

print(apps)