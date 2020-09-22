import turtle
from random import randint as random_randint

global myTurtle
myTurtle = turtle.Turtle()

myTurtle.speed(0)
myTurtle.hideturtle()

global screen_largeur, screen_hauteur
screen_largeur = 800
screen_hauteur = 600

global fenetre_largeur, fenetre_hauteur
fenetre_largeur = 30
fenetre_hauteur = 30

global porte_largeur, porte_hauteur
porte_largeur = 30
porte_hauteur = random_randint(50, 59)

global balcon_hauteur
balcon_hauteur = 30

global etage_hauteur
etage_hauteur = 60

global immeuble_largeur
immeuble_largeur = 140

# set fenetre largeur hauteur

def set_fenetre_l(largeur):
    """
    Permet de modifier la largeur d'une fenetre

    Parametre : largeur
        largeur : un entier
    """
    try:
        fenetre_largeur = int(largeur)
    except:
        raise "ValueError, must be an integer"

def set_fenetre_h(hauteur):
    """
    Permet de modifier la hauteur d'une fenetre

    Parametre : hauteur
        hauteur : un entier
    """
    try:
        fenetre_hauteur = int(largeur)
    except:
        raise "ValueError, must be an integer"

# set porte largeur hauteur

def set_porte_l(largeur):
    """
    Permet de modifier la largeur d'une porte

    Parametre : largeur
        largeur : un entier
    """
    try:
        porte_largeur = int(largeur)
    except:
        raise "ValueError, must be an integer"

def set_porte_h(hauteur):
    """
    Permet de modifier la hauteur d'une porte

    Parametre : hauteur
        hauteur : un entier
    """
    try:
        porte_hauteur = int(largeur)
    except:
        raise "ValueError, must be an integer"

# set balcon hauteur

def set_balcon_h(hauteur):
    """
    Permet de modifier la hauteur d'une rembarde pour la porte-fenetre

    Parametre : hauteur
        hauteur : un entier
    """
    try:
        balcon_hauteur = int(largeur)
    except:
        raise "ValueError, must be an integer"

# set immeuble largeur

def set_immeuble_l(largeur):
    """
    Permet de modifier la largeur d'un immeuble

    Parametre : largeur
        largeur : un entier
    """
    try:
        immeuble_largeur = int(largeur)
    except:
        raise "ValueError, must be an integer"

# set etage hauteur

def set_etage_h(hauteur):
    """
    Permet de modifier la hauteur d'un etage/ du rez-de-chaussée

    Parametre : hauteur
        hauteur : un entier
    """
    try:
        etage_hauteur = int(hauteur)
    except:
        raise "ValueError, must be an integer"

# go to + angle

def __initiate_myTurtle__(posX, posY, color_line, color_plain):
    """
    déplace le curseur à la position posX posX et le pointe vers le coté droit de l'écran
    """
    myTurtle.end_fill()
    myTurtle.color(color_line, color_plain)
    myTurtle.penup()
    myTurtle.setheading(0)
    myTurtle.goto(posX, posY)
    myTurtle.pendown()
    myTurtle.begin_fill()


# draw fenetre

def draw_fenetre(posX, posY, color = "#8ab8c9"): # bleu gris clair
    """
    Dessine une fenetre à un endroit donné

    Arguments : posX, posY
        posX : position x (abscisse) du curseur
        posY : position y (ordonné) du curseur

    Variables Globales : fenetre_largeur, fenetre_hauteur
        fenetre_hauteur : hauteur de la fenetre à dessiner
            par defaut : 30
        fenetre_largeur : largeur de la fenetre à dessiner
            par defaut : 30
    Pour modifier ces Variables Globales
        set_fenetre_l(largeur)
        set_fenetre_h(hauteur)
    """
    __initiate_myTurtle__(posX, posY, "white", color)

    for i in range(2):
        myTurtle.forward(fenetre_largeur)
        myTurtle.left(90)
        myTurtle.forward(fenetre_hauteur)
        myTurtle.left(90)

# draw porte

def draw_porte(posX, posY, color = "brown"): # marron
    """
    Dessine une porte à un endroit donné

    Arguments : posX, posY
        posX : position x (abscisse) du curseur
        posY : position y (ordonné) du curseur

    Variables Globales : porte_largeur, porte_hauteur
        porte_hauteur : hauteur de la porte à dessiner
            par defaut : un nombre aléatoire entre 50 et 59
        fenetre_largeur : largeur de la fenetre à dessiner
            par defaut : 30
    Pour modifier ces Variables Globales
        set_porte_l(largeur)
        set_porte_h(hauteur)
    """

    __initiate_myTurtle__(posX, posY, "white", color)

    for i in range(2):
        myTurtle.forward(porte_largeur)
        myTurtle.left(90)
        myTurtle.forward(porte_hauteur)
        myTurtle.left(90)

# draw balcon

def draw_balcon(posX, posY, color = "black"): # noir
    """
    Dessine une rembarde pour une porte-fenetre à un endroit donné

    Arguments : posX, posY
        posX : position x (abscisse) du curseur
        posY : position y (ordonné) du curseur

    Variables Globales : balcon_hauteur, porte_largeur
        balcon_hauteur : hauteur du balcon à dessiner
            par defaut : 30
        porte_largeur : largeur de la porte-fenetre (qui est aussi la largeur du balcon)
            par defaut : 30
    Pour modifier ces Variables Globales
        set_balcon_h(hauteur)
        set_porte_l(largeur)
    """
    __initiate_myTurtle__(posX, posY, "white", color)

    largeur = (porte_largeur / 5) - 1

    for i in range(5):
        myTurtle.left(90)
        myTurtle.forward(30)
        myTurtle.right(90)
        myTurtle.forward(largeur)
        myTurtle.right(90)
        myTurtle.forward(30)
        myTurtle.left(90)
        myTurtle.forward(1)

# draw porte + balcon

def draw_porte_fenetre(posX, posY, color_porte = "#8ab8c9", color_balcon = "black"): # marron noir
    """
    Dessine porte avec une rembarde à un endroit donné

    Arguments : posX, posY
        posX : position x (abscisse) du curseur
        posY : position y (ordonné) du curseur

    Variables Globales : porte_largeur, porte_hauteur, balcon_hauteur
        porte_hauteur : hauteur de la porte à dessiner
            par defaut : un nombre aléatoire entre 50 et 59
        fenetre_largeur : largeur de la fenetre à dessiner
            par defaut : 30
        balcon_hauteur : hauteur du balcon à dessiner
            par defaut : 30
    Pour modifier ces Variables Globales
        set_porte_h(hauteur)
        set_fenetre_l(largeur)
        set_balcon_h(hauteur)
    """
    draw_porte(posX, posY, color_porte)
    draw_balcon(posX, posY, color_balcon)

# draw etage

def draw_etage(posX, posY, color = "orange"): # orange
    """
    Dessine un etage à un endroit donné

    Parametre : posX, posY
        posX : posX : position x (abscisse) du curseur
        posY : position y (ordonné) du curseur

    Variables Globales : etage_hauteur, immeuble_largeur
        etage_hauteur : la hauteur de l'étage à déssiner
            par defaut : 60
        immeuble_largeur : l'étage prend la largeur de l'immeuble
            par defaut : 140
        fenetre_hauteur : hauteur de la fenetre à dessiner
            par defaut : 30
        fenetre_largeur : largeur de la fenetre à dessiner
            par defaut : 30
        porte_hauteur : hauteur de la porte à dessiner
            par defaut : un nombre aléatoire entre 50 et 59
        balcon_hauteur : hauteur du balcon à dessiner
            par defaut : 30
    Pour modifier ces Variables Globales
        set_etage_h(hauteur)
        set_immeuble_l(largeur)
        set_fenetre_l(largeur)
        set_fenetre_h(hauteur)
        set_porte_h(hauteur)
        set_balcon_h(hauteur)
    """

    __initiate_myTurtle__(posX, posY, "white", color)

    for i in range(2):
        myTurtle.forward(immeuble_largeur)
        myTurtle.left(90)
        myTurtle.forward(etage_hauteur)
        myTurtle.left(90)

    list_posX = [posX + 15, posX + 55, posX + 95]

    for i_posX in list_posX:
        if random_randint(0,1) == 0:
            draw_fenetre(i_posX, posY + 20)
        else:
            draw_porte_fenetre(i_posX, posY)

# draw rez-de-chaussée

def draw_rez_chaussee(posX, posY, color = "orange"): # orange
    """
    Dessine un rez-de-chaussée à un endroit donné

    Parametre : posX, posY
        posX : posX : position x (abscisse) du curseur
        posY : position y (ordonné) du curseur

    Variables Globales : etage_hauteur, immeuble_largeur
        etage_hauteur : la hauteur du rez-de-chaussée (la même que la hauteur d'un étage)
            par defaut : 60
        immeuble_largeur : l'étage prend la largeur de l'immeuble
            par defaut : 140
        fenetre_hauteur : hauteur de la fenetre à dessiner
            par defaut : 30
        fenetre_largeur : largeur de la fenetre à dessiner
            par defaut : 30
        porte_hauteur : hauteur de la porte à dessiner
            par defaut : un nombre aléatoire entre 50 et 59
        balcon_hauteur : hauteur du balcon à dessiner
            par defaut : 30
    Pour modifier ces Variables Globales
        set_etage_h(hauteur)
        set_immeuble_l(largeur)
        set_fenetre_l(largeur)
        set_fenetre_h(hauteur)
        set_porte_h(hauteur)
        set_balcon_h(hauteur)
    """

    __initiate_myTurtle__(posX, posY, "white", color)

    for i in range(2):
        myTurtle.forward(immeuble_largeur)
        myTurtle.left(90)
        myTurtle.forward(etage_hauteur)
        myTurtle.left(90)

    list_posX = [posX + 15, posX + 55, posX + 95]

    is_porte = False
    for i in range(len(list_posX)):
        if is_porte == False:
            if i == 2:
                draw_porte(list_posX[i], posY)
                is_porte = True
            else:
                if random_randint(0,1) == 0:
                    draw_fenetre(list_posX[i], posY + 20)
                else:
                    draw_porte(list_posX[i], posY)
                    is_porte = True
        else:
            draw_fenetre(list_posX[i], posY + 20)

# draw toit

def draw_toit(posX, posY, color = "black"): # noire
    """
    Dessine un toit à un endroit donné

    Parametre : posX, posY
        posX : posX : position x (abscisse) du curseur
        posY : position y (ordonné) du curseur

    Variables Globales : immeuble_largeur
        immeuble_largeur : l'étage prend la largeur de l'immeuble
            par defaut : 140
    Pour modifier ces Variables Globales
        set_immeuble_l(largeur)
    """

    rebord = 5

    __initiate_myTurtle__(posX - rebord, posY, "white", color)

    largeur = rebord + immeuble_largeur + rebord

    millieu = posX - rebord + largeur / 2

    hauteur = posY + 15

    myTurtle.forward(largeur)

    myTurtle.goto(millieu, hauteur)

    myTurtle.goto(posX - rebord, posY)

# draw immeuble

def draw_immeuble(posX, posY, color_porte = "brown", color_balcon = "black", color_fenetre = "#8ab8c9", color_porte_fenetre_porte = "brown", color_porte_fenetre_fenetre = "black"):
    """
    Dessine un rez-de-chaussée à un endroit donné

    Parametre : posX, posY
        posX : posX : position x (abscisse) du curseur
        posY : position y (ordonné) du curseur

    Variables Globales : etage_hauteur, immeuble_largeur
        etage_hauteur : la hauteur du rez-de-chaussée (la même que la hauteur d'un étage)
            par defaut : 60
        immeuble_largeur : l'étage prend la largeur de l'immeuble
            par defaut : 140
        fenetre_hauteur : hauteur de la fenetre à dessiner
            par defaut : 30
        fenetre_largeur : largeur de la fenetre à dessiner
            par defaut : 30
        porte_hauteur : hauteur de la porte à dessiner
            par defaut : un nombre aléatoire entre 50 et 59
        balcon_hauteur : hauteur du balcon à dessiner
            par defaut : 30
    Pour modifier ces Variables Globales
        set_etage_h(hauteur)
        set_immeuble_l(largeur)
        set_fenetre_l(largeur)
        set_fenetre_h(hauteur)
        set_porte_h(hauteur)
        set_balcon_h(hauteur)
    """

    draw_rez_chaussee(posX, posY)

    nb_etage = random_randint(1,4)

    for i in range(nb_etage):
        posY += etage_hauteur
        draw_etage(posX, posY)

    if random_randint(0,1) == 0:
        posY += etage_hauteur
        draw_toit(posX, posY)

# draw road

def draw_road(posX, posY):
    """
    Dessine une rue à un endroit donné de façon aléatoire

    Parametre : posX, posY
        posX : posX : position x (abscisse) du curseur
        posY : position y (ordonné) du curseur

    Variables Globales : etage_hauteur, immeuble_largeur
        etage_hauteur : la hauteur du rez-de-chaussée (la même que la hauteur d'un étage)
            par defaut : 60
        immeuble_largeur : l'étage prend la largeur de l'immeuble
            par defaut : 140
        fenetre_hauteur : hauteur de la fenetre à dessiner
            par defaut : 30
        fenetre_largeur : largeur de la fenetre à dessiner
            par defaut : 30
        porte_hauteur : hauteur de la porte à dessiner
            par defaut : un nombre aléatoire entre 50 et 59
        balcon_hauteur : hauteur du balcon à dessiner
            par defaut : 30
    Pour modifier ces Variables Globales
        set_etage_h(hauteur)
        set_immeuble_l(largeur)
        set_fenetre_l(largeur)
        set_fenetre_h(hauteur)
        set_porte_h(hauteur)
        set_balcon_h(hauteur)
    """

    for i in range(4):
        draw_immeuble(posX, posY)
        posX = posX + immeuble_largeur + 30



# Pour tester si mes fonctions fonctionnent

if __name__ == "__main__":
    # initialise l'écran
    turtle.setup(800, 600)
    turtle.title("Draw a road")
    turtle.bgcolor("black")

    myTurtle.pencolor("white")

    draw_road(-300,-200)
    turtle.done()
