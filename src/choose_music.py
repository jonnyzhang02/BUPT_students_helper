# import tkinter as tk
# from tkinter import ttk
# import time
#
#
# class DigitalClock(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         # configure the root window
#         self.title('Digital Clock')
#         self.resizable(0, 0)
#         self.geometry('250x80')
#         self['bg'] = 'black'
#
#         # change the background color to black
#         self.style = ttk.Style(self)
#         self.style.configure(
#             'TLabel',
#             background='black',
#             foreground='red')
#
#         # label
#         self.label = ttk.Label(
#             self,
#             text=self.time_string(),
#             font=('Digital-7', 40))
#
#         self.label.pack(expand=True)
#
#         # schedule an update every 1 second
#         self.label.after(1000, self.update)
#
#     def time_string(self):
#         return time.strftime('%H:%M:%S')
#
#     def update(self):
#         """ update the label every 1 second """
#
#         self.label.configure(text=self.time_string())
#
#         # schedule another timer
#         self.label.after(1000, self.update)
#
#
# if __name__ == "__main__":
#     clock = DigitalClock()
#     clock.mainloop()

import tkinter as tk
from tkinter import filedialog
from PIL import Image
filepath = 'Bubble.mid'

global mark
mark = 0
def music_choose():

    def open_music():
        try:
            global img
            global filepath
            filepath = filedialog.askopenfilename() # 打开文件，返回该文件的完整路径
            filename.set(filepath)
            global mark
            mark = 1
        except Exception as e:
            print("您没有选择任何文件",e)
            mark = 0

    def save_music():
        try:
            if mark == 1:
                music_var.set('已设为提示音！')
            else:
                music_var.set('请选择一个文件！')
        except Exception as e:
            print(e)


    window = tk.Toplevel()
    window.title("更换提示音")
    window.geometry('400x200+300+300')
    window.iconbitmap('233.ico')
    filename = tk.StringVar()
    music_var = tk.StringVar()
    # 定义读取文件的组件
    entry = tk.Entry(window, textvariable=filename)
    entry.grid(row=1, column=0, padx=5, pady=5)
    tk.Button(window, text='选择音频', command=open_music).grid(row=1, column=1, padx=5, pady=5)
    # 定义保存文件的组件
    entry1 = tk.Entry(window, textvariable=music_var)
    entry1.grid(row=2, column=0, padx=5, pady=5)
    tk.Button(window, text='设置音频', command=save_music).grid(row=2, column=1, padx=5, pady=5)
    window.mainloop()


def music_change():
    return filepath
