from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ANJAY")
root.iconbitmap(r"c:\Users\Danangjoyoo\Pictures\cam.ico")

img = ImageTk.PhotoImage(Image.open(r"c:\Users\Danangjoyoo\Pictures\komeng.jpg"))
img1 = ImageTk.PhotoImage(Image.open(r"c:\Users\Danangjoyoo\Pictures\ravika.jpg"))
listimg = [img, img1]
idx_list = 0
botlabel = Label(text="Images {} of {}".format(idx_list+1,(len(listimg))),bd=2,anchor=E,relief=SUNKEN)
botlabel.grid(row=2,column=2)
label = Label(image=img)
label.grid(row=0,column=0,columnspan=3)

frame = LabelFrame(root,text='frame nich',padx=5,pady=5)
frame.grid(row=3,column=1)

def nextt():
    global idx_list
    global label
    label.grid_forget()
    idx_list += 1
    if idx_list <= (len(listimg)-1):
        idx_list = idx_list
    else:
        idx_list = 0
    print(idx_list)
    label = Label(image=listimg[idx_list])
    label.grid(row=0, column=0, columnspan=3)
    botlabel = Label(text="Images {} of {}".format(idx_list+1,(len(listimg))),bd=2,anchor=E,relief=SUNKEN)
    botlabel.grid(row=2,column=2)

def backk():
    global idx_list
    global label
    label.grid_forget()
    idx_list -= 1
    if idx_list < 0:
        idx_list = (len(listimg) - 1)
    else:
        idx_list = idx_list
    print(idx_list)
    label = Label(image=listimg[idx_list])
    label.grid(row=0, column=0, columnspan=3)
    botlabel = Label(text="Images {} of {}".format(idx_list+1, (len(listimg))),bd=2,anchor=E,relief=SUNKEN)
    botlabel.grid(row=2, column=2)

butQuit = Button(root, text="Exit Program", command=root.quit)
butnext = Button(root, text='>>',command=nextt)
butback = Button(root, text='<<',command=backk)

butQuit.grid(row=1, column=1)
butback.grid(row=1, column=0)
butnext.grid(row=1, column=2)

root.mainloop()