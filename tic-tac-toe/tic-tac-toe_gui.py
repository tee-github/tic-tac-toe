# tic tac toe game GUI

import tkinter
from tkinter import messagebox
import pygame
from pygame import mixer
window = tkinter.Tk()
window.title("Tic Tac Toe GUI")
window.geometry("700x700")

# background image
bg = tkinter.PhotoImage(file="pixelsunset.png")

background = tkinter.Label(window, image=bg)
background.place(x=0, y=0, relwidth=1, relheight=1)

pygame.mixer.init()

# background music
mixer.music.load("txtbluehourlofi.mp3")
mixer.music.play(-1)

symbols = ["X","O"]
turn = 0
game_round = 0
winner = False
x_score = 0
o_score = 0


def score_board():
    global x_score
    global o_score
    if winner == True and symbols[turn] == "X":
        x_score = (x_score + 1)
    elif winner == True and symbols[turn] == "O":
        o_score = (o_score + 1)

def disable_all_buttons():
    b1.config(state=tkinter.DISABLED)
    b2.config(state=tkinter.DISABLED)
    b3.config(state=tkinter.DISABLED)
    b4.config(state=tkinter.DISABLED)
    b5.config(state=tkinter.DISABLED)
    b6.config(state=tkinter.DISABLED)
    b7.config(state=tkinter.DISABLED)
    b8.config(state=tkinter.DISABLED)
    b9.config(state=tkinter.DISABLED)

def check_winner():
    global winner
    global symbols
    global turn
    # horizontal check
    if b1["text"] == symbols[turn] and b2["text"] == symbols[turn] and b3["text"] == symbols[turn]:
        b1.config(bg="#FDE68A")
        b2.config(bg="#FDE68A")
        b3.config(bg="#FDE68A")
        winner = True
        if symbols[turn] == "X":
            messagebox.showinfo("Winner", "Congratulations X is the winner!")
        else:
            messagebox.showinfo("Winner", "Congratulations O is the winner!")
        disable_all_buttons()
    if b4["text"] == symbols[turn] and b5["text"] == symbols[turn] and b6["text"] == symbols[turn]:
        b4.config(bg="#FDE68A")
        b5.config(bg="#FDE68A")
        b6.config(bg="#FDE68A")
        winner = True
        if symbols[turn] == "X":
            messagebox.showinfo("Winner", "Congratulations X is the winner!")
        else:
            messagebox.showinfo("Winner", "Congratulations O is the winner!")
        disable_all_buttons()
    if b7["text"] == symbols[turn] and b8["text"] == symbols[turn] and b9["text"] == symbols[turn]:
        b7.config(bg="#FDE68A")
        b8.config(bg="#FDE68A")
        b9.config(bg="#FDE68A")
        winner = True
        if symbols[turn] == "X":
            messagebox.showinfo("Winner", "Congratulations X is the winner!")
        else:
            messagebox.showinfo("Winner", "Congratulations O is the winner!")
        disable_all_buttons()

    # vertical check
    if b1["text"] == symbols[turn] and b4["text"] == symbols[turn] and b7["text"] == symbols[turn]:
        b1.config(bg="#FDE68A")
        b4.config(bg="#FDE68A")
        b7.config(bg="#FDE68A")
        winner = True
        if symbols[turn] == "X":
            messagebox.showinfo("Winner", "Congratulations X is the winner!")
        else:
            messagebox.showinfo("Winner", "Congratulations O is the winner!")
        disable_all_buttons()
    if b2["text"] == symbols[turn] and b5["text"] == symbols[turn] and b8["text"] == symbols[turn]:
        b2.config(bg="#FDE68A")
        b5.config(bg="#FDE68A")
        b8.config(bg="#FDE68A")
        winner = True
        if symbols[turn] == "X":
            messagebox.showinfo("Winner", "Congratulations X is the winner!")
        else:
            messagebox.showinfo("Winner", "Congratulations O is the winner!")
        disable_all_buttons()
    if b3["text"] == symbols[turn] and b6["text"] == symbols[turn] and b9["text"] == symbols[turn]:
        b3.config(bg="#FDE68A")
        b6.config(bg="#FDE68A")
        b9.config(bg="#FDE68A")
        winner = True
        if symbols[turn] == "X":
            messagebox.showinfo("Winner", "Congratulations X is the winner!")
        else:
            messagebox.showinfo("Winner", "Congratulations O is the winner!")
        disable_all_buttons()

    # diagonal check
    if b1["text"] == symbols[turn] and b5["text"] == symbols[turn] and b9["text"] == symbols[turn]:
        b1.config(bg="#FDE68A")
        b5.config(bg="#FDE68A")
        b9.config(bg="#FDE68A")
        winner = True
        if symbols[turn] == "X":
            messagebox.showinfo("Winner", "Congratulations X is the winner!")
        else:
            messagebox.showinfo("Winner", "Congratulations O is the winner!")
        disable_all_buttons()
    if b3["text"] == symbols[turn] and b5["text"] == symbols[turn] and b7["text"] == symbols[turn]:
        b3.config(bg="#FDE68A")
        b5.config(bg="#FDE68A")
        b7.config(bg="#FDE68A")
        winner = True
        if symbols[turn] == "X":
            messagebox.showinfo("Winner", "Congratulations X is the winner!")
        else:
            messagebox.showinfo("Winner", "Congratulations O is the winner!")
        disable_all_buttons()

    if game_round == 8 and winner == False:
        messagebox.showinfo("Game over", "We have a tie!")
        disable_all_buttons()

# button clicked function
def b_click(b):
    global game_round
    global turn
    if b["text"] == " ":
        b["text"] = symbols[turn]
        button_sound = mixer.Sound("buttonsoundeffect.mp3")
        button_sound.play()
        check_winner()
        score_board()
        turn = (turn + 1) %2
        game_round = game_round + 1
    elif ["text"] != " ":
        messagebox.showerror("Error", "That box has already been selected\n Please pick a valid box.")

# reset the game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global game_round
    global winner
    game_round = 0
    winner = False
    # build buttons
    b1 = tkinter.Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = tkinter.Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = tkinter.Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = tkinter.Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = tkinter.Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = tkinter.Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = tkinter.Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = tkinter.Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = tkinter.Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # grid buttons to the screen
    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)

    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)

    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)


    title = tkinter.Label(window, text="Tic Tac Toe", fg="#C79588", font=("fixedsys",35), bg="#3F79AE")
    note = tkinter.Label(window, text="*Note* Players take turn going first each game\n Click options --> reset to update the score board", fg="#5977AF", font=("fixedsys",11), bg="#A68E88")
    xlabel = tkinter.Label(window, text="X's Score:", font=("fixedsys",20), bg="#5977AF")
    olabel = tkinter.Label(window, text="O's Score:", font=("fixedsys",20), bg="#7B77B1")
    xscore = tkinter.Label(window, text=x_score, font=("fixedsys",20), bg="#5977AF")
    oscore = tkinter.Label(window, text=o_score, font=("fixedsys",20), bg="#7B77B1")

    title.config(anchor=tkinter.CENTER)
    title.grid(row=0, column=0, columnspan=3, pady=20)
    note.grid(row=4, column=0, columnspan=6)
    xlabel.grid(row=1, column=5)
    olabel.grid(row=2, column=5)
    xscore.grid(row=1, column=6)
    oscore.grid(row=2, column=6)


# dropdown menu
my_menu = tkinter.Menu(window)
window.config(menu=my_menu)

options_menu = tkinter.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

window.mainloop()







