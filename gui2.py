import tkinter
from tkinter import filedialog
#from tkinter import Image
from PIL import ImageTk, Image
#import PIL.Image
#import Image, ImageTk

import cv2
from conecction import *

def define_rect(image):
    """
    Define a rectangular window by click and drag your mouse.

    Parameters
    ----------
    image: Input image.
    """

    clone = image.copy()
    rect_pts = []  # Starting and ending points
    win_name = 'image'  # Window name

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


    def save(clone):
        clone = image.copy()

    def refresh(win_name, clone):
        # close the open windows
        cv2.destroyWindow(win_name)
        cv2.imshow(win_name, clone)

    #saveBtn = Button(root, text='Guardar', command=lambda: save(win_name,clone)).pack()
    #refreshBtn = Button(root, text='Borrar', command=lambda: refresh(win_name, clone)).pack()
    while True:
        cv2.imshow(win_name, clone)
        print('Opened image')

        key = cv2.waitKey(0) & 0xFF

        if key == ord("r"):  # Hit 'r' to replot the image
            clone = image.copy()

        elif key == ord("c"):  # Hit 'c' to confirm the selection
            break


    return rect_pts

def saveTag(tagStr, points,tagName, filename, imgID):
    tagText = tagStr.get()
    imgIDText = imgID.get()

    print("Label: ", tagText)
    print("ImgName: ", imgID)
    Label(root, text = '¡Guardado con éxito!').grid(row = 43, column=2)


    print("--- target window ---")
    print("Starting point is ", points[0])
    print("Ending   point is ", points[1])

    tagName.delete(0, 'end')
    imgID.delete(0, 'end')

    nameTxt = imgIDText+'.txt'
    f = open(nameTxt, 'w')
    f.write(tagText+' '+str(points[0])+' '+str(points[1]))
    f.close()

    # Sending to database
    insertBLOB(imgIDText,filename,nameTxt,tagText)

def tag(image, filename):
    # Points of the target window
    points = define_rect(image)

    imgIDname = ''

    #File name
    imgID= StringVar()
    saveLb= tkinter.Label(root, text= 'Guardar imagen como: ')
    saveLb.grid(pady=5, padx= 20, row=40,column=1, sticky=W+E)
    imgIDname = tkinter.Entry(root, textvariable= imgID, bd = 2)
    imgIDname.grid(pady=5, row=40,column=2,sticky= W+E)

    #Tag name
    tagStr = StringVar()                                     #saves the tag string
    tagLb= tkinter.Label(root, text='Etiqueta: ')
    tagLb.grid(pady=5, padx=20,row=41, column=1, sticky=W+E)

    tagName = tkinter.Entry(root, textvariable= tagStr, bd = 2)
    tagName.grid(pady=5, row=41, column=2, sticky= W+E)

    saveButton =Button(root, text = 'Guardar', command = lambda : saveTag(tagStr,points, tagName, filename, imgIDname))
    saveButton.grid(row = 42, column=2)

def open_img():
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
    btn2 = Button(root, text='Etiquetar', command=lambda: tag(imgCV, filename))
    btn2.grid(pady=20, row=20, column=1)

def search():

    frame2 = Tk()
    frame2.geometry("400x400+500+100")
    frame2.title('Búsqueda de imágenes')
    frame2.resizable(width=True, height=True)
    tagStrFind = StringVar()  # saves the tag string
    tagLbF = tkinter.Label(frame2, text=' Buscar etiqueta: ')
    tagLbF.grid(pady=5, padx=20, row=1, column=1, sticky=W)
    tagNameF = tkinter.Entry(frame2, textvariable=tagStrFind, bd=2)
    tagNameF.grid(pady=5, row=1, column=2, sticky=W + E)
    searchTagBtn = Button(frame2, text= 'Buscar', command = lambda :searchImg(tagNameF, frame2) ,width= 15)
    searchTagBtn.grid(pady=10, row=2, column=2, sticky= W+E)



#Root window
root = Tk()
root.geometry("1000x1000+180+100")
root.title("Editor")
root.resizable(width=True, height=True)

btn1 = Button(root, text='Abrir imagen', command= open_img, width=15)
btn1.grid(pady=10, row=5,column=1,sticky=W)
searchBtn = Button(root, text= 'Buscar imágenes', command= lambda: search(), width=15)
searchBtn.grid(pady=10, row=10, column=1, sticky=W)

root.mainloop()