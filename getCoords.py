from tkinter import *
from math import *
import json

grille = []
for i in range(44):
    ligne=[0 for j in range(27)]
    grille.append(ligne)


def coord(clic):#scenario du jeu par etape

    # on récupère dans la boite  ( ou variable) "x_cliquer" l' abscisse où a cliqué l'utilisateur, de même pour l'ordonnée:
    x=clic.x
    y=clic.y
    print("coord x et y: ", end="")
    print(x, end="")
    print(",", end="")
    print(y)

    x1 = floor(x/30)
    y1 = floor(y/30)
    
    mon_cadre.create_line(x1*30,y1*30,(x1+1)*30,(y1+1)*30,width=2,fill='blue')
    mon_cadre.create_line((x1+1)*30,y1*30,x1*30,(y1+1)*30,width=2,fill='blue')
    
    grille[x1][y1] = 1


def write_json(clic):
    #user_scrapped_info = {'username': username, 'real_followers': types['real_followers'] / number_followers, 'cities': cities}
    #string = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    grilleMap = {'grille': grille}
    string = json.dumps(grilleMap)
    file = open('./Grid/grid.json', 'w')
    file.write(string)
    file.write('\n')
    file.close()


def read_json(filename):
    with open(filename) as json_file:
        json_data = json.load(json_file)
        return json_data['grille']


def display_map(terrain):
    for x1 in range(44):
        for y1 in range(27):
            if terrain[x1][y1] == 1:
                mon_cadre.create_line(x1*30,y1*30,(x1+1)*30,(y1+1)*30,width=2,fill='blue')
                mon_cadre.create_line((x1+1)*30,y1*30,x1*30,(y1+1)*30,width=2,fill='blue')



if __name__ == "__main__":
    # Création de la fenêtre principale :
    fen1 = Tk()
    fen1.resizable(width=False, height=False)


    # création d'un canevas (appelé "mon_cadre") à gauche de la fenêtre, où l'on va pouvoir dessiner  :

    mon_cadre = Canvas(fen1,bg='white',height=810,width=1320)
    mon_cadre.bind("<Button-1>", coord)
    mon_cadre.bind("<Button-2>", write_json)
    mon_cadre.pack()

    imageFixe=PhotoImage(file='grilleMap.gif')
    mon_cadre.create_image(0,0,image=imageFixe, anchor=NW)

    fen1.mainloop()
