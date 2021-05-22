import tkinter
import math
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()


def robot(x, y):
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5,
                       fill="red", outline="", tags="robot")


def entry_action():
    action = entry1.get()
    perform_action(action)


def perform_action(ac):
    ac.split(",")

    if len(ac) < 2:
        action = ac.split()

    else:
        action = ac.split(",")
        action = [acs.split() for acs in action]

    j = 0
    while j < len(action):
        identifier = action[j][0]
        value = action[j][1]

        if identifier == "right":
            right(value)

        elif identifier == "left":
            left(value)

        elif identifier == "line":
            add_line(value)

        elif identifier == "pencolor":
            pen_color(value)

        elif identifier == "penwidth":
            pen_width(value)

        elif identifier == "repeat":
            index = action.index(action[j]) + 1
            repeated_values = []
            info = value.split(";")
            n, end = int(info[0]), int(info[1])
            for i in range(n):
                for k in range(end):
                    repeated_values.append(action[j + k + 1])
            for r in range(len(repeated_values)):
                action.insert(index + r, repeated_values[r])
        j += 1


def right(par):
    global angle_deg
    angle_deg -= int(par)


def left(par):
    global angle_deg
    angle_deg += int(par)


def pen_color(par):
    global _pen_color
    _pen_color = par


def pen_width(par):
    global _pen_width
    _pen_width = int(par)


def load_data():
    data = str()
    with open("R20_sequence.txt") as sequence:
        for seq in sequence:
            data += seq

    data = data.replace("\n", ", ")
    perform_action(data)


def add_line(length):
    global coords
    angle_rad = round((angle_deg / 180) * math.pi, 3)
    new_x = coords[0] + (math.sin(angle_rad) * int(length))
    new_y = coords[1] + (math.cos(angle_rad) * int(length))
    coords.append(new_x), coords.append(new_y)
    canvas.create_line(coords, fill=_pen_color, width=_pen_width,
                       tags="t_line")
    coords = coords[2:]


def export():
    canvas.delete("robot")
    from datetime import datetime
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    canvas.postscript(file=f"export{time}.eps")
    exit(f"Your image was saved at/ export{time}.eps")


coords = [int(canvas["height"]) / 2] * 2
angle_deg, _pen_width, _pen_color = 180, 1, "blue"
robot(200, 200)
load_button = tkinter.Button(text="Load", width=5, height=2,
                             command=load_data)
load_button.pack()
entry1 = tkinter.Entry(bd=5)
entry1.pack()
entry_button = tkinter.Button(text="Done", width=5, height=2,
                              command=entry_action)
entry_button.pack()
export_button = tkinter.Button(text="Export", command=export)
export_button.pack()
canvas.mainloop()
