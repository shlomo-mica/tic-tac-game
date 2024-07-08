from tkinter import Tk, Button, filedialog, PhotoImage, Label
# from PIL import Image, ImageTk, ImageDraw, ImageFont
import tkinter as tk
import numpy as np
from events_response import click, array_calculate, canvas_return


def Winner_Test(f):
    # Check if all values in rows and columns are equal---> boolean
    first_col = np.all(my_array[:, 0] == my_array[0, 0])
    second_col = np.all(my_array[:, 1] == my_array[1, 1])
    third_col = np.all(my_array[:, 2] == my_array[2, 2])

    first_row = np.all(my_array[0, :] == my_array[0, 0])
    second_row = np.all(my_array[1, :] == my_array[1, 1])
    third_row = np.all(my_array[2, :] == my_array[2, 2])
    if first_row or second_row or third_row or first_col or second_col or third_col:
        print("win")
        return "is the Winner"
    else:
        print("lose")
        return 'No winner'


def onObjectClick(y):
    clicked_item = canvas.find_withtag('current')  # Finds the item that was clicked
    print("clicked", clicked_item[0])
    solutions = np.argwhere(my_array == clicked_item[0])
    print(solutions[0][0], solutions[0][1])
    play_righy = array_calculate(clicked_item[0], solutions[0][0], solutions[0][1], my_array)
    play_righy.change_x_array()
    canvas.itemconfig(clicked_item, text='✘')  # addr[clicked_item[0]]
    Winner_Test(f=2)
    print(my_array)


def on_right_click(x):
    clicked_item = canvas.find_withtag('current')  # Finds the item that was clicked
    print("clicked", clicked_item)  # [0] ignore touple just the first value
    canvas.itemconfig(clicked_item, text='𝑶')
    solutions = np.argwhere(my_array == clicked_item[0])
    print(solutions[0][0], solutions[0][1])
    play_left = array_calculate(clicked_item[0], solutions[0][0], solutions[0][1], my_array)
    play_left.change_y_array()
    Winner_Test(f=2)
    print(my_array)


def clear():
    canvas.destroy()
    canvas_return()


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
canvas.grid(row=4, column=4)

# CANVAS RETURN OBJECT
new_game_restart = canvas_return()

my_button = tk.Button(root, text="Click Me", bg='blue', command=clear)  # lambda: print("Button clicked!"))
my_button.grid(row=4, column=4)

# canvas.pack(anchor='center', expand=True)


font = ("Times New Roman", 50, "bold")
# create images


item2 = click(75, 100, canvas, font, tag=2)
item5 = click(75, 300, canvas, font, tag=3)
item8 = click(75, 500, canvas, font, tag=4)
item3 = click(270, 100, canvas, font, tag=5)
item6 = click(270, 300, canvas, font, 6)
item9 = click(270, 500, canvas, font, 7)
item4 = click(450, 100, canvas, font, 8)
item7 = click(450, 300, canvas, font, 9)
item10 = click(450, 500, canvas, font, 10)
addr = ([item2.tags, item3.tags
    , item4.tags, item5.tags, item6.tags, item7.tags, item8.tags, item9.tags, item10.tags])

my_array = np.array(addr).reshape(3, 3)

# binding events
canvas.tag_bind(item2.tags[0], '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item2.tags[0], '<Button-3>', on_right_click)

canvas.tag_bind(item3.tags[0], '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item3.tags[0], '<Button-3>', on_right_click)
canvas.tag_bind(item4.tags[0], '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item4.tags[0], '<Button-3>', on_right_click)
canvas.tag_bind(item5.tags[0], '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item5.tags[0], '<Button-3>', on_right_click)
canvas.tag_bind(item6.tags[0], '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item6.tags[0], '<Button-3>', on_right_click)
canvas.tag_bind(item7.tags[0], '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item7.tags[0], '<Button-3>', on_right_click)
canvas.tag_bind(item8.tags[0], '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item8.tags[0], '<Button-3>', on_right_click)
canvas.tag_bind(item9.tags[0], '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item9.tags[0], '<Button-3>', on_right_click)
canvas.tag_bind(item10.tags[0], '<ButtonPress-1>', onObjectClick)
canvas.tag_bind(item10.tags[0], '<Button-3>', on_right_click)


def label_clicked(*args):
    print("Label clicked")


root.mainloop()

