import random
import time
import tkinter
import tkinter.messagebox
from tkinter import *


def config2():
    root.destroy()
    root.quit()

    branch = tkinter.Tk()
    branch.resizable(False, False)  # 禁止更改窗口大小
    branch.title('数据在线监测系统')

    class page2:
        def __init__(self, master):
            self.master = master
            self.statubutt()
            self.datadisplay()

        def statubutt(self):  # '单选按钮：LabelFrame(), Radiobutton()'
            ground_ = LabelFrame(self.master, text="", padx=3, pady=1)
            ground_.pack(side=LEFT)
            ground = LabelFrame(ground_, text="", padx=3, pady=1)
            ground.pack(side=TOP)

            '配置一个块'
            ground2 = LabelFrame(ground, text="开关控制", padx=3, pady=10)  # 框内元素和框的距离
            ground2.pack(padx=1, pady=1, side=LEFT, anchor=W)  # 框与框或窗口边界的距离

            H = IntVar()
            H.set(1)
            Radiobutton(ground2, text="开", variable=H, value=1).grid(stick=W, row=0, column=0)
            Radiobutton(ground2, text="关", variable=H, value=2).grid(stick=E, row=0, column=1)
            Radiobutton(ground2, text="     自  动      ", variable=H, value=3, indicatoron=False).grid(stick=S, padx=5,pady=5, )
            '通过 indicatoron=False 改变按钮方块填充效果'

            ground4 = LabelFrame(ground, text="时间显示", padx=3, pady=10)
            ground4.pack(padx=1, pady=1, side=RIGHT, anchor=W)

            G = Label(ground4, text='', font=("楷体", 15), fg="blue", justify=RIGHT, padx=10)
            G.pack(anchor=S)

            def gettime():
                T2 = time.strftime("%Y-%b-%d\n  %H:%M:%S \n%a   ", time.localtime(time.time()))
                G.configure(text=T2)
                self.master.after(500, gettime)
            gettime()

            def list__():
                ground5= LabelFrame(ground_, text="查看日志", padx=1, pady=10)
                ground5.pack(padx=1, pady=1, side=BOTTOM, anchor=W)
                scroll = Scrollbar(ground5)  # 创建列表滑块
                scroll.pack(side=RIGHT, fill=Y)
                list_ = ['2019-9-15.txt', '2019-9-16.txt', '2019-9-17.txt', '2019-9-18.txt', '2019-9-19.txt',
                         '2019-9-20.txt', '2019-9-21.txt', '2019-9-22.txt', '2019-9-23.txt', '2019-9-24.txt',
                         '2019-9-25.txt']
                A = Listbox(ground5, font=("楷体", 15), fg="green", yscrollcommand=scroll.set)  # 列表内容
                for item in list_:
                    A.insert(50, item)
                A.pack(side=LEFT, anchor=W)
                Button(ground5, text="删除文件", command=lambda x=A: x.delete(ACTIVE)).pack(padx=1, pady=1,)  # 列表添加删除按钮
                scroll.config(command=A.yview)
            list__()

        def datadisplay(self):
            # ground3 = LabelFrame(self.master, text="数据显示", padx=4, pady=5)
            ground3 = Frame(self.master)
            ground3.pack(side=RIGHT)

            L = Label(ground3, text=' ', font=("楷体", 20), fg="green", justify=RIGHT)
            L.pack(side=TOP, anchor=N, fill=X, expand=YES, padx=10)

            I = Label(ground3, text=' ', font=("楷体", 20), fg="green", justify=RIGHT)
            I.pack(side=TOP, anchor=CENTER, fill=X, expand=YES, padx=10)

            J = Label(ground3, text=' ', font=("楷体", 20), fg="green", justify=RIGHT)
            J.pack(side=TOP, anchor=S, fill=X, expand=YES, padx=10)

            def getvalue():
                value1 = round(random.uniform(0, 9), 1)
                value2 = round(random.uniform(10, 20), 1)
                value3 = round(random.uniform(0, 30), 1)
                L.configure(text="P H:" + str(value1))
                I.configure(text="水氧:" + str(value2))
                J.configure(text="水温:" + str(value3))
                self.master.after(2000, getvalue)
            getvalue()

    page2(branch)
    branch.mainloop()

