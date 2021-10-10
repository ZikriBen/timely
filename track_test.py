import time
from pynput import mouse
from pynput import keyboard

total = 15
mouse_c = mouse.Controller()
before = mouse_c.position
timeout = time.time() + total
stops = []
start_time = time.time()
running = True
activity = False
keyboard_c = keyboard.Controller()


def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return str(int(percentage)) + "%"


def on_press(key):
    global activity
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        activity = True
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    global running
    print('{0} released'.format(
        key))
    if key == keyboard.Key.f10:
        # Stop listener
        running = False
        return False


def on_move(x, y):
    global activity
    print('Pointer moved to {0}'.format((x, y)))
    activity = True


def on_click(x, y, button, pressed):
    global activity
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    activity = True


def on_scroll(x, y, dx, dy):
    global activity
    print('Scrolled {0}'.format((x, y)))
    activity = True


k_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
k_listener.start()

m_listener = mouse.Listener(on_click=on_click, on_move=on_move, on_scroll=on_scroll)
m_listener.start()

while True and running:
    current = mouse_c.position
    if activity:
        current_time = time.time()
        delta = current_time - start_time
        if delta > 2:
            stops.append((delta, start_time, current_time))

        start_time = time.time()

    activity = False
    before = current
    time.sleep(0.5)

    if time.time() > timeout:
        keyboard_c.press(keyboard.Key.esc)
        keyboard_c.release(keyboard.Key.esc)
        break

current_time = time.time()
delta = current_time - start_time
if delta > 2:
    stops.append((delta, start_time, current_time))

print(stops)
active_time = total - sum([delta[0] for delta in stops])
print(f"From {str(total)}, you have worked: {str(round(active_time, 2))}  which is {percentage(active_time, total)}")