# Wersja 0.0.1 - do modyfikacji
import turtle
import tkinter as tk
import random

# Initial condition
iterations = 4
axiom = "F--F--F"
rules = {"F": "F+F--F+F"}
angle = 60


def clean():
    t.clear()
    turtle.bye()


# Functions
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


def draw_fractal(iterations, axiom, rules, angle, length=8, size=2, y_offset=0,
                 x_offset=0, offset_angle=0):
    inst = create_l_system(iterations, axiom, rules)
    global t
    t = turtle.RawTurtle(screen)
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


# Invoking - wywołanie
root = tk.Tk()
root.resizable(False, False)
root.title("Fractals GUI")

frame = tk.Frame(root)
frame.pack(side=tk.LEFT)

bottomframe = tk.Frame(root)
bottomframe.pack(side=tk.LEFT)

canvas = tk.Canvas(frame)
canvas.config(width=700, height=700)
canvas.pack()

global screen
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("black")


root.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
root.grid_columnconfigure((0, 1, 2, 3), weight=1)

button_draw = tk.Button(bottomframe, width=8, height=2, text="Draw Fractal", command=lambda: draw_fractal(iterations, axiom, rules, angle))
button_clean = tk.Button(bottomframe, width=8, height=2,text="Clean", command=lambda: clean())
button_exit = tk.Button(bottomframe, width=8, height=2,text="Exit", command=lambda: root.quit())
button_draw.grid(row=0,column=0)
button_clean.grid(row=1,column=0)
button_exit.grid(row=2,column=0)

tk.Label(bottomframe).grid(row=3)

root.mainloop()