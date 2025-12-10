import tkinter as tk
import time
import os
import random
from tkinter import messagebox
root=tk.Tk()
root.title("mışlıq komitesi")
root.geometry("400x800")
def arxaplandeyis():
    # random reng
    reng = ["yellow", "pink", "orange", "gray", "red", "white"]
    yeni_reng= random.choice(reng)
    
    root.configure(bg=yeni_reng)

    # mışlıq
    messagebox.showinfo("Uyarı", f"Arxa plan deyisdi: {yeni_reng}")

# Düymə
btn = tk.Button(root, text="Rengi misla", command=change_bg, font=("Arial", 14))
btn.pack(pady=40)

root.mainloop()
#bunu davam ettirin :D
