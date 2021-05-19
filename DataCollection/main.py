
# To run this as part of a bigger program, use mutltiprocessing to create a seperate process
# for video recording using the following lines.
from multiprocessing import Process
import cv2
from timeloop import Timeloop
import time
import os
from time import sleep

# set recording duration
record_time = 20

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def make_1080p(cap):
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_4k(cap):
    cap.set(3, 3840)
    cap.set(4, 2160)

def make_720p(cap):
    cap.set(3, 1280)
    cap.set(4, 720)

def close_cam(cap):
    cap.release()

def capture_image():
    print('Opening camera')
    cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
    print('Camera ON')

    ret, frame = cap.read()  # return a single frame in variable `frame`
    print('Picture received')

    if not ret:
        print("failed to grab frame")

    name = "images/" + time.strftime("%Y%m%d-%H%M%S") + ".png"
    print(name)

    cv2.imwrite(name, frame)


if __name__ == '__main__':
    print_hi('PyCharm')

    times = 0
    delay = 1  # Define the interval for capturing images - in seconds
    print('Starting capture')
    cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
    fps = cap.get(cv2.CAP_PROP_FPS)  # getting the number of frame in 1 second of video
    timer_limit = fps * delay

    print('Init camera')
    make_720p(cap)  # Call the different resolution based on camera hardware

    print('Starting')

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # print('Timer expiry')
        #if button.is_pressed:
        times += 1
        if times > timer_limit:
            print("Detected")
            print('Opening camera')
            #cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
            print('Camera ON')

            ret, frame = cap.read()  # return a single frame in variable `frame`
            print('Picture received')

            if not ret:
                print("failed to grab frame")

            name = "images/" + time.strftime("%Y%m%d-%H%M%S") + ".png"
            # path_to = 'C:\\Users\\k64096478\\Work\\DataCollection'
            # save_directory = os.path.join(path_to, name)
            print(name)

            cv2.imwrite(name, frame)

            #capture_image()
            times = 0
        # sleep(0.1)

    close_cam(cap)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/







