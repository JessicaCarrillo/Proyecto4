import turtle
import os
turtle.setup(750,300)
t=turtle.Screen()
t.bgcolor("black")
t=turtle.Screen()
t.title("MI NOMBRE")
t=turtle.Turtle()
t=turtle.Pen()
t.reset()
t.color("red")
t.up()
t.right(360)
t.setpos(-250,1)
t.down()

#CREACION DE LA LETRA J
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(80)
t.right(270)
t.forward(20)
t.right(270)
t.forward(60)
t.left(270)

t.forward(30)
t.right(270)
t.forward(20)
t.left(90)
t.end_fill()


#CREACION DE LA LETRA E
t.up()
t.right(360)
t.forward(70)
t.down()
t.begin_fill()
t.color("red")
t.forward(45)
t.left(90)
t.forward(15)
t.right(270)
t.forward(20)
t.left(270)
t.forward(15)
t.left(270)
t.forward(20)
t.left(90)
t.forward(15)
t.left(90)
t.forward(20)
t.left(270)
t.forward(15)
t.left(270)
t.forward(20)
t.left(90)
t.forward(15)
t.right(270)
t.forward(45)
t.left(90)

t.forward(76)
t.end_fill()


#CREACION DE LA LETRA S
t.up()
t.left(90)
t.forward(70)
t.down()
t.begin_fill()
t.color("yellow")
t.forward(45)
t.left(90)
t.forward(40)
t.left(90)
t.forward(25)
t.left(270)
t.forward(15)
t.right(-270)
t.forward(25)
t.left(90)
t.forward(20)
t.left(90)
t.forward(45)
t.left(-270)
t.forward(46)

t.right(-90)
t.forward(25)

t.left(-90)
t.forward(15)
t.left(270)
t.forward(25)
t.left(90)
t.forward(15)


t.end_fill()


#CREACION DE LA LETRA S
t.up()
t.left(90)
t.forward(70)
t.down()
t.begin_fill()
t.color("yellow")
t.forward(45)
t.left(90)
t.forward(40)
t.left(90)
t.forward(25)
t.left(270)
t.forward(15)
t.right(-270)
t.forward(25)
t.left(90)
t.forward(20)
t.left(90)
t.forward(45)
t.left(-270)
t.forward(46)

t.right(-90)
t.forward(25)

t.left(-90)
t.forward(15)
t.left(270)
t.forward(25)
t.left(90)
t.forward(15)

t.end_fill()


#CREACION DE LA LETRA I
t.up()
t.left(90)
t.forward(70)
t.down()
t.begin_fill()
t.color("yellow")
t.forward(20)
t.left(90)
t.forward(75)
t.left(90)
t.forward(20)
t.left(90)
t.forward(75)
t.end_fill()

#CREACION DE LA LETRA C
t.up()
t.left(90)
t.forward(45)
t.down()
t.begin_fill()
t.color("green")
t.forward(50)
t.left(90)
t.forward(15)
t.left(90)
t.forward(30)
t.left(270)
t.forward(45)
t.right(-270)
t.forward(30)
t.left(90)
t.forward(15)
t.left(90)
t.forward(50)
t.left(90)
t.forward(75)
t.end_fill()

#CREACION DE LA LETRA A
t.up()
t.left(90)
t.forward(75)
t.down()
t.begin_fill()
t.color("green")
t.forward(20)
t.left(90)
t.forward(35)
t.left(-90)
t.forward(25)
t.left(-90)
t.forward(35)
t.left(90)
t.forward(20)
t.left(90)
t.forward(75)
t.left(90)
t.forward(65)
t.left(90)
t.forward(75)
t.end_fill()

t.up()
t.left(145)
t.forward(65)
t.down()
t.begin_fill()
t.color("black")
t.circle(8)
t.end_fill()



turtle.getscreen()._root.mainloop()





