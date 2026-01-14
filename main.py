import random
from turtle import Turtle, Screen
colors = ["red","orange","yellow","green","blue","purple"]
tartarugas = []
corrida = False
screen = Screen()
for i in range(0,6):
    nova_tartaruga = Turtle(shape="turtle")
    nova_tartaruga.teleport(x=-238, y=0 + i * 20)
    nova_tartaruga.penup()
    nova_tartaruga.color(colors[i])
    tartarugas.append(nova_tartaruga)

screen.setup(width=500,height=400)
aposta = screen.textinput(title="faça suas apostas",prompt="qual tartaruga irá vencer?")

if aposta:
    corrida = True

while corrida:

    for tartaruga in tartarugas:
        if tartaruga.xcor() < 225:
            distancia_aleatoria = random.randint(0,10)
            tartaruga.forward(distancia_aleatoria)
        else:
            if tartaruga.color()[0] == aposta:
                print(f"Você venceu, a tartaruga {tartaruga.color()[0]} é a ganhadora")
            else:
                print(f"Você perdeu, a tartaruga {tartaruga.color()[0]} é a ganhadora")
            corrida = False
            break

screen.exitonclick()