
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import cv2


'''
filename = filedialog.askopenfilename(title='open')   #Search for file
imgCV = cv2.imread(filename)
img = Image.open(filename)
'''
def open_img(root):
    filename = filedialog.askopenfilename(title='Abrir imagen')   #Search for file
    print(filename)
    imgCV = cv2.imread(filename)
    print('what')
    img = Image.open(filename)
    img = img.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img )
    panel.image = img                                    #Displays the image
    panel.grid(pady=10, padx= 50, row=20, column=2)
    return imgCV,filename

def hola():
    print('hola')