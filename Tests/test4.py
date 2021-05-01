import tkinter
canvas = tkinter.Canvas()
canvas.pack()

tk = canvas.create_rectangle(10, 10, 100, 100, fill="red")
print(not tk)
