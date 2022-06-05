# Wersja 0.0.1 - do modyfikacji
import turtle
import tkinter as tk
import random
from tkinter import messagebox


# Clean window function
def clean():
    messagebox.showinfo('Informacja', 'Właśnie czyścisz okno.')
    t.clear()
    turtle.bye()


def exit():
    clean()
    root.quit()


# Useful functions for drawing fractals
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


# Specific functions for specific fractal draw
# KOCH FRACTAL
def koch_fractal_draw(iterations=4, axiom="F--F--F", rules={"F": "F+F--F+F"}, angle=60, length=6, size=2, y_offset=-200,
                      x_offset=-300, offset_angle=0):
    inst = create_l_system(iterations, axiom, rules)
    global t
    t = turtle.RawTurtle(screen)
    t.up()
    t.goto(x_offset, y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    t.hideturtle()
    draw_l_system(t, inst, angle, length)


def sierpinski_fractal_draw(iterations=6, axiom="YF", rules={"X": "YF+XF+Y", "Y": "XF-YF-X"}, angle=60, length=6,
                            size=2, y_offset=-200, x_offset=-200, offset_angle=60):
    inst = create_l_system(iterations, axiom, rules)
    global t
    t = turtle.RawTurtle(screen)
    t.up()
    t.goto(x_offset, y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    t.hideturtle()
    draw_l_system(t, inst, angle, length)


def rings_fractal_draw(iterations=4, axiom="F+F+F+F", rules={"F": "FF+F+F+F+F+F-F"}, angle=90, length=6, size=2,
                       y_offset=-0, x_offset=-100, offset_angle=60):
    inst = create_l_system(iterations, axiom, rules)
    global t
    t = turtle.RawTurtle(screen)
    t.up()
    t.goto(x_offset, y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    t.hideturtle()
    draw_l_system(t, inst, angle, length)


def levy_fractal_draw(iterations=16, axiom="F", rules={"F": "+F--F+"}, angle=45, length=6, size=2, y_offset=-150,
                      x_offset=100, offset_angle=60):
    inst = create_l_system(iterations, axiom, rules)
    global t
    t = turtle.RawTurtle(screen)
    t.up()
    t.goto(x_offset, y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    t.hideturtle()
    draw_l_system(t, inst, angle, length)


def dragon_fractal_draw(iterations=15, axiom="FX+FX+FX", rules={"X": "X+YF+", "Y": "-FX-Y"}, angle=90, length=6, size=2,
                        y_offset=-100, x_offset=-100, offset_angle=60):
    inst = create_l_system(iterations, axiom, rules)
    global t
    t = turtle.RawTurtle(screen)
    t.up()
    t.goto(x_offset, y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    t.hideturtle()
    draw_l_system(t, inst, angle, length)


###########################
#  -------- MAIN --------
###########################
root = tk.Tk()
root.geometry("1100x1100")
root.resizable(False, False)
root.title("Fractals GUI")

# Okno/ramka dla Turtle do rysowania fraktali
frame = tk.Frame(root)
frame.pack(side=tk.LEFT)

# Ramki dla przycisków
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM)

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP)

center_frame = tk.Frame(root)
center_frame.pack(pady=150, side=tk.TOP)

canvas = tk.Canvas(frame)
canvas.config(width=900, height=900)
canvas.pack()

global screen
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("black")

# Konfiguracja ilosci kolumn i wierszy
root.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
root.grid_columnconfigure((0, 1, 2, 3), weight=1)

bttn_clean_window = tk.Button(top_frame, width=8, height=2, text="Clean window", command=lambda: clean())
bttn_draw_koch = tk.Button(center_frame, width=8, height=2, text="Koch Snowflake", command=lambda: koch_fractal_draw())
bttn_draw_sierpinski = tk.Button(center_frame, width=8, height=2, text="Sierpinski\nTriangle",
                                 command=lambda: sierpinski_fractal_draw())
bttn_draw_rings = tk.Button(center_frame, width=8, height=2, text="Rings", command=lambda: rings_fractal_draw())
bttn_draw_levy = tk.Button(center_frame, width=8, height=2, text="Levy-C-Curve", command=lambda: levy_fractal_draw())
bttn_draw_dragon = tk.Button(center_frame, width=8, height=4, text="Three\nDragon\nCurve",
                             command=lambda: dragon_fractal_draw())
bttn_exit = tk.Button(bottom_frame, width=8, height=2, text="Exit", command=lambda: exit())

# Konfiguracja rozmieszczenia przycisków
bttn_clean_window.grid(row=1, column=0)
bttn_draw_koch.grid(row=2, column=0)
bttn_draw_sierpinski.grid(row=3, column=0)
bttn_draw_rings.grid(row=4,column=0)
bttn_draw_levy.grid(row=5,column=0)
bttn_draw_dragon.grid(row=6,column=0)
bttn_exit.grid(row=7, column=0)

# Odstepy miedzy przyciskami
tk.Label(bottom_frame).grid(row=8)
tk.Label(top_frame).grid(row=0)

# Główna pętla aplikacji do rysowania fraktali
root.mainloop()