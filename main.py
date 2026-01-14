import random
from turtle import Turtle, Screen
# lista para armazenar a cor de cada uma das tartarugas
cores = ["red","orange","yellow","green","blue","purple"]
#lista onde as instâncias da classe Turtle ficarão
tartarugas = []
#variável para usar no while
corrida = False
#criando o objeto da classe Screen
screen = Screen()
screen.setup(width=500,height=400)
#For para criar 6 tartarugas, mudando a forma delas para de um tartaruga, o 'default' é uma seta
#Colocando ela no começo da tela e empilhando uma na outra
#Fazendo que ao andarem não deixem um rastro(penup)
#Mudando a cor de cada tartaruga conforme lista: cores[0], cores[1] ...
#Adicionando cada objeto na lista de tartarugas
for i in range(0,6):
    nova_tartaruga = Turtle(shape="turtle")
    nova_tartaruga.teleport(x=-238, y=i * 20)
    nova_tartaruga.penup()
    nova_tartaruga.color(cores[i])
    tartarugas.append(nova_tartaruga)

#cria um campo onde na tela da corrida para fazer a aposta(cor da tartaruga) no qual tem que ser em inglês
aposta = screen.textinput(title="faça suas apostas",prompt="qual tartaruga irá vencer?")
#se aposta existir a corrida começará
if aposta:
    corrida = True

#enquanto a corrida for True ela vai fazer o seguinte:
while corrida:
    #for para passar de tartaruga em tartaruga
    #condição de vitória: caso a coordena 'x' for maior que 225(fim da tela), a tartaruga ganha
    for tartaruga in tartarugas:
        if tartaruga.xcor() < 225:
            #faz com que a tartaruga ande uma distância aleatória de 0 a 10 unidades
            distancia_aleatoria = random.randint(0,10)
            tartaruga.forward(distancia_aleatoria)
        else:
            #checa se a tartaruga ganhadora é da cor que você apostou
            #.color() para pegar a cor e o index[0], por conta de retornar uma tupla de dois valores no qual só preciso do primeiro
            if tartaruga.color()[0] == aposta:
                print(f"Você venceu, a tartaruga {tartaruga.color()[0]} é a ganhadora")
            else:
                print(f"Você perdeu, a tartaruga {tartaruga.color()[0]} é a ganhadora")
            #muda a corrida para false e sai do loop for
            corrida = False
            break
#sair da tela ao clickar nela
screen.exitonclick()