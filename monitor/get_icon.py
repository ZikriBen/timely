

import psutil
from ctypes import wintypes, windll, create_unicode_buffer, byref



def getProcessName():
    # time.sleep(3)
    hWnd = windll.user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    windll.user32.GetWindowThreadProcessId(hWnd, byref(pid))
    process = psutil.Process(pid.value)
    
    return process

print(getProcessName().exe())