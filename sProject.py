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
    def __init__ (self, x=800, y=600):
        self.x = x
        self.y = y
        self.root = Tk()
        self.root.bind("<F12>", self.full)
        self.root.geometry("%dx%d" % (self.x,self.y))
        self.winW, self.winH = self.root.winfo_reqwidth(), self.root.winfo_reqheight()
        #print(self.winW, self.winH)
        self.localW = 0
        self.localH = 0
        self.fullscreen = False




#Frame/Label for title

        self.center(self.root)
        #self.root.resizable(width=FALSE,height=FALSE)
        self.frame = Frame(self.root, width = self.x, height=self.y,bg="#0033CC", padx=10,pady=20)
        self.frame.pack(side=RIGHT,fill=BOTH,expand=1)
        self.frame2 = Frame(self.root, width = 200, height=self.y, bg="#0066FF", relief= SUNKEN)
        self.frame2.pack(side=LEFT,fill=Y)
        self.lab1 = Label(self.frame,
               text="Welcome to Cray's Auto KNL Tests\nDeveloped by: Dan Yao - Summer 2015",
               font=("Times New Roman", 18), bg="#0066FF",pady=5,padx=10, relief=GROOVE)
        self.lab1.pack(side=TOP)
        self.innerCanvasFrame = Frame(self.frame, bd=4, relief=RAISED)
        self.innerCanvasFrame.pack(expand=1,fill=BOTH,pady=(40,20),padx=10)
        self.canvas = Canvas(self.innerCanvasFrame,width=self.x-250,height=self.y,scrollregion=(0,0,1000,1000), bg="gray")

#Scrollbar

        self.hbar = Scrollbar(self.innerCanvasFrame,orient=HORIZONTAL)
        self.hbar.pack(side=BOTTOM,fill=X)
        self.hbar.config(command=self.canvas.xview)
        self.vbar = Scrollbar(self.innerCanvasFrame,orient=VERTICAL)
        self.vbar.pack(side=RIGHT,fill=Y)
        self.vbar.config(command=self.canvas.yview)
        self.canvas.config(width=self.x-250,height=self.y)
        self.canvas.config(xscrollcommand=self.hbar.set,yscrollcommand=self.vbar.set)
        self.canvas.pack(side=TOP, fill=BOTH, expand=1)
        self.ims = PhotoImage(file="about.gif")

#Cray Logo

        im = PhotoImage(file="logo.gif")
        self.logo= Label(self.frame2,image=im)
        self.logo.photo = im
        self.logo.pack(side=TOP)

#Create Menu Buttons

        AboutDevButton = Button(self.frame2,
                                text="About the developer",
                                padx=30,pady=10,
                                command=lambda: self.about(self.canvas))
        AboutDevButton.pack(side=TOP,fill=X)

        FirstApp = Button(self.frame2,
                          text="FirstApp",
                          padx=30,pady=10,
                          command=None)
        FirstApp.pack(side=TOP,fill=X)

        SecondApp = Button(self.frame2,
                           text="SecondApp",
                           padx=30,pady=10,
                           command=None)
        SecondApp.pack(side=TOP, fill=X)
        self.root.title("Daniel's Applications")
        #self.root.bind("<KeyPress>", self.keyPress)
        self.root.mainloop()


#Centering to middle of screen

    def center(self,root):
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        root1 = root.winfo_width()
        root2 = root.winfo_height()
        print(root1,root2)
        x = w/2 - root1/2
        y = h/2 - root2/2
        root.geometry("+%d+%d" % ((x/2, y/2-100)))


#Fullscreen function

    def full(self, event):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        if self.fullscreen:
            self.root.geometry("%dx%d+350+100" % (self.x,self.y))
            self.fullscreen=False
        else:
            self.localH,self.localW=self.winH,self.winW
            print(self.localH,self.localW)
            self.root.geometry("%dx%d+0+0" % (w,h-75))
            self.fullscreen=True

#About developer canvas

    def about(self, canvas):
        canvas.delete("all")
        self.lab1['text']='About the Developer: Daniel Yao'
        canvas.create_image(100, 100, image = self.ims, state=NORMAL)
        textLabel = Label(canvas,
               text="Daniel Yao is a Junior at the University of Minnesota - Twin Cities.\
                     He is currently an Diagnostics Intern at Cray Supercomputers working\
                     on diags tests for the new Intel Xeon Phi processor KNL. \
                     This is a automated system dedicated to scheduling tests and\
                     viewing the results of these tests in GUI. This is an attempt to\
                     produce a more consolidated way to run diagnostics tests on Cray systems.",
               font=("Times New Roman", 14),bg="gray",pady=5,anchor=W,wraplength=500)
        textLabel.pack()
        canvas.create_window(250,250,window=textLabel)


def main():

    introWin = introWindow()

main()