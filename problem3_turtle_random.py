import random
N=input("entrer un entier entre 0 et 9:")
int(N)
print(N)
#chaque forme est choisie au hazard par le random entre carre cercle et triangle random
forme=random.choice(["carre","cercle","triangle"])

import turtle
#creer une fonction pour chaque forme
def carre():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
def cercle():
    turtle.circle(25)

def triangle():
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    
if forme=="carre":
    for i in range(N):
        carre()
if forme=="Triangle":
    for i in range(N):
        triangle()
if forme=="cercle":
    for i in range(N):
        cercle()

    