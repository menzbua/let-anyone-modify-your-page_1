import turtle

def draw():
	window = turtle.Screen()
	window.bgcolor("green")
#	draw_circle()
	for i in range(1,360):
		draw_square()
#	draw_triangle()

	window.exitonclick()

def draw_circle():
	hans = turtle.Turtle()
	hans.circle(100)

def draw_triangle():
	wurschd = turtle.Turtle()
	wurschd.color("blue")
	i = 0
	while i < 3:
		wurschd.forward(-200)
		wurschd.left(120)
		i = i + 1

def draw_square():
	brad = turtle.Turtle()
	brad.shape("circle")
	brad.color("red")
	brad.speed("slow")
	i = 0
	while i < 4:
		brad.forward(200)
		brad.right(90)
	 	i = i + 1

draw()