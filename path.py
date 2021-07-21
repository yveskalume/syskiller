import os

class Path():

    def __init__(self) -> None:
        self.path_appdata = os.getenv('APPDATA')
        self.appdirectory = os.path.join(self.path_appdata,".syskiller")