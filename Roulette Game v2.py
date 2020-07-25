import random
import numpy as np
from tkinter import *

class wheel(Frame):
    __random_number = np.arange(1,33)
    __trial = 0
    __trialLeft = 10
    __gameStateOver = False

    def spin(self):
        num1 = self.__e1
        num2 = self.__e2
        num3 = self.__e3
        rand1 = random.choice(wheel.__random_number)
        rand2 = random.choice(wheel.__random_number)
        rand3 = random.choice(wheel.__random_number)
        if num1 == rand1:
            print('NICE GUESS! =>> {} == {}'.format(num1,rand1))
        elif num1 != rand1:
            print('try again!')
        if num2 == rand2:
            print('NICE GUESS! =>> {} == {}'.format(num2,rand2))
        elif num2 != rand2:
            print('try again!')
        if num3 == rand3:
            print('NICE GUESS! =>> {} == {}'.format(num3,rand3))
        elif num1 != rand1:
            print('try again!')
        if num1 == rand1 and num2 == rand2 and num3 == rand3:
            print('GREATT YOU WIN!')
        else:
            print('THE NUMBER IS {} | {} | {} \nYOU LOSE! TRY AGAIN!'.format(rand1,rand2,rand3))

    def getTrial(self):
        return self.__trial

    def cetak1(self):
        self.cetakGrand(1)

    def cetakGrand(self,value):
        print(value)

    def gameWidget(self):
        self.entry1 = Entry(self)
        self.entry1['width'] = 15
        self.entry1.pack(side=LEFT)
        self.__e1 = self.entry1.get()
        self.entry2 = Entry(self)
        self.entry2['width'] = 20
        self.entry2.pack(side=LEFT)
        self.__e2 = self.entry2.get()
        self.entry3 = Entry(self)
        self.entry3['width'] = 25
        self.entry3.pack(side=LEFT)
        self.__e3 = self.entry3.get()

        self.submit = Button(self)
        self.submit["text"] = "SUBMIT!"
        self.submit['command'] = self.cetak1
        self.submit.pack(side=TOP)

    def gameover(self):
        if self.__trialLeft - self.__trial <= 0:
            self.__gameStateOver = True
        else:
            self.__gameStateOver = False
        return self.__gameStateOver

    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        self.gameWidget()

root = Tk()
app = wheel(master=root)
app.mainloop()
root.destroy()