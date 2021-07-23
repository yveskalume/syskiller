from Killer import Killer
from tkinter.constants import BOTTOM, CENTER, LEFT
from tkinter import Button, Frame, PhotoImage, Tk, Entry, Label
from functools import cached_property
import turtle
import threading


class MainView():

    def run(self):
        # window = Tk()
        # window.geometry('300x200')
        # window.title('Syskiller')
        # window.configure(bg='white')
        # window.resizable(False, False)

        # mImage = PhotoImage(file='icone.png')

        # button = Button(window,image = mImage)
        # button.config(bg='white')
        # button.pack(anchor=CENTER)

        # text = Label(window, text='Vous etes protege', font=('Roboto',20))
        # text.configure(fg='white')
        # # text.place(y=80)
        # text.pack(anchor=CENTER,side=BOTTOM)

        # window.mainloop()
        threading.Thread(target=self.design).start()
        threading.Thread(target = Killer().run()).start()

    def design(self):
        screen = turtle.Screen()
        screen.setup(400, 400)
        colors = ["pink", "yellow", "blue", "green", "white", "red"]
        sketch = turtle.Pen()
        turtle.bgcolor("black")
        turtle.title("Syskiller")

        for i in range(200):
            sketch.pencolor(colors[i % 6])
            sketch.width(i / 100 + 1)
            sketch.forward(i)
            sketch.left(59)
        turtle.Screen().exitonclick()
