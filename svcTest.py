import time
import random
from pathlib import Path
from SMWinservice import SMWinservice
import os

def appendInfoToFile(path,filename,strcontent):
    txtFile=open(path+filename,'a+')
    txtFile.write(strcontent)
    txtFile.close()

class svcTest(SMWinservice):
    _svc_name_ = "svcTEST"
    _svc_display_name_ = "svcTEST"
    _svc_description_ = "Let's see if this works..."

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            for i in range(1,4):
                appendInfoToFile('C:\\Users\\1098350515\\Documents\\','test.txt','hey')
            appendInfoToFile('C:\\Users\\1098350515\\Documents\\','test.txt','--------------------------------')    

            
            
            


if __name__ == '__main__':
    svcTest.parse_command_line()