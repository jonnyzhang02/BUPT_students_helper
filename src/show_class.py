import datetime
import time
from tkinter import *
import openpyxl
from PIL import Image, ImageTk

t = []


def read_class_info():
    workbook = openpyxl.load_workbook('课程表.xlsx')
    sheet = workbook['课程表']
    class_info_ = [[]]
    for r in range(14):
        for c in range(112):
            temp = sheet.cell(row=r + 1, column=c + 1).value
            one = temp.find('\n')
            two = temp.find('\n', one + 1)
            if not one == -1:
                temp = temp[:two]
            class_info_[r].append(temp)
        class_info_.append([])
    return class_info_


def draw_window(pic_way, cv):
    if pic_way:
        img_open = Image.open(pic_way)
        global img_png
        img_png = ImageTk.PhotoImage(img_open)
        cv.create_image(600, 350, image=img_png)
    week_names = ["星期一", "星期二", "星期三", "星期四", "星期五"]
    class_times = ["第1节\n08:00-08:45", "第2节\n08:50-09:35", "第3节\n09:50-10:35", "第4节\n10:40-11:25", "第5节\n11:30-12:15",
                   "第6节\n13:00-13:45", "第7节\n13:50-14:35", "第8节\n14:45-15:30", "第9节\n15:40-16:25", "第10节\n16:35-17:20",
                   "第11节\n17:25-18:10", "第12节\n18:30-19:15", "第13节\n19:20-20:05", "第14节\n20:10-20:55",
                   "第14节\n20:10-20:55"]
    for day in range(5):
        cv.create_text(150 + day * 200, 20, text=week_names[day], fill='#FF1493', font=('微软雅黑', 10, 'bold'))  # 星期文字
        for line in range(14):
            if day == 0:
                cv.create_text(50, 80 + line * 45, text=class_times[line], fill='#FF1493',
                               font=('微软雅黑', 10, 'bold'))  # 节次文字

def print_class(week, cv, class_info,color):
    global t
    if not week:
        t_new = print_class(get_current_week(), cv, class_info,color)
    else:
        for each_ in t:
            cv.delete(each_)
        t_new = [cv.create_text(50, 30, text="第{}周".format(week), fill='#FF1493', font=('微软雅黑', 15, 'bold'))]
        for day in range(5):
            for line in range(14):
                t_new.append(
                    cv.create_text(150 + day * 200, 80 + line * 45, fill=color,
                                   text=class_info[line][(week - 1) * 7 + day],
                                   font=('微软雅黑', 10, 'bold')))  # 课程文字
    return t_new


def get_current_week():
    date0 = '2022-02-28'
    d0 = datetime.datetime.strptime(date0, '%Y-%m-%d')
    date1 = time.strftime("%Y-%m-%d", time.localtime())
    d1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    return int((d1 - d0).days / 7) + 1


def show_calendar(colour,pic_way=''):
    # create window
    root = Tk()
    root.config(bg='#BFEFFF')
    root.title("邮学小帮手")
    root.geometry('1300x700')
    class_info = read_class_info()
    # root.iconbitmap('之后的图标路径')
    cv = Canvas(root, bg="#BFEFFF", width=1200, height=700)  # create canvas
    global t

    draw_window(pic_way, cv)
    t = print_class(0, cv, class_info,colour)

    weeks_F = []
    for i in range(17):
        exec('''def week_{}(cv=cv, class_info=class_info, color = colour):
                    global t
                    t = print_class({}, cv, class_info, color)'''.format(i, i))
        weeks_F.append("week_{}".format(i))
    temp = 1

    Button(root, text="当前周".format(temp), command=eval('week_0'), fg='#FF7256', activeforeground='#CD6600',
           font=('微软雅黑', 18, 'bold')).place(x=1205, y=15)
    for each in weeks_F[1:]:
        Button(root, text="第{0:^5}周".format(temp), command=eval(each), fg='#FF7256', activeforeground='#CD6600',
               width=10,font=('微软雅黑', 10, 'bold')).place(x=1205, y=40 + temp * 36)
        temp = temp + 1

    cv.pack(anchor='w')
    root.mainloop()

# show_calendar('#000000')