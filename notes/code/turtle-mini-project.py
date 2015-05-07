import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(50)
		some_turtle.right(90)

def draw_triangle(some_turtle):
	for i in range(1,4):
		some_turtle.forward(100)
		some_turtle.left(120)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("white")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(0)
	for i in range(1,73):
		draw_square(brad)
		brad.right(5)

	hans = turtle.Turtle()
	hans.shape("turtle")
	hans.color("blue")
	hans.speed(0)

	for i in range(1,25):
		draw_triangle(hans)
		hans.right(15)

	stengel = turtle.Turtle()
	stengel.color("green")
	stengel.shape("turtle")
	stengel.pensize(5)
	stengel.right(90)
	stengel.forward(250)

	window.exitonclick()

draw_art()