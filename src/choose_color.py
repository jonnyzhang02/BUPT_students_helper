def color_choose():
    import tkinter as tk
    import re
    from tkinter import colorchooser

    findcolor = re.compile(r", '(.*?)'")  # 匹配企业
    def kebiaocolor():
        global kebiao_color
        kebiao_color = str(colorvalue)
        kebiao_color = re.findall(findcolor, kebiao_color)[0]  # 获取单位


    root = tk.Tk()
    root.title("颜色选择")
    root.geometry('400x200+300+300')
    root.iconbitmap('233.ico')
    def callback():
        # 打开颜色对话款
        global colorvalue
        colorvalue = tk.colorchooser.askcolor()
        # 在颜色面板点击确定后，会在窗口显示二元组颜色值
        lb.config(text='颜色值:'+ str(colorvalue))
    lb=tk.Label(root,text='',font=('宋体',10))
    # 将label标签放置在主窗口
    lb.pack()
    tk.Button(root, text="点击选择颜色", command=callback, width=14, bg='#808080').pack()
    tk.Button(root, text='设为课程字体颜色',command=kebiaocolor, width=14, bg='#808080').pack()
    # 显示界面
    root.mainloop()
kebiao_color = '#000000'
def color_return():
    return kebiao_color
