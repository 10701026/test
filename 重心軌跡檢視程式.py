import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
F1z_length=100
def plot_chart1():
    global F1z_length
    F1z_length = len(F1z_data)  # 取得 F1z 的長度
    ax1.clear()
    ax1.plot(range(F1z_length), F1z_data, label='F1z')
    ax1.set_xlabel('Index')
    ax1.set_ylabel('F1z')
    ax1.legend()
    canvas1.draw()

def plot_chart2():
    x = np.random.rand(100)
    y = np.random.rand(100)
    ax2.clear()
    ax2.scatter(x, y, s=displayrange_slider.get())
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    canvas2.draw()

def select_file():
    file_path = filedialog.askopenfilename(title="選取檔案", filetypes=[("Text files", "*.txt")])
    print("選取的檔案路徑:", file_path)
    if file_path:
        data = np.genfromtxt(file_path, delimiter=',')
        global F1z_data
        F1z_data = data[:, 2]  # 將 F1z 的值設定為 txt 檔案中的第三個數字
        plot_chart1()  # 重新繪製曲線圖

def output_parameters():#輸出
    start_idx = int(signstart_value.get())
    end_idx = int(signend_value.get())
    print(f"Start index: {start_idx}, End index: {end_idx}")

def update_value(label, slider):
    label.config(text=f"{slider.get():.2f}")  # 保留兩位小數

def update_timeaxis_slider_max():
    signstart_slider.config(to=F1z_length)
    signend_slider.config(to=F1z_length)

root = tk.Tk()
root.title("帶圖表的視窗")
root.geometry("1100x800")

# 創建功能列
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="選取檔案", command=select_file)
file_menu.add_separator()
file_menu.add_command(label="退出", command=root.quit)
menu_bar.add_cascade(label="檔案", menu=file_menu)

# 創建圖表1
frame1 = ttk.Frame(root, padding="3")
frame1.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
fig1 = Figure(figsize=(5, 4), dpi=100)
ax1 = fig1.add_subplot(111)
canvas1 = FigureCanvasTkAgg(fig1, master=frame1)
canvas1.draw()
canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 創建圖表2
frame2 = ttk.Frame(root, padding="3")
frame2.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)
fig2 = Figure(figsize=(5, 4), dpi=100)
ax2 = fig2.add_subplot(111)
canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
canvas2.draw()
canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 創建繪圖按鈕
plot_button1 = ttk.Button(root, text="繪製曲線圖", command=plot_chart1)
plot_button1.grid(row=2, column=0, sticky=tk.W+tk.E)

plot_button2 = ttk.Button(root, text="繪製散佈圖", command=plot_chart2)
plot_button2.grid(row=2, column=1, sticky=tk.W+tk.E)

# 創建框架以包含"切割“按鈕和滑桿
frame4 = ttk.Frame(root, padding="3")
frame4.grid(row=3, column=0, rowspan=5, sticky=tk.W+tk.E+tk.N+tk.S)

# 創建切割按鈕
cut_button = ttk.Button(frame4, text="切割")
cut_button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    #開始滑桿


signstart_slider= ttk.Scale(frame4, from_=1, to=F1z_length, orient=tk.HORIZONTAL, length=200)
signstart_slider.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
text_label = ttk.Label(frame4, text="訊號起點:")
text_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
signstart_label = ttk.Label(frame4, text=f"{ signstart_slider.get():.2f}")
signstart_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    #結束滑桿
signend_slider = ttk.Scale(frame4, from_=1, to=F1z_length, orient=tk.HORIZONTAL, length=200)
signend_slider.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
text_label = ttk.Label(frame4, text=f"訊號終點:")
text_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
signend_label = ttk.Label(frame4, text=f"{signend_slider.get():.2f}")
signend_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

update_timeaxis_slider_max()

# 創建框架以包含滑桿
frame3 = ttk.Frame(root, padding="3")
frame3.grid(row=3, column=1, rowspan=6, sticky=tk.W+tk.E+tk.N+tk.S)

# 創建滑桿標籤和滑桿
#時間軸滑桿
timeaxis_slider = ttk.Scale(frame3, from_=1, to=F1z_length, orient=tk.HORIZONTAL, length=200)
timeaxis_slider.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
text_label = ttk.Label(frame3, text=f"時間軸:")
text_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
timeaxis_label = ttk.Label(frame3, text=f"{timeaxis_slider.get():.2f}")
timeaxis_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


#範圍滑桿
displayrange_slider = ttk.Scale(frame3, from_=1, to=100, orient=tk.HORIZONTAL, length=200)
displayrange_slider.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
text_label = ttk.Label(frame3, text=f"顯示範圍:")
text_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
displayrange_label = ttk.Label(frame3, text=f" {displayrange_slider.get():.2f}")
displayrange_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# 創建 CutoffFreq 的滑桿
CutoffFreq_slider = ttk.Scale(frame3, from_=0, to=1.00, orient=tk.HORIZONTAL, length=200)
CutoffFreq_slider.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
text_label = ttk.Label(frame3, text=f"CutoffFreq:")
text_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
CutoffFreq_label = ttk.Label(frame3, text=f"{CutoffFreq_slider.get():.2f}")
CutoffFreq_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# 創建框架以包含滑桿
frame5 = ttk.Frame(root, padding="3")
frame5.grid(row=8, column=0, rowspan=6, sticky=tk.W+tk.E+tk.N+tk.S)

# 創建輸出按鈕
output_button = ttk.Button(frame5, text="輸出參數", command=output_parameters)
output_button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

# 綁定滑桿事件
signstart_slider.bind("<Motion>", lambda event: update_value(signstart_label, signstart_slider))
signend_slider.bind("<Motion>", lambda event: update_value(signend_label, signend_slider))
timeaxis_slider.bind("<Motion>", lambda event: update_value(timeaxis_label, timeaxis_slider))
displayrange_slider.bind("<Motion>", lambda event: update_value(displayrange_label, displayrange_slider))
CutoffFreq_slider.bind("<Motion>", lambda event: update_value(CutoffFreq_label, CutoffFreq_slider))

root.mainloop()
