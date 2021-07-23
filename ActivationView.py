import os
from MainView import MainView
from tkinter.constants import CENTER
# import psutil
from tkinter import Button, Frame, Tk, Entry, Label, PhotoImage, Canvas
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

    def run(self) -> None:

        window = Tk()
        window.geometry('560x560')
        window.title('Syskiller')
        window.configure(bg='black')
        window.resizable(False, False)
        #window.iconbitmap('./icon.ico')

        login_window = Frame(window, width=400, height=450, bg='white')
        login_window.place(x=80, y=45)
        # Login Text
        login_text = Label(login_window, text='Activation', font=('Roboto', 20))
        login_text.configure(fg='black', bg='white')
        login_text.place(x=200, y=80, anchor='center')

        # Info Login Text
        label_text = Label(login_window, text='Veuillez entrez une clé d\'activation pour l\'utilisation du logiciel',
                          wraplengt=200, font=(15))
        label_text.configure(fg='black', bg='white')
        label_text.place(x=200, y=150, anchor='center')

        key = Entry(window)
        key.configure(bg='white', fg='black', font=('Roboto', 18))
        key.place(x=100, y=240, height=40, width=360)

        # Login Button

        login_button = Button(window, text='Activer', fg='white', bg='red',
                              command=lambda: self.login(key.get(), window))
        login_button.place(x=180, y=300, height=50, width=200)

        # Contact number and phone number
        """
        canva = Canvas(login_window, width=150, height=40, bg='white', highlightthickness=0)
        img = PhotoImage(file='./phone.png', master=login_window)
        canva.create_image(25, 20, image=img)
        canva.create_text(90, 20, text='contactez nous:', font=(13))
        canva.place(x=200, y=380, anchor='center')"""

        phone_label = Label(login_window, text="contactez nous:", font=(13))
        phone_label.configure(fg="black", bg="white")
        phone_label.place(x=200, y=380, anchor='center')

        phone_text = Label(login_window, text='+243 97 493 9405', font=(13))
        phone_text.configure(fg='black', bg='white')
        phone_text.place(x=200, y=410, anchor='center')

        window.mainloop()

        # Login Function

    def login(self, key, window):

        if key == "E89AB9635E2CA":
            success = Label(text='Success. You Loged in', fg='green', bg='white')
            success.place(x=245, y=355)
            try:
                path_appdata = os.getenv('APPDATA')
                appdirectory = os.path.join(path_appdata, ".kprotect")
                os.mkdir(appdirectory)
                window.destroy()
                MainView().run()
            except OSError as error:
                print(error)
        else:
            feiled = Label(text='Incorrect Email Or Password', fg='red', bg='white')
            feiled.place(x=245, y=355)

    def activate(self) -> bool:
        return
