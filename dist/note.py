
'''
**********************************************************************************************
*****************************************  Tkinter GUI  **************************************
**********************************************************************************************
Thinker总共提供了三种布局组件的方法：pack(),grid()和place()
grid()：
    允许用表格的形式来管理组件的位置，row代表行，column代表列：如row=1，column=2表示第二行第三列(0表示第一行)
    stick用来设置组件的位置：                                   N
                                                             NW | NE
                                                          W -- -|- -- E
                                                             SW | SE
                                                                S
pack()：
       side:按扭停靠在窗口的位置：LEFT、TOP、RIGHT、BOTTOM
       ------ SIDE 优先级大于 anchor!!!! ------
       anchor:方位：N、E、S、W、CENTER
       fill:填充：X、Y、BOTH、NONE
       expand:扩展：YES、NO
       pad:边距：padx = x方向外边距、pady = y方向的外边距、ipadx = x方向的内边距、ipady = y方向的内边距
'''
#######################################################################################################################
'''
'列表块:Listbox()'



                pho = PhotoImage(file='D:/BG2.png')
                canvas = Canvas(self.master, width=680, height=380, bd=0, highlightthickness=0, bg='#00FFFF')
                canvas.pack(expand=YES, fill=BOTH)
                canvas.create_image(340, 180, image=pho)
                # canvas.create_window(100, 50, width=100, height=20, window=datadisplay)
                canvas.create_text( 340, 180,text='')


                pho = PhotoImage(file='D:/BG2.png')
                canvas = Canvas(self.master, width=680, height=380, bd=0, highlightthickness=0, bg='#00FFFF')
                canvas.pack(expand=YES, fill=BOTH)
                canvas.create_image(340, 180, image=pho)
                #canvas.create_window(100, 50, width=100, height=20, window=datadisplay)
                canvas.create_text(300,150,text='')

        canvas = tkinter.Canvas(width=680, height=380, bd=0, highlightthickness=0)
        canvas.pack(expand=YES, fill=BOTH)
        pho = ImageTk.PhotoImage(Image.open('D:/BG2.png'))
        canvas.create_image(340, 180, image=pho)
        #canvas.create_window(100, 50, width=100, height=20,window=root)
'''

'''
'文本显示:Lable()'
def txt__(branch):
    B = Label(branch, text=Topic,font=("楷体",15),
              fg = "blue",justify=LEFT, padx=10)
    B.pack(side=TOP)
'''
'''
'多选按钮：LabelFrame(),Checkbutton()'
def checkbutt__(branch):
    ground1 = LabelFrame(branch,text= "项目选项",padx = 15,pady = 15)
    ground1.pack(padx=10, pady=10,side = RIGHT)

    E = ["项目一","项目二","项目三"]
    F = []
    for check in E:
        F.append(IntVar())
        G = Checkbutton(ground1,text = check,variable = F[-1])
        G.pack(anchor = N)
'''

'''
'背景设置:PhotoImage()'
def photo__():
    pic = PhotoImage(file="D:/BG.gif")
    D = Label(root, text=T1,
              justify=LEFT, image=pic, compound=CENTER, font=("幼圆", 20), fg="white")
    D.pack()

    photo = PhotoImage(file="D:/arduino.gif")
    imgLabel = Label(root, image=photo)
    imgLabel.pack(side=BOTTOM)


'输入框：Entry(),insert()'
def input__(branch):
    I = Entry(branch)
    I.pack(padx =20, pady = 20)
    I.delete(0,END)
    I.insert(0,"请输入Modbus指令：")


'响应按钮:tkinter.messagebox.showinfo(),tkinter.Button()'
def button__(branch):
    def CallBack():
        tkinter.messagebox.showinfo("警告", "输入有误")
        # 第二页的”注销“——重启服务
    Button(branch, text="确认", command=CallBack, fg="blue").pack()


