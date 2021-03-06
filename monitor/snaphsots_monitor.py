import cv2
import time
import pytesseract
from pytesseract import Output
import numpy as np
from threading import Thread
from PIL import ImageGrab
from pathlib import Path
from datetime import datetime

class SnapshotMonitor():

    def __init__(self, output_path, prefix="", interval=10, compression=9) -> None:
        
        self.outpur_path = output_path
        self.prefix = prefix
        self.compression = compression
        self.running = False
        self.interval = interval 
        tesseract_cmd_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
        pytesseract.pytesseract.tesseract_cmd = (tesseract_cmd_path)


    def take_screenshot(self) -> None:
        screen = np.array(ImageGrab.grab(bbox=None))
        cimg = cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
        
        scale_percent = 80
        width = int(cimg.shape[1] * scale_percent / 100)
        height = int(cimg.shape[0] * scale_percent / 100)
        dsize = (width, height)
        output = cv2.resize(cimg, dsize)

        cv2.imwrite(str(Path(self.outpur_path).joinpath(f'snap_{datetime.now().strftime("%d-%m-%Y_%I-%M-%S%p")}.jpg')), output, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
        cv2.imwrite(str(Path(self.outpur_path).joinpath(f'snap_{datetime.now().strftime("%d-%m-%Y_%I-%M-%S%p")}.png')), output, [cv2.IMWRITE_PNG_COMPRESSION, self.compression])


    def thread_monitoring(self):
        while self.running:
            self.take_screenshot()
            time.sleep(self.interval)


    def start_snapshot(self):
        self.running = True
        Thread(target=self.thread_monitoring, args=()).start()

    def stop_snapshot(self):
        self.running = False

    def get_string_from_image(self, image_path) -> str:
        img = cv2.imread(image_path)
        return pytesseract.image_to_string(img)

    def get_dict_from_image_path(self, image_path) -> dict:
        img = cv2.imread(image_path)
        return pytesseract.image_to_data(img, output_type=Output.DICT)

    def get_dict_from_image(self, image) -> dict:
        return pytesseract.image_to_data(image, output_type=Output.DICT)

    def search_in_word(self, words, target):
        n_boxes = len(words['text'])
        for i in range(n_boxes):
            if target in words['text'][i]:
                print(words['text'][i])

    def search_in_image(self, image_path, target):
        img = cv2.imread(image_path)
        words = self.get_dict_from_image(img)

        n_boxes = len(words['text'])
        padding = 3
        for i in range(n_boxes):
            if target in words['text'][i]:
                print(words['text'][i])
                (x, y, w, h) = (words['left'][i], words['top'][i], words['width'][i], words['height'][i])
                img = cv2.rectangle(img, (x - padding, y - padding), (x + w + padding, y + h + padding), (255, 0, 255), 1)

        cv2.imshow('img', img)
        cv2.waitKey(0)

if __name__ == "__main__":
    sm = SnapshotMonitor(output_path=r"C:\Personal\snapshots")
    sm.take_screenshot()
    # sm.search_in_image(r"C:\Personal\comp_image.png", "Original")
# # val = input("Enter your value: ")

# # if val in text_str:
# #     print("Found!")
# # else:
# #     print("Not found!")


# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# # print(d.keys())

# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if "config" in d['text'][i]:
#         print(d['text'][i])