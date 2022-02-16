import threading
import time
import tkinter
from functools import partial

import PIL.Image  # pip install pillow
import PIL.ImageTk
import cv2  # pip install opencv-python
import imutils

stream = cv2.VideoCapture("clip.mp4")
flag = True


def play(speed):
    # print(speed)
    global flag
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(140, 26, fill="blue", font="Times 26 bold", text="... Decision Pending ...")
    flag = not flag


def pending(decision):
    # Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # Wait for 1 second
    time.sleep(1)
    # Display sponsor img
    frame = cv2.cvtColor(cv2.imread("sponsor.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # Wait for 1.5 sec
    time.sleep(1.5)
    # Display Out/ Not Out img
    if decision == 'Out':
        decision_img = 'out.jpg'
    else:
        decision_img = 'notout.jpg'
    frame = cv2.cvtColor(cv2.imread(decision_img), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("Out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("Not Out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


def quit_drs():
    exit()


# width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368

# tkinter GUI starts here
window = tkinter.Tk()
window.title("Third Umpire DRS kit")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control Playback
btn = tkinter.Button(window, text="<< Previous (Fast)", width=50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<< Previous (Slow)", width=50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text="Next (Fast) >>", width=50, command=partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text="Next (Slow) >>", width=50, command=partial(play, 2))
btn.pack()
btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()
btn = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()
btn = tkinter.Button(window, text="Quit", width=50, command=quit_drs)
btn.pack()

window.mainloop()
