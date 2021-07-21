import os
from MainView import MainView
from tkinter.constants import CENTER
# import psutil
from tkinter import Button, Frame, Tk, Entry, Label
from functools import cached_property, partial
from path import Path

# path_appdata = os.getenv('APPDATA')
# appdirectory = os.path.join(path_appdata,".syskiller")


# while True:
#     for process in psutil.process_iter():
#         name = process.name
#         print(name)
#         if name == "syswin.exe":
#             process.kill()


class ActivationView():

    
    def run(self) -> None :
        
        window = Tk()
        window.geometry('560x560')
        window.title('Syskiller')
        window.configure(bg='black')
        window.resizable(False, False)


        login_window = Frame(window, width=400, height=450, bg='white')
        login_window.place(x=80, y=45)
        
        #Login Text
        login_text = Label(window, text='Activation', font=('Roboto',20))
        login_text.configure(fg='black', bg='white')
        login_text.place(x=100, y=180)


        key = Entry(window)
        key.configure(bg='white', fg='black', font=('Roboto',18))
        key.place(x=100, y=240, height=40, width= 360)

        #Login Button

        login_button = Button(window, text='Activer', fg='white', bg='red', command= lambda: self.login(key.get(),window))
        login_button.place(x=180, y=300, height=50, width=200)

        window.mainloop()

        #Login Function
    def login(self,key,window):

        if key == "E89AB9635E2CA":
            success = Label(text='Success. You Loged in', fg='green', bg='white')
            success.place(x=245, y=355)
            try:
                os.mkdir(".kprotect")
                window.destroy()
                MainView().run()
            except OSError as error:
                print(error)
        else:
            feiled = Label(text='Incorrect Email Or Password', fg='red', bg='white')
            feiled.place(x=245, y=355)
    def activate(self) -> bool:
        return