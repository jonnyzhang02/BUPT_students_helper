from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import choose_music
import creep
import show_calendar
import choose_color
import choose_back
import Todolist
import alarm
import desktop_app

window = Tk()  # 创建一个窗体
width = 690
height = 455
# 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2-50)
window.geometry(size_geo)
window.resizable(0,0)

buptphoto = ImageTk.PhotoImage(file="beiyou.jpg"),
buptlabel = Label(window, image=buptphoto)

window.title('邮学小帮手') #修改标题
window.iconbitmap('233.ico')

buptback = Canvas(window, bg="blue", height=450, width=690)
# background_label = Label(window, image=buptphoto)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
buptback.pack()
buptback.create_image(345, 270, image=buptphoto)
window.config(background="#c0c0c0")

def kaifa():
    kf = Toplevel()
    kf.title('开发人员')
    kf.iconbitmap('233.ico')
    width = 300
    height = 200
    # 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = kf.winfo_screenwidth()
    screenheight = kf.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    kf.geometry(size_geo)
    kf.resizable(0, 0)
    kf.config(background="#8000ff")
    l = tk.Label(kf,
    text='孙泽凯-2020212180\n\n张扬-2020212185\n\n王梓安-2020212212',bg='#8000ff',font=('宋体', 18, 'bold'),
    width=200,height=200, fg = '#ffffff',padx=10, pady=15, borderwidth=10, relief="sunken").pack()

button0 = tk.Button(window,
    text='邮   学   小   帮   手',bg='#8000ff',font=('华文琥珀', 35, 'bold'),width=25,height=1, fg = '#ffffff',
    padx=10, pady=15, borderwidth=10, relief="sunken",command=kaifa)
button0.place(x=0,y=0)

def command_creep():
    # 使用 curselection来选中文本
    try:
        creep.creeper()
    except Exception as e:
        e = '发现一个错误'
        messagebox.showwarning(e,'请按照正确步骤使用程序')

global bg_path
bg_path = tk.StringVar()

global class_color
class_color = tk.StringVar()
class_color.set('#000000')

def command_show_calendar():
    try:
        bg_path.set(choose_back.bg_change())
        class_color.set(choose_color.color_return())
        # pic_way = bg_path.get()
        show_calendar.show_calendar(class_color.get(),bg_path.get())
    except:
        show_calendar.show_calendar(class_color.get())

def command_todo():
    try:
        bg_path.set(choose_back.bg_change())
        Todolist.todo_main(bg_path.get())
    except:
        Todolist.todo_main()

def command_alarm():
    # try:
    alarm.alarm_system(0,choose_music.music_change())
    print('1succ')
    # except:
    #     print('2')

def gexinghua():
    wd1 = Toplevel()
    width = 500
    height = 300
    # 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = wd1.winfo_screenwidth()
    screenheight = wd1.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 50)
    wd1.geometry(size_geo)
    wd1.resizable(0, 0)
    wd1.iconbitmap('233.ico')
    wd1.config(background="#8000ff")
    wd1.title('个性化设置')
    def gxh1():
        choose_back.file_saves()
        wd1.quit()
    def gxh2():
        choose_color.color_choose()
        wd1.quit()
    def gxh3():
        choose_music.music_choose()
        wd1.quit()
    def gxh4():
        desktop_app.haha()
        wd1.quit()
    bt1 = tk.Button(wd1, text='背景\n更换', activebackground='yellow', bg = '#e2ad41', font = ('隶书',15),
            width=6, height=2, command=gxh1).pack(side = LEFT,expand = True)
    bt2 = tk.Button(wd1, text='颜色\n选择', activebackground='yellow', bg = '#e2ad41', font = ('隶书',15),
            width=6, height=2, command=gxh2).pack(side = LEFT,expand = True)
    bt3 = tk.Button(wd1, text='提示音\n更换', activebackground='yellow', bg = '#e2ad41', font = ('隶书',15),
            width=6, height=2, command=gxh3).pack(side = LEFT,expand = True)
    bt4 = tk.Button(wd1, text='桌面\n挂件', activebackground='yellow', bg = '#e2ad41', font = ('隶书',15),
            width=6, height=2, command=gxh4).pack(side = LEFT,expand = True)
    wd1.mainloop()

button1 = tk.Button(window, text='获取\n课程信息', activebackground='yellow', bg = '#9301fe',font = ('隶书',12),
            fg='#ffffff', cursor="watch",width=8, height=3, command=command_creep)
button1.place(x=205,y=190)

button2 = tk.Button(window, text = '显示\n课程表', activebackground='yellow', bg = '#9301fe', font = ('隶书',12),
            fg='#ffffff', cursor="watch",width=8,height=3,command=command_show_calendar)
button2.place(x=405,y=190)

button3 = tk.Button(window, text = '设置\n待办事项', activebackground='yellow', bg = '#9301fe', font = ('隶书',12),
            fg='#ffffff', cursor="watch",width=8,height=3,command=command_todo)
button3.place(x=115,y=310)

button4 = tk.Button(window, text = '启用\n提醒系统', activebackground='yellow', bg = '#9301fe', font = ('隶书',12),
            fg='#ffffff', cursor="watch",width=8,height=3,command=command_alarm)
button4.place(x=305,y=310)

button5 = tk.Button(window, text = '个性化\n设置', activebackground='yellow', bg = '#9301fe', font = ('隶书',12),
            fg='#ffffff', cursor="watch",width=8,height=3,command=gexinghua)
button5.place(x=495,y=310)

window.mainloop()  # 进入消息循环