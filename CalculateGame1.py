import numpy as np
from tkinter import *
import random

class Game(Frame):
    __numbers = np.arange(2,7)

    def __init__(self,master):
        Frame.__init__(self,master)
        self.__value1 = 0
        self.__value2 = 0
        self.pack()
        self.board()

    def board(self):
        self.__rand = random.choice(Game.__numbers)
        self.__dispNum = Label(self,text=self.__rand)
        self.__dispNum.grid(row=0,column=1)
        #self.__dispNum.pack(side=TOP)

        # box 1:1
        self.__box11 = Button(self,padx=10,pady=10,fg='yellow',bg='black',text='1',command=self.butval1)
        self.__box11.grid(row=1,column=0)
        # box 1:2
        self.__box12 = Button(self, padx=10, pady=10, fg='yellow', bg='black', text='2',command=self.butval2)
        self.__box12.grid(row=1,column=1)
        # box 1:3
        self.__box13 = Button(self, padx=10, pady=10, fg='yellow', bg='black', text='3',command=self.butval3)
        self.__box13.grid(row=1,column=2)
        # SIGN MATHEMATICS
        self.__inpSignPlus = Button(self, padx=7, pady=7, fg='red', bg='white', text='+')
        self.__inpSignPlus['command'] = self.signPlus
        self.__inpSignPlus.grid(row=3,column=1)
        #restart-BUTTon
        self.__resBut = Button(self,padx=5, pady=10, fg='white', bg='blue', text='Play Again!',command=self.restart)
        self.__resBut.grid(row=4,column=1)

    def transferValueFromButton(self,value):
        if self.__value1 == 0:
            self.__value1 = value
            print('value1 inserted')
        elif self.__value1 != 0:
            self.__value2 = value
            print('value2 inserted')
            self.calculate()
    def butval1(self):
        self.transferValueFromButton(1)
    def butval2(self):
        self.transferValueFromButton(2)
    def butval3(self):
        self.transferValueFromButton(3)

    def signPlus(self):
        self.__signMath = '+'

    def calculate(self):
        if self.__signMath == '+':
            self.__result = self.__value1 + self.__value2
            if self.__result == self.__rand:
                print('GREAT!')
            else:
                print('WRONG')
    def restart(self):
        self.__rand = random.choice(Game.__numbers)

root = Tk()
game = Game(root)
game.mainloop()
root.destroy()