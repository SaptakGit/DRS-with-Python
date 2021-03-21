import tkinter
import cv2 # pip install opencv-python
import PIL.Image, PIL.ImageTk # pip install pillow
from functools import partial

def play(speed):
    print(speed)

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
btn = tkinter.Button(window, text="<< Previous (Fast)", width=50)
btn.pack()
btn = tkinter.Button(window, text="<< Previous (Slow)", width=50)
btn.pack()
btn = tkinter.Button(window, text="Next (Fast) >>", width=50, command=partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text="Next (Slow) >>", width=50)
btn.pack()
btn = tkinter.Button(window, text=" Give Out", width=50)
btn.pack()
btn = tkinter.Button(window, text=" Give Not Out", width=50)
btn.pack()

window.mainloop()