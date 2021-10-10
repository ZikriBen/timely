import time
from pynput.mouse import Controller


def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return str(int(percentage)) + "%"


mouse = Controller()

before = mouse.position

global_start_time = time.time()

start_time = time.time()
work_time = []

timeout = time.time() + 15   # 15 seconds from now

while True:
    current = mouse.position
    if before != current:
        print('Movement detected')
        current_time = time.time()
        delta = current_time - start_time

        if(delta > 2):
            work_time.append(delta)
        start_time = time.time()

    before = current
    time.sleep(0.5)

    if time.time() > timeout:
        break
print(work_time)
global_end_time = time.time() - global_start_time
global_work_time = global_end_time

for delta in work_time:
    global_work_time -= delta

print(f"From {str(round(global_end_time, 2))}, you have worked: {str(round(global_work_time, 2))}  which is {percentage(global_work_time, global_end_time)}")