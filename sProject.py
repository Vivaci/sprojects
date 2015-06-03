#-------------------------------------------------------------------------------
# Name:        Summer Project
# Author:      Vivaci
#
# Created:     03/06/2015
# Copyright:   (c) Vivaci 2015
# Licence:     Yao Inc.
#-------------------------------------------------------------------------------

# Modules
from tkinter import *
import re


class introWindow:
    def __init__ (self, x=800, y=500):
        self.x = x
        self.y = y
        self.root = Tk()
        self.canvas = Canvas(self.root,width=self.x,height=self.y)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.center(self.root)

#Label for title

        lab1 = Label(self.root,
               text="Welcome to Daniel's Applications\nDeveloped: Summer 2015",
               font=("Helvetica", 16))
        lab1.pack()
        self.canvas.create_window(400,25,window = lab1)

#Create Menu Buttons

        AboutDevButton = Button(self.root,
                                text="About the developer",
                                padx=30,pady=10,
                                command=None)
        AboutDevButton.pack()
        AboutDevButton.place(bordermode=OUTSIDE,
                             x=100, y=150,
                             height=50, width=150)


        FirstApp = Button(self.root,
                          text="FirstApp",
                          padx=30,pady=10,
                          command=None)
        FirstApp.pack()

        SecondApp = Button(self.root,
                           text="SecondApp",
                           padx=10,pady=10,
                           command=None)
        SecondApp.pack()

        #self.label1 = Label(self.root, textvariable=var)
        #label.grid(column=0, row=0)
        self.root.title("Daniel's Applications")
        self.root.bind("<KeyPress>", self.keyPress)
        self.root.mainloop()

    def center(self,root):
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        root1 = root.winfo_width()
        root2 = root.winfo_height()
        x = w/2 - root1/2
        y = h/2 - root2/2
        root.geometry("+%d+%d" % ((x/2, y/2)))


    def keyPress(self, event):
        pass


def main():
    #ele = "1 dsafd 4 asdfij 56 asdf"
    #result = re.split("\D+", ele)
    #print(result)
    introWin = introWindow()



main()