from MainView import MainView
from ActivationView import ActivationView
from tkinter.constants import CENTER
# import psutil
from tkinter import Button, Frame, Tk, Entry, Label
from functools import cached_property
import os

# while True:
#     for process in psutil.process_iter():
#         name = process.name
#         print(name)
#         if name == "syswin.exe":
#             process.kill()


# Window
path_appdata = os.getenv('APPDATA')
appdirectory = os.path.join(path_appdata, ".kprotect")

if os.path.isdir(appdirectory):
    MainView().run()
else:
    ActivationView().run()
