#!/usr/bin/env python3

import tkinter as tk

def close():
    window.destroy()

window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

button = tk.Button(window, text="Закрыть", font=('Helvetica', 10, 'bold'), command=close)
button.place(x=330, y=400, width=90, height=30)

window.mainloop()
