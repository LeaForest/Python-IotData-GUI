# -*- encoding = UTF-8 -*-
import time
import threading
import login
import display
from login import config1

if __name__ == '__main__':

    thread1 = threading.Thread(target = login.config1)
    thread2 = threading.Thread(target = display.config2)
    thread1.start()

    #if val.input2__() is True:
     #   print('呼啦')
    #if login.config1.page1.input2__():
    #    thread2.start()
    #    root.destroy()
    #    root.quit()

