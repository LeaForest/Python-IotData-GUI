import time
import tkinter
import tkinter.messagebox
from tkinter import *
#from PIL import ImageTk, Image
import time



def config1():
    admin = "admin"
    passwd = "passwd"
    Topic = "此程序，主要用于水质、空气环境监测数据\n的本地显示！同时，作为响应控制的GUI程序！"

    root = tkinter.Tk()  # 创建窗口对象
    root.title('数据在线监测系统')
    root.resizable(False, False)  # 禁止更改窗口大小

    pic = PhotoImage(file="D:/BG3.png")
    photo = PhotoImage(file="D:/yofc3.gif")
    class page1:
        def __init__(self, master):
            self.master = master
            self.time1display()
            self.photo__()
            self.input2__()

        def input2__(self):
            ground0 = LabelFrame(self.master, text="管理员登陆", padx=20, pady=20)
            ground0.pack(padx=20, pady=20)

            Label(ground0, text="账号:").grid(row=0)
            Label(ground0, text="密码:").grid(row=1)
            J = Entry(ground0)
            J.grid(row=0, column=1, padx=10, pady=5)
            K = Entry(ground0)
            K.grid(row=1, column=1, padx=10, pady=5)

            def show():
                class nullerror(Exception):
                    def __init__(self, arg):
                        self.args = arg
                class wrongerror(Exception):
                    def __init__(self, arg):
                        self.args = arg

                try:
                    if J.get() == admin and K.get() == passwd:
                        tkinter.messagebox.showinfo("欢迎登陆！", "ID:" + J.get() + "\n" + Topic)
                        J.delete(0, END)
                        K.delete(0, END)
                        return True


                    elif J.get() is "" or K.get() is "":
                        raise nullerror("!")
                    else:
                        raise wrongerror("!")
                except nullerror as e:
                    tkinter.messagebox.showinfo("信息", "账号或密码不能为空")
                except wrongerror as f:
                    tkinter.messagebox.showinfo("信息", "请输入正确的账号或密码")


            def enterclick(event):  # 按下回车键将同样相当于按钮触发事件
                show()

            # 将回车响应事件绑入
            if self.master.bind('<Return>', enterclick) and show == True:
                    return True
            elif Button(ground0, text="登陆", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)and show ==True:
                    return True
            else:
                Button(ground0, text="退出", width=10, command=exit).grid(row=3, column=1, sticky=E, padx=10, pady=5)


        def time1display(self):
            D = Label(self.master, text='', justify=LEFT, image=pic, compound=CENTER, font=("幼圆", 20), fg="white")
            D.pack(side=TOP)

            def gettime():
                T2 = time.asctime(time.localtime(time.time()))
                D.configure(text=T2 + "\n\n   环境监测系统管理平台")
                self.master.after(500, gettime)
            gettime()


        def photo__(self):
            ps = Label(self.master, text="Copyright © 2019-2020 nicdo Y.O.F.C", font=("黑体", 10), fg="grey", justify=LEFT,
                       padx=10)
            ps.pack(side=BOTTOM, expand=YES, fill=BOTH)
            imgLabel = Label(self.master, image=photo)
            imgLabel.pack(side=BOTTOM, expand=YES)

    page1(root)
    root.mainloop()




'''
树莓派 做服务器
安装配置
写死IP
控制端连接内网
向树莓派进行通信
Nodemcu+Modbus继电器作客户端
手机+WEB / nodmcu+开关 作无线控制端
'''


