from tkinter import PhotoImage
import tkinter as tk


class click:

    def __init__(self, x, y, canvas, font, tag):
        self.canvas = canvas
        self.can = canvas
        self.x_axis = x
        self.y_axis = y
        self.text = "image"
        self.tags = tag,
        self.font = "Times New Roman"
        self.size = 50
        self.bold = "green"
        self.fill = "red"
        self.anchor = "w"
        self.font = font
        self.create_image()

    def print_test(self):
        print("key1 is on")

    def create_image(self, font=("Times New Roman", 50, "bold")):
        self.canvas.create_text(self.x_axis, self.y_axis, text=self.tags, anchor='w', font=font, fill='green')
        return self.tags


class array_calculate:

    def __init__(self, item_number, arr_x_loc, arr_y_loc, my_array):
        self.item = item_number
        self.x_loc = arr_x_loc
        self.y_loc = arr_y_loc
        self.array = my_array

    def change_x_array(self):
        self.array[self.x_loc, self.y_loc] = 100

    def change_y_array(self):
        self.array[self.x_loc, self.y_loc] = 99

    def playagain(self):
        print(33)


# https://stackoverflow.com/questions/51856163/how-can-i-clear-or-overwrite-a-tkinter-canvas
class canvas_return:
    def __init__(self):
        root = tk.Tk()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(1)
        root.geometry(f"{h}x{w}+0+0")

        canvas = tk.Canvas(root, width=h, height=w, highlightthickness=0)
        tictactoe_picture = PhotoImage(file=r"C:\Users\shlom\OneDrive\תמונות\Tic-tac-toe.png")
        image = canvas.create_image(300, 300, image=tictactoe_picture, anchor='center')
        canvas.grid(row=4, column=4)
        my_button = tk.Button(root, text="Click Me", bg='blue', command='start_again')  # lambda: print("Button clicked!"))
        my_button.grid(row=4, column=4)

    # def clearPlotPage(self):
    #     self.canvas.destroy()
    #     self.canvas = None
    #     self.plot()
    #     print("Plot Page has been cleared")