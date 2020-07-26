from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.title('ANJAAY LEARNING')
root.iconbitmap(r"c:\Users\Danangjoyoo\Pictures\cam.ico")

r, img1, img2, img3, kotak1, ch1, ch2, ch3, ch4, but0, but1, head, random_num, answer = 0,0,0,0,0,0,0,0,0,0,0,0,0,0

def destroyQuest():
    global kotak1, ch1, ch2, ch3, ch4, but0, but1, but2, head, answer
    but0.grid_forget()
    try:
        kotak1.grid_forget()
        ch1.grid_forget()
        ch2.grid_forget()
        ch3.grid_forget()
        ch4.grid_forget()
        but1.grid_forget()
        but2.grid_forget()
    except:
        pass
    try:
        head.grid_forget()
    except:
        pass
    try:
        answer.grid_forget()
    except:
        pass

def submit():
    destroyQuest()
    global r, kotak1, but2, ans1,ans2,ans3,random_num, answer
    score_now = r.get()
    if score_now == 100:
        kotak1 = congrat_pic
        congrat_pic.grid(row=0,column=0)
        but2.grid(row=1,column=0,columnspan=2)
        if random_num == 0:
            answer = Label(root, image=ans1)
        elif random_num == 1:
            answer = Label(root, image=ans2)
        else:
            answer = Label(root, image=ans3)
        answer.grid(row=0,column=1)
    else :
        kotak1 = salah_pic
        salah_pic.grid(row=0, column=0)
        but2.grid(row=1, column=0, columnspan=2)
        if random_num == 0:
            answer = Label(root, image=ans1)
        elif random_num == 1:
            answer = Label(root, image=ans2)
        else:
            answer = Label(root, image=ans3)
        answer.grid(row=0,column=1)

def start():
    global r, img1, img2, img3, kotak1, ch1, ch2, ch3, ch4, but1, head, random_num
    destroyQuest()
    r = IntVar()
    img1 = ImageTk.PhotoImage(Image.open(r'C:\Users\Danangjoyoo\Pictures\meme\Hewan Head Wrong\burunga1.jpg'))
    img2 = ImageTk.PhotoImage(Image.open(r'C:\Users\Danangjoyoo\Pictures\meme\Hewan Head Wrong\pandanguin1.jpg'))
    img3 = ImageTk.PhotoImage(Image.open(r'C:\Users\Danangjoyoo\Pictures\meme\Hewan Head Wrong\gorijah1.jpg'))
    idx_img = [img1, img2, img3]
    random_num = random.randrange(3)
    chosen_pic = idx_img[random_num]

    head = Label(root, text='Hewan Apa nicch?', padx=30, pady=10)
    kotak1 = Label(root, image=chosen_pic)

    if random_num == 0:
        ch1 = Radiobutton(root, text='Singa', variable=r, value=100)
        ch2 = Radiobutton(root, text='Gajah', variable=r, value=1)
        ch3 = Radiobutton(root, text='Penguin', variable=r, value=2)
        ch4 = Radiobutton(root, text='Burung', variable=r, value=3)
    elif random_num == 1:
        ch1 = Radiobutton(root, text='Kucing', variable=r, value=1)
        ch2 = Radiobutton(root, text='Panda', variable=r, value=100)
        ch3 = Radiobutton(root, text='Penguin', variable=r, value=2)
        ch4 = Radiobutton(root, text='Jerapah', variable=r, value=3)
    elif random_num == 2:
        ch1 = Radiobutton(root, text='Penguin', variable=r, value=3)
        ch2 = Radiobutton(root, text='Gajah', variable=r, value=1)
        ch3 = Radiobutton(root, text='Singa', variable=r, value=2)
        ch4 = Radiobutton(root, text='Gorila', variable=r, value=100)

    but1 = Button(root, text='Submit cuy', command=submit)

    head.grid(row=0, column=0, columnspan=2)
    kotak1.grid(row=1, rowspan=4, column=0)
    ch1.grid(row=1, column=1)
    ch2.grid(row=2, column=1)
    ch3.grid(row=3, column=1)
    ch4.grid(row=4, column=1)
    but1.grid(row=5, column=0, columnspan=2)


boot = ImageTk.PhotoImage(Image.open(r'C:\Users\Danangjoyoo\Pictures\meme\Hewan Head Wrong\start.jpg'))
congrat = ImageTk.PhotoImage(Image.open(r'C:\Users\Danangjoyoo\Pictures\meme\Hewan Head Wrong\congrat.jpg'))
salah = ImageTk.PhotoImage(Image.open(r'C:\Users\Danangjoyoo\Pictures\meme\Hewan Head Wrong\salah.jpg'))
ans1 = ImageTk.PhotoImage(Image.open(r'C:\Users\Danangjoyoo\Pictures\meme\Hewan Head Wrong\burunga.jpg'))
ans2 = ImageTk.PhotoImage(Image.open(r'C:\Users\Danangjoyoo\Pictures\meme\Hewan Head Wrong\pandanguin.jpg'))
ans3 = ImageTk.PhotoImage(Image.open(r'C:\Users\Danangjoyoo\Pictures\meme\Hewan Head Wrong\gorijah.jpg'))

boot_pic = Label(root, image=boot)
congrat_pic = Label(root, image=congrat)
salah_pic = Label(root, image=salah)

but0 = Button(root,text='MULAI KUY',padx=30,pady=30,command=start)
but2 = Button(root,text='Coba Lagi!',command=start)

but0.grid(row=0,column=0)


root.mainloop()