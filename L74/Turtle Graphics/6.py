import turtle
screen = turtle.Screen()
turtle.penup()
turtle.write("Press the Up/Down or a to change background color ", font = ('Arial', 10, 'bold'))
def up():
	screen.bgcolor('blue')
def down():
	screen.bgcolor('green')
screen.onkey(up, "Up")
screen.onkeypress(down, "Down")
screen.listen()
turtle.done()