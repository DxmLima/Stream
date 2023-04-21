
from tkinter import Tk, Entry, Button, StringVar


class Deck:
    def __init__(self, master):
        master.title("AtenaDev")
        master.geometry('750x550+0+0')
        master.config(bg='black')
        master.resizable(False, False)

        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.print()).place(x=100, y=50)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=100, y=150)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=100, y=250)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=200, y=50)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=300, y=50)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=400, y=50)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=500, y=50)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=200, y=150)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=300, y=250)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=400, y=250)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=500, y=250)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=300, y=150)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=400, y=150)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=500, y=150)
        Button(width=11, height=4, text='X', relief='flat', bg='white',
               command=lambda: self.show('Y')).place(x=200, y=250)

    def print(self):
        print("Hello Dev")

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)


root = Tk()
atenadev = Deck(root)
root.mainloop()
