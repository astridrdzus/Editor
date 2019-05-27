from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import cv2


def define_rect(image):
    """
    Define a rectangular window by click and drag your mouse.

    Parameters
    ----------
    image: Input image.
    """

    clone = image.copy()
    rect_pts = []  # Starting and ending points
    win_name = "image"  # Window name

    def select_points(event, x, y, flags, param):

        nonlocal rect_pts
        if event == cv2.EVENT_LBUTTONDOWN:
            rect_pts = [(x, y)]

        if event == cv2.EVENT_LBUTTONUP:
            rect_pts.append((x, y))

            # draw a rectangle around the region of interest
            cv2.rectangle(clone, rect_pts[0], rect_pts[1], (0, 255, 0), 2)
            cv2.imshow(win_name, clone)

    cv2.namedWindow(win_name)
    cv2.setMouseCallback(win_name, select_points)

    while True:
        # display the image and wait for a keypress
        cv2.imshow(win_name, clone)
        key = cv2.waitKey(0) & 0xFF

        if key == ord("r"):  # Hit 'r' to replot the image
            clone = image.copy()

        elif key == ord("c"):  # Hit 'c' to confirm the selection
            break

    # close the open windows
    cv2.destroyWindow(win_name)

    return rect_pts

def tag(image):
    # Points of the target window
    points = define_rect(image)

    print("--- target window ---")
    print("Starting point is ", points[0])
    print("Ending   point is ", points[1])






def open_img():
    filename = filedialog.askopenfilename(title='open')
    imgCV = cv2.imread(filename)
    img = Image.open(filename)
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    btn2 = Button(root, text='Etiquetar', command=lambda: tag(imgCV)).pack()


root = Tk()
root.geometry("1200x1200+0+0")
root.title("Editor")
root.resizable(width=True, height=True)

btn1 = Button(root, text='Abrir imagen', command=open_img).pack()

root.mainloop()