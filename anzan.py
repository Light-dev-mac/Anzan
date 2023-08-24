from tkinter import *
from tkinter import ttk
import numpy as np

def push_button():
   print(txt.get())
win = Tk()
win.title('test')
#エデットボックス作成
txt = StringVar()
edit = ttk.Entry(win, textvariable=txt) 
edit.grid(row=1,column=1)
edit.grid_configure(padx=5, pady=5)
#ボタン作成
button = ttk.Button(win, text='OK', command=push_button)
button.grid(row=2,column=2)
button.grid_configure(padx=5, pady=5)
button2 = ttk.Button(win, text='ボタンを押してね', command=push_button)
button2.grid(row=5,column=2)
button2.grid_configure(padx=5, pady=5)
win.mainloop()

# if __name__ == '__main__':
#     baseGround = Tk()
#     baseGround.geometry('500x300')
#     title = baseGround.title("ANZAN")
#     for i in range(20):
#         r = np.random.rand()
#         questionMessage = ""
#         if r < 0.2:
#             a1 = (1000 - 10 ) * np.random.rand() + 10 
#             questionMessage = f"{0}✕ 11".format(a1)
#         elif r < 0.4:
#             a1 = ((10 - 1) * np.random.rand() + 1 ) * 10 + 5
#             questionMessage = f"{0} ^2".format(a1)
#         elif r < 0.6:
#             b = (10 - 1) * np.random.rand() + 1 
#             a1 = ((10 - 1) * np.random.rand() + 1 ) * 10 + b
#             a2 = ((10 - 1) * np.random.rand() + 1 ) * 10 + (10-b)
#             questionMessage = f"{0} ✕ {1}".format(a1, a2)
#         elif r < 0.8:
#             a1 = (10000 - 1000) * np.random.rand() + 1000
#             a2 = (1000 - 100) * np.random.rand() + 100
#             questionMessage = f"{0} ✕ {1}".format(a1, a2)
                
        
#         lable = ttk.Label(text=questionMessage, foreground="orange", background="black")
#         lable.pack()
#         baseGround.mainloop()