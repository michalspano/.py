import tkinter
from random import *
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()

flowers = []
for f in range(3):
    flowers.append(tkinter.PhotoImage(file=f"flowers/flower{f + 1}.png"))


def create_flowers(r, s):
    c_width = int(canvas["width"])
    for i in range(r):
        x, y = randint(s, c_width - s), randint(s, c_width - s)
        random_flower = choice(flowers)
        if random_flower == flowers[0]:
            tag = "flower1"
        elif random_flower == flowers[1]:
            tag = "flower2"
        else:
            tag = "flower3"

        canvas.create_image(x, y, image=random_flower, tags=(i, tag))


def wilting():
    obj_count = len(canvas.find_all())

    if obj_count > 0:
        for ID in canvas.find_all():
            c = canvas.coords(ID)
            canvas.coords(ID, [c[0] + 1, c[1] - 1])
    canvas.after(500, wilting)


create_flowers(10, 50)
wilting()
canvas.mainloop()
