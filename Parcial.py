import turtle
import sys
import tkinter as tk
from tkinter import *
root=Tk()
pepe = turtle.Turtle()
pepe.hideturtle()
pepe.shape("turtle")
pepe.pu()
pepe.goto(-45,100)
pepe.pd()
bucles=" "
sides=" "
color = str
opcion=("")
testing=("")
xx=[]
yy=[]
desplazamientox=0
desplazamientoy=0
test1=0
test2=0
xpegar=[]
ypegar=[]
diccionario={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---",
"k":"-.-","l":".-..","m":"--","n":"-.","ñ":"--.--","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-",
"v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","á":".--.-","é":"..-..","ó":"---.","0":"-----","1":".----",
"2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",
"(":"-.--.","+":".-.-.","¿":"..-.-",",":"--..--",")":"-.--.-","-":"-....-","¡":"--...-","?":"..--..",
"&":".-...","_":"..--.-","'":".----.",":":"---...","!":"-.-.--",";":"-.-.-.","$":"...-..-","/":"-..-.","=":"-...-",
" ":"/","@":".--.-."}


def reset():
  global bucles, sides, opcion, testing, desplazamientox, desplazamientoy, test1, test2, xx, yy, xpegar, ypegar
  bucles=" "
  sides=" "
  opcion=("")
  testing=("")
  xx=[]
  yy=[]
  desplazamientox=0
  desplazamientoy=0
  test1=0
  test2=0
  xpegar=[]
  ypegar=[]

def config():
  global color
  color = str(turtle.textinput('Color', 'Ingrese el nombre del color en inglés'))
  reset()
  pepe.hideturtle()
  pepe.shape("turtle")
  pepe.pu()
  pepe.goto(-45,100)
  pepe.pencolor(color)
  pepe.pd()

  
def lados():
  global sides
  global bucles
  sides = int(turtle.numinput("Lados ","Cuantos lados tendrá tu poligono: ", 0, 3, 10))
  pepe.clear()
  pepe.pd()
  bucles=sides

def regular():
  global opcion
  opcion="regular"
  for i in range(bucles):
    pepe.pd()
    pepe.forward(70)
    pepe.right(360/sides)
    pepe.pu()

def deshacer():
  global bucles
  if opcion == 'regular':
    bucles=bucles-1
    pepe.clear()
    regular()
  if opcion == 'irregular':
    bucles = len(xx)
    del(xx[bucles-1])
    del(yy[bucles-1])
    pepe.clear()
    for i in range (len(xx)):
      pepe.goto((xx[i]+desplazamientox),(yy[i]+desplazamientoy))
      pepe.pd()


def copiar():          
  global testing
  testing="copiado"

def pegar():                  
  if testing=="copiado":
    if opcion=="regular":    
      pepe.pu()
      turtle.onscreenclick(click_pegar_regular)
    if opcion=="irregular":
      turtle.onscreenclick(click_pegar_irregular)

  else:
    print("No ha copiado nada")
  

def borrar():
  reset()
  pepe.clear()

def salir():

    sys.exit()
    
def click_pegar_regular(x,y):                                    
    xpegar.append(int(x))
    ypegar.append(int(y))
    pepe.pu()
    pepe.goto(x,y)
    regular()

def click_pegar_irregular(x,y):                                 
  global desplazamientox,desplazamientoy,test1,test2
  xpegar.append(int(x))
  ypegar.append(int(y))
  pepe.pu()
  pepe.goto(x,y)
  desplazamientox=(xpegar[test1]-xx[0])
  desplazamientoy=(ypegar[test2]-yy[0])
  for i in range (len(xx)):
    #pepe.pu()
    pepe.goto((xx[i]+desplazamientox),(yy[i]+desplazamientoy))
    #pepe.dot(10, "black")
    pepe.pd()
  test1+=1
  test2+=1

def mouse (x, y):
  xx.append(int(x))
  yy.append(int(y))
  pepe.clear
  pepe.goto(x,y)
  pepe.pd()
  print(xx,yy)


def dibujo_libre():
  global opcion
  opcion="irregular"
  pepe.clear()
  pepe.pu()
  turtle.onscreenclick(mouse)

def ASCII_morse():
    reset()
    dibujo = []
    turtle.pencolor(color)
    turtle.clear()
    turtle.hideturtle()
    turtle.pu()
    turtle.goto(-100,50)
    turtle.right(90)

    frase=str(turtle.textinput('Morse', 'Ingrese la frase a tradducir: '))
    frase=frase.lower()
    #turtle.write(frase,false,"right",(arial,30, "italic"))
    lista_letras=list(str(frase))
    lista_traducida=[]
    #turtle.write(lista_letras,false,"right",(arial,30, "italic"))
    for i in lista_letras:
        letra=i
        lista_traducida.append(diccionario[letra])
        for i in diccionario[letra]:
          dibujo.append(i)
        dibujo.append('/')
    #print(lista_traducida)
    #print(dibujo)
    lista_traducida=" ".join(lista_traducida)
    turtle.speed(2)

    def punto():
      turtle.dot(4)
      turtle.pd()
      turtle.pu()
      turtle.forward(7)
    
    def linea():
      turtle.pensize(1)
      turtle.pd()
      turtle.forward(7)
      turtle.pu()
      turtle.forward(7)

    def espacio():
      turtle.forward(7)       

    for i in dibujo:
      if i == '.':
        punto()
      elif i == '-':
        linea()
      elif i == '/':
        espacio()

'''def morse_ASCII():
    reset()
    color = str(turtle.textinput('Color', 'Ingrese el nombre del color en inglés'))
    turtle.pencolor(color)
    pepe.clear()
    pepe.shape("turtle")
    pepe.hideturtle()
    pepe.pu()
    pepe.goto(-45,100)
    pepe.pd()
    morse=str(turtle.textinput('ASCII', 'Ingrese un código Morse: '))
    lista_morse=morse.split()
    lista_traducida=[]
    for i in range (len(lista_morse)):
        for keyword, value in diccionario.items():
            if value==lista_morse[i]:
                lista_traducida.append(keyword)
    lista_traducida="".join(lista_traducida)
    turtle.write("La traducción es: %s " %lista_traducida,True,"center",("courier",15,"bold"))
'''


def button():
  Button(root, text="Poligono por lados", command=lambda:[lados(),regular()]).pack()
  Button(root, text="ASCII-MORSE", command=ASCII_morse).pack()
  #Button(root, text="MORSE-ASCII", command=morse_ASCII).pack()
  Button(root, text="DibujoLibre", command=dibujo_libre).pack()
  Button(root, text="Color", command= config, background = 'sky blue').pack()
  Button(root, text="Copiar", command=copiar).pack()
  Button(root, text="Pegar", command=pegar).pack()
  Button(root, text="Borrar todo", command=borrar).pack()
  Button(root, text="Deshacer", command=deshacer).pack()
  Button(root, text="Salir", command=salir).pack()
# Configuración inicial
#def config():
	
def main():
  config()
  button()
main()


root.mainloop()