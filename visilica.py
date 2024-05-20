from tkinter import *

root = Tk()
root.title('Виселица')
canvas = Canvas(root, width=600, height=600)
canvas.pack()

def but():
    y = 0
    while y < 600:
        x = 0
        while x < 600:
            x = 0
            while x < 600:
                canvas.create_rectangle(x, y, x+33, y+33, fill="white", outline="blue")
x = +33
y = +33

fag - ''''''
root.mainloop()