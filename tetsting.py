from typing import Optional

from ctypes import wintypes, windll, create_unicode_buffer, c_ulong, pointer
import psutil
import time



def getProcessName() -> Optional[str]:
    # time.sleep(3)
    hWnd = windll.user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    windll.user32.GetWindowThreadProcessId(hWnd, pointer(pid))
    process = psutil.Process(pid.value)

    print(process.name())
