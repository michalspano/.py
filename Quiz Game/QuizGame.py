import tkinter
from random import *
import tkinter.colorchooser

window = tkinter.Tk()
window.title("Welcome!")
default_color = "skyblue"
canvas = tkinter.Canvas(width=300, height=300, bg=default_color)
quiz1 = tkinter.Canvas(width=400, height=400, bg=default_color)
canvas.pack()

data1, data2 = list(), list()
score_count, question_index = int(), int()
language_switch = tkinter.IntVar()


def load_data():
    global data1, data2
    with open("data.txt", "r") as inputTextFile:
        data = [line.strip().split(";") for line in inputTextFile]
    data1 = [data[i][0] for i in range(len(data))]
    data2 = [data[i][1] for i in range(len(data1))]


load_data()


def language_options():
    global data1, data2
    if language_switch.get() == 1:
        print("English")
        dismiss_main_menu_elements()
    elif language_switch.get() == 2:
        dismiss_main_menu_elements()
        data1, data2 = data2, data1
        print("Slovak")
    else:
        print("No option was selected")
        restart()


def pick_color():
    c = tkinter.colorchooser.askcolor()
    color = c[1]
    if color != None:
        canvas["bg"] = color
    label1["bg"], radiobutton1["bg"], radiobutton2["bg"], button1["highlightbackground"] = \
        color, color, color, color
    quiz1["bg"] = color


def test_type1():
    language_options()
    dismiss_main_menu_elements()
    quiz1.pack()

    listbox1.pack()
    shuffled_data = data2[:]
    shuffle(shuffled_data)

    for element in shuffled_data:
        listbox1.insert("end", element)

    button2 = tkinter.Button(text="Close", command=restart)
    button2.pack()
    question_pick()


def question_pick():
    global data1, data2, question_index
    quiz1.delete("word_text")
    if len(data1) > 0:
        question_index = randrange(0, len(data1))
        quiz1.create_text(200, 200, text=data1[question_index], font="Arial 50",
                          tags="word_text")
    else:
        print(f"YOU WON {score_count} / 10")


def correct_result(event):
    global score_count
    selected = listbox1.curselection()
    if listbox1.get(selected) == data2[question_index]:
        score_count += 1
        listbox1.delete(selected)
        data1.pop(question_index), data2.pop(question_index)
    question_pick()


def main_menu_assets():
    global tx
    canvas.delete("main_label")
    tx += 3

    if tx >= int(canvas["width"]) + 100:
        tx = - 100
    canvas.create_text(tx, int(canvas["height"]) / 2, text="Test your skills!",
                       font="Arial 25 bold", tags="main_label")
    canvas.after(25, main_menu_assets)


def dismiss_main_menu_elements():
    canvas.destroy()
    label1.destroy(), radiobutton1.destroy(), radiobutton2.destroy(), button1.destroy()


def restart():
    import sys
    import os
    os.execv(sys.executable, ['python'] + sys.argv)


tx = 150
main_menu_assets()
menu = tkinter.Menu(window)
window.config(menu=menu)

file_menu = tkinter.Menu(menu, tearoff=0)
file_menu.add_command(label="Quiz 1", command=test_type1)

menu.add_cascade(label="Quizzes", menu=file_menu)

label1 = tkinter.Label(text="Choose a language to translate to: ",
                       bg=default_color)
label1.pack()
radiobutton1 = tkinter.Radiobutton(text="English", variable=language_switch,
                                   value=1, bg=default_color)
radiobutton1.pack(anchor="center")
radiobutton2 = tkinter.Radiobutton(text="Slovak", variable=language_switch,
                                   value=2, bg=default_color)
radiobutton2.pack(anchor="center")

button1 = tkinter.Button(text="Settings", command=pick_color,
                         highlightbackground=default_color)
button1.pack(anchor="center")
listbox1 = tkinter.Listbox()
listbox1.bind("<Double-Button-1>", correct_result)
window.mainloop()
