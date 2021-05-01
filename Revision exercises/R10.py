import tkinter
import time
canvas = tkinter.Canvas(height=300)
canvas.pack()


def draw_matches(r, sprite):
    width = r * sprite.width() + 10
    canvas["width"] = width
    for i in range(r):
        canvas.create_image(i * 50 + 20, 150, image=sprite)


def player_handler(switch):
    global player1, user_click
    if switch:
        player1 = False
    else:
        player1 = True
    user_click = 0
    with open("R10_save.txt", "a") as _break:
        _break.write("switch\n")
    label_value(player_var)


def click(event):
    global user_click
    x, y = event.x, event.y
    picked = canvas.find_overlapping(x, y, x, y)

    user_click += 1

    if user_click <= 3:
        if len(picked) > 0:
            picked = picked[0]
            with open("R10_save.txt", "a") as output:
                output.write(str(picked) + "\n")
            canvas.delete(picked)

    check(player1)


def check(switch):
    if len(canvas.find_all()) == 0:
        with open("R10_save.txt", "a") as player_lost:
            if switch:
                player_lost.write(f"Player1\n{user_range}")
                exit("Player 1 lost.")
            else:
                player_lost.write(f"Player2\n{user_range}")
                exit("Player 2 lost.")


def label_value(var):
    if player1:
        var.set("Player 1")
    else:
        var.set("Player 2")


def restart():
    with open("R10_save.txt", "r") as inputTextFile:
        data = [line.strip() for line in inputTextFile]

    if len(data) > 0:
        matches_count = int(data[-1])
        data = data[:-1]

        if matches_count == user_range:
            i = 0
            for j in range(len(data)):
                move = data[j]
                if move == "switch":
                    i += 1
                    if i % 2 == 0:
                        player_var.set("Player 1")
                    else:
                        player_var.set("Player 2")
                elif j == len(data) - 1:
                    canvas.create_text(int(canvas["width"]) / 2,
                                       int(canvas["height"]) / 2,
                                       text=f"{data[-1]} lost!",
                                       font="Arial 30 bold")
                else:
                    canvas.delete(move)
                time.sleep(1.5)
                canvas.update()
                file_reset = open("R10_save.txt", "w")
                file_reset.close()
    else:
        print("Empty txt. file.")


user_range = int(input("Number of matches: "))
user_click, player1 = int(), True
player_var = tkinter.StringVar()
label_value(player_var)
match_sprite = tkinter.PhotoImage(file="match.png")
draw_matches(user_range, match_sprite)

label1 = tkinter.Label(textvariable=player_var)
label1.pack()
player_button = tkinter.Button(text="Done", width=7, height=2,
                               command=lambda: player_handler(player1))
player_button.pack()
restart_button = tkinter.Button(text="Restart", width=7, height=2,
                                command=restart)
restart_button.pack()
canvas.bind("<Button-1>", click)
canvas.mainloop()
