import psutil
import time

class Killer():

    def run(self) :
        while True:
            for process in psutil.process_iter():
                name = process.name
                print(name)
                if name == "syswin.exe":
                    process.kill()
            time.sleep(4)