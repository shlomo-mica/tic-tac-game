from tkinter import Tk, Canvas, Button, filedialog, PhotoImage, Label
# from PIL import Image, ImageTk, ImageDraw, ImageFont
import tkinter as tk
import numpy as np
from events_response import click


def exit(event):
    root.quit()


def onObjectClick(event):
    clicked_item = canvas.find_withtag('current')  # Finds the item that was clicked
    print("clicked", clicked_item[0])

    # print('Got object click', event.x, event.y)
    # print(event.widget.find_closest(event.x, event.y))
    canvas.itemconfig(addr[clicked_item[0]], text='✘')


def on_right_click(event):
    clicked_item = canvas.find_withtag('current')  # Finds the item that was clicked
    print("clicked", clicked_item[0])

    # print(('Got object click', event.x, event.y))
    # print(event.widget.find_closest(event.x, event.y))
    canvas.itemconfig(addr[clicked_item[0]], text='O')


#

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry(f"{h}x{w}+0+0")
root.title("COD_BOD")
root.configure(background='black')
root.bind("<Escape>", exit)

canvas = tk.Canvas(root, width=h, height=w, highlightthickness=0)
tictactoe_picture = PhotoImage(file=r"C:\Users\shlom\OneDrive\תמונות\Tic-tac-toe.png")
image = canvas.create_image(300, 300, image=tictactoe_picture, anchor='center')
# canvas.pack(anchor='center', expand=True)
canvas.grid(row=1, column=1)

array = np.full((1, 3, 3), "😊", dtype=None)
print("this33", array)

# Create a text label on the canvas
item2 = canvas.create_text(75, 100, text="😊", tags='obj1Id', font=("Times New Roman", 50, "bold"), fill="green",
                           anchor="w")
item3 = canvas.create_text(75, 300, text="😊", tags='obj2Id', font=("Times New Roman", 50, "bold"), fill="green",
                           anchor="w")
item4 = canvas.create_text(75, 500, text="😊", tags='obj3Id', font=("Times New Roman", 50, "bold"), fill="green",
                           anchor="w")

item5 = canvas.create_text(270, 100, text="😊", tags='obj3Id', font=("Times New Roman", 50, "bold"), fill="green",
                           anchor="w")
font = ("Times New Roman", 50, "bold")
# create image
item6 = click(270, 300, canvas, font)
item7 = click(270, 500, canvas, font)
item8 = click(450, 100, canvas, font)
item9 = click(450, 300, canvas, font)
item10 = click(450, 500, canvas, font)

addr = [0, 0, item2, item3, item4, item5, 6, 7, 8, 9, 10]

canvas.tag_bind(item2, '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item2, '<Button-3>', on_right_click)
canvas.tag_bind(item3, '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item3, '<Button-3>', on_right_click)
canvas.tag_bind(item4, '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item4, '<Button-3>', on_right_click)
canvas.tag_bind(item5, '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item5, '<Button-3>', on_right_click)
canvas.tag_bind(6, '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(6, '<Button-3>', on_right_click)
canvas.tag_bind(7, '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(7, '<Button-3>', on_right_click)
canvas.tag_bind(8, '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(8, '<Button-3>', on_right_click)
canvas.tag_bind(9, '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(9, '<Button-3>', on_right_click)
canvas.tag_bind(10, '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(10, '<Button-3>', on_right_click)


def label_clicked(*args):
    print("Label clicked")


root.mainloop()

window = Tk()
window.title("Tic-tac-game")
# window.config(padx=100, pady=50, bg='gray')
label1 = Label(text="✘", padx=1, pady=0)
label1.pack(anchor="center")

window.mainloop()
# item7.create_image(font=("Times New Roman", 50, "bold"))

# def on_right_click(event):
#     print("Right click!")
#
# root = tk.Tk()
# frame = tk.Frame(root, width=100, height=100)
# frame.bind("<Button-3>", on_right_click)
# frame.pack()


# Bind the click event to the label
# label1.bind("<Button-1>", label_clicked)
# anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = ..
# label1.grid(column=0, row=0)
# label2 = Label(text="✘")
# label2.grid(column=0, row=1)
# label3 = Label(text="✘")
# label3.grid(column=0, row=0)
# label = tk.Label(window, text="Hello World!")
# def label_clicked(*args):
#     print("Label clicked")


# Bind the click event to the label
# label1.bind("<Button-1>", label_clicked)

# canvas = Canvas(window, height=600, width=600, highlightthickness=0, bg='white')
# tictactoe_picture = PhotoImage(file=r"C:\Users\shlom\OneDrive\תמונות\Tic-tac-toe.png")
# # image = canvas.create_image(300, 300, image=tictactoe_picture, anchor='center')
# canvas.pack(anchor='center', expand=True)
