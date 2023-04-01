# create onscreen turtle
import turtle, random    # allows to use the turtle library
import math
backGroundColor = input("What color background would you like? ")



wn = turtle.Screen()   #creates a graphics window
wn.title("Turle graphics")      #gives title to the screen
wn.bgcolor(str(backGroundColor))        #set background color



alexColor = input("What color do you want alex to be? ")
alexPen = int(input("What size do you want for alex? "))
alex = turtle.Turtle()    #create a turtle named alex
alex.color(str(alexColor))       # make alex red
alex.pensize(alexPen)
alex.left(90)   #tell alex to move forward by 150 units
alex.left(90)   #turn by 90 degrees
alex.forward(75)   #complete the second side of a triangle
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)



segunColor = input("What color do you want segun to be? ")
segun = turtle.Turtle()
segun.color(str(segunColor))
segun.pen(1)
segun.right(90)
segun.forward(150)
segun.left(90)
segun.forward(75)



ellaColor = input("What color do you want ella to be? ")
ella = turtle.Turtle()
ella.color(str(ellaColor))
ella.right(45)
ella.forward(75)
ella.left(90)
ella.forward(150)



jamalColor = input("What color do you want jamal to be? ")
jamal = turtle.Turtle()
jamal.color(str(jamalColor))
jamal.left(180)
jamal.forward(75)




lola = turtle.Turtle()
lola.pensize(5)

ayo = turtle.Turtle()
ayo.color("hotpink")

lola.forward(80)
lola.left(120)
lola.forward(80)
lola.left(120)
lola.forward(80)
lola.left(120)

lola.right(180)
lola.forward(80)

ayo.forward(180)
ayo.left(90)
ayo.forward(50)
ayo.left(90)
ayo.forward(50)
ayo.left(90)
ayo.forward(50)
ayo.left(90)


jamal = turtle.Turtle()
jamal.pensize(10)
jamal.color("blue")
jamal.right(90)
jamal.forward(150)

jamal.left(90)
jamal.forward(75)


tina = turtle.Turtle()
tina.pensize(10)
tina.color("Orange")
tina.left(180)
tina.forward(75)


ken = turtle.Turtle()
ken.color("blue")
ken.shape("turtle")

dist = 5
ken.up()     #lifts tail of the turtle to not draw line

for _ in range(30):
    ken.stamp()      # leave an impression on the canvas
    ken.forward(dist)
    ken.right(24)
    dist = dist + 2


elan = turtle.Turtle()

distance = 50
for _ in range(10):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10

nikea = turtle.Turtle()
nikea.shape("turtle")
nikea.penup()
for size in range(3):
    nikea.forward(50)
    nikea.stamp()


# prob = random.random()
# print(prob)
#
# diceThrow = random.randrange(1,7)
# print(diceThrow)
bob = turtle.Turtle()

for _ in range(8):
    bob.right(90)
    bob.forward(50)
    bob.left(90)
    bob.forward(50)
    bob.left(90)
    bob.forward(50)
    bob.left(90)
    bob.forward(50)
    bob.right(45)
    bob.forward(50)
    bob.right(90)
    bob.forward(50)


boob = turtle.Turtle()


boob.right(90)
boob.forward(50)
boob.left(90)
boob.forward(50)
boob.left(90)
boob.forward(50)
boob.left(90)
boob.forward(50)
boob.right(135)

dist = math.sqrt(50*50/2)

wn.exitonclick()







