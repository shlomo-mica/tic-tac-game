class click:

    def __init__(self, x, y, canvas, font):
        self.canvas = canvas
        self.can = canvas
        self.x_axis = x
        self.y_axis = y
        self.text = "image"
        self.tags = 'obj3Id',
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
        print(self.y_axis, self.y_axis)
        # can.create_text(x, y, text=text, tags='obj3Id', font=("Times New Roman", 50, "bold"),
        #                 fill="black", anchor="w")
        number = self.canvas.create_text(self.x_axis, self.y_axis, text='😊', anchor='w', font=font, fill='green')
        return number
