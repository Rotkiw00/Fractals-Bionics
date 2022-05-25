import turtle

SPEED = 0
HEIGHT = 500
WIDTH = 500
SET_ANGLE = 0
PEN_X = -110
PEN_Y = 75
COLORS = ['red', 'cyan', 'yellow', 'blue', 'green', 'pink']
BG_COLOR = 'black'

def koch_curve(koch, iter, len, scale_factor, angle):
  if iter == 0:
    koch.pencolor(COLORS[i])
    koch.forward(len)
  else:
    koch.pencolor(COLORS[i])
    iter -= 1
    len /= scale_factor
    koch_curve(koch, iter, len, scale_factor, angle)
    koch.left(angle)
    koch_curve(koch, iter, len, scale_factor, angle)
    koch.right(angle * 2)
    koch_curve(koch, iter, len, scale_factor, angle)
    koch.left(angle)
    koch_curve(koch, iter, len, scale_factor, angle)

k_curve = turtle.Turtle()
k_curve.hideturtle()

screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor(BG_COLOR)

k_curve.penup()
k_curve.goto(x=PEN_X,y=PEN_Y)
k_curve.pendown()

k_curve.setheading(SET_ANGLE)
k_curve.speed(SPEED)

for i in range(3):
    koch_curve(k_curve, 3, 200, 3, 60)
    k_curve.right(120)

turtle.mainloop()