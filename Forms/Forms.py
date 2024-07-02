from tkinter import *

class MainWindow(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Smart Truck")
        self.config(bg="skyblue")
        self.maxsize(900, 600)
        self.left_frame = Frame(self, width=200, height=400)
        self.left_frame.grid(row=0,column=0,padx=10,pady=5)
        self.right_frame = Frame(self, width=650, height=400, bg="grey")
        self.right_frame.grid(row=0, column=1, padx=10, pady=5)
    
    def chargeControllers(self):
        self.Btn1 = Button(self.left_frame, text="hello")
        self.Btn1.grid()

    def show_frame(self):
        self.frame.tkraise()
        