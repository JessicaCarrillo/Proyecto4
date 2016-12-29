import turtle
a = int(input("ingrese un numero de puntas para una estrella : "))
t = turtle.Pen()
t=turtle.Screen()
tess=turtle.Turtle()
t.reset()
if(a%2==0):
        t.title("ESTRELLA DE LADOS PARES")
        for x in range(a):
                tess.forward(100)
                aa=a/2
                an = 180/aa
                ang = 180 - an
                tess.left(ang)
else:
        t.title("ESTRELLA DE LADOS IMPARES")
        for x in range(1,a+1):
                tess.forward(200)
                an = 360/2
                ang = 180/a
                angu=an+ang
                tess.left(angu)
                
turtle.getscreen()._root.mainloop()

