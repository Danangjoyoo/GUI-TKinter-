from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import numpy
import cv2

root = Tk()
root.title('Face detector')
root.iconbitmap(r"c:\Users\Danangjoyoo\Pictures\cam.ico")

get_img = 0

def open_file():
    global get_img
    filename = filedialog.askopenfilename(initialdir=r"c:\Users\Danangjoyoo\Pictures",title="Deteksi mana nich?",filetypes=(('png','*.png'),('jpg','*.jpg'),('All files','*.*')))
    get_img = ImageTk.PhotoImage(Image.open(r'{}'.format(filename)))
    show = Label(root, image=get_img).grid(row=1,column=0)
    print(filename)
    open(filename)

def faces(directory):
    img = cv2.imread(r'{}'.format(directory))
    img = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    blur = cv2.medianBlur(gray,5)
    face_cascade = cv2.CascadeClassifier('face2.xml')
    faces = face_cascade.detectMultiScale(blur,1.3,5)
    try:
        for x,y,w,h in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(250,30,30),3)
    except:
        pass
    return img

def open(directory):
    img = faces(directory)
    cv2.imshow('wow',img)

but1 = Button(root,text='Open File',command=open_file).grid(row=0,column=0)
root.mainloop()