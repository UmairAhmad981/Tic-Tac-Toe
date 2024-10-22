import os
import sys
import tkinter as tk
from tkinter import PhotoImage, Toplevel

def resource_path(relative_path): #To Add App Logo Bundled with exe and can retrive from it
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# 0 - X
# 1 - O
# 2 - Empty
active = True
gamestatus = [2] * 9
allwinpos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]
activeplayer = 0
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(width=False,height=False)
icon_path = resource_path('tic-tac-toe_1191134.png')
icon = PhotoImage(file=icon_path)
root.iconphoto(True, icon)

lst2 = [tk.StringVar() for _ in range(9)]
def reset(): #Reset Function to reset after win or tie
    global gamestatus, activeplayer, active
    gamestatus = [2] * 9
    activeplayer = 0
    active = True
    for i in range(9):
        lst2[i].set('')

def check_winner(): #To Check if the game is finished or not
    global gamestatus,active
    for pos in allwinpos:
        if gamestatus[pos[0]] == gamestatus[pos[1]] == gamestatus[pos[2]] != 2:
            active = False
            return True
    if 2 not in gamestatus:
        active = False
        return "Tie"
    return False

def Tap(press): #After Pressing Function
    global active,activeplayer
    if gamestatus[press] == 2: #Check if the Field is Empty then only fill with X or O
        gamestatus[press] = activeplayer
        lst2[press].set('X' if activeplayer == 0 else 'O')
        winner = check_winner() #check is game is finished or not
        if winner != False:
            declareScreen = Toplevel(root) #If game is finished create a new window 

            declareScreen.attributes("-topmost", True)
            declareScreen.grab_set()#make the declareScreen as priority Screen and disable Root Screen Activity

            root_x = root.winfo_x() #get X,Y Coordinate of root
            root_y = root.winfo_y()
            
            root_width = root.winfo_width() #get Width and Height of root
            root_height = root.winfo_height()


            declareScreen_width = 150
            declareScreen_height = 70

            x = root_x + (root_width // 2) - (declareScreen_width // 2) #adjusting this window to the center of the root window
            y = root_y + (root_height // 2) - (declareScreen_height // 2)
            declareScreen.geometry(f"{declareScreen_width}x{declareScreen_height}+{x}+{y}")
            def resetfn():
                reset()
                declareScreen.destroy() #exiting the window after reset
            resetBtn=tk.Button(declareScreen,text="Reset Game",command=resetfn)
            if winner == True:
                show = tk.Label(declareScreen,text=f"Player {activeplayer} wins!")
            elif winner == "Tie":
                show = tk.Label(declareScreen,text="It's a tie!")
            show.pack()
            resetBtn.pack()
        activeplayer = 1 if activeplayer == 0 else 0

lst = []
a = 0
for i in range(3): #making 3x3 button 
    for j in range(3):
        btn = tk.Button(root, textvariable=lst2[a],pady=0,padx=0, height=1, width=3, command=lambda val=a: Tap(val),font=("",50,'bold'))
        btn.grid(row=i, column=j)
        lst.append(btn)
        a += 1

root.mainloop()
