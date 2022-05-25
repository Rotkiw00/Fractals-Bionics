import random
import turtle

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            colors = ['yellow', 'green', 'blue', 'red']
            t.pencolor(colors[random.randint(0, 3)])
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)


def main(iterations, axiom, rules, angle, length=8, size=2, y_offset=0,
         x_offset=0, offset_angle=0, width=450, height=450):

    inst = create_l_system(iterations, axiom, rules)
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)
    wn.bgcolor("black")
    t.up()
    t.backward(-x_offset)
    t.left(0)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    t.hideturtle()
    draw_l_system(t, inst, angle, length)

    wn.exitonclick()

# Równania afiniczne
# Krzywa sierpinskiego
axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 4 # TOP: 7
angle = 60
main(iterations, axiom, rules, angle)
