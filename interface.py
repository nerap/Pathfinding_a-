from tkinter import *
import random
import time

def color_case(x, y, color):
    mon_cadre.create_rectangle(x*30+1,y*30+1,(x+1)*30-1,(y+1)*30-1,fill=color,width=1)

def clic(event):
    update()
    
def update():
    color_case(random.randrange(0, 44), random.randrange(0, 27), "red")
    fen1.after(1, update)

def main():
    fen1.resizable(width=False, height=False)
    
    # création d'un canevas (appelé "mon_cadre") à gauche de la fenêtre, où l'on va pouvoir dessiner  :
    
    imageFixe=PhotoImage(file='grilleMap.gif')
    mon_cadre.create_image(0,0,image=imageFixe, anchor=NW)
    
    mon_cadre.bind("<Button-1>", clic)
    mon_cadre.pack()
    fen1.mainloop()
    
fen1 = Tk()
mon_cadre = Canvas(fen1,bg='white',height=810,width=1320)
main()