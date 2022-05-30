# Wersja 0.0.1 - do modyfikacji
import turtle
import tkinter as tk
import random

# Clean window function
def clean():
    t.clear()
    turtle.bye()

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
def koch_fractal_draw(iterations = 4, axiom = "F--F--F", rules = {"F": "F+F--F+F"}, angle = 60, length=8, size=2, y_offset=0,
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

#zrobic: Przyciski rysujace fraktale

def sierpinski_fractal_draw(iterations, axiom, rules, angle, length, size, y_offset,x_offset,offset_angle):
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


###########################
#  -------- MAIN --------
###########################
root = tk.Tk()
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

canvas = tk.Canvas(frame)
canvas.config(width=700, height=700)
canvas.pack()

global screen
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("black")

# Konfiguracja ilosci kolumn i wierszy
root.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
root.grid_columnconfigure((0, 1, 2, 3), weight=1)

bttn_clean_window = tk.Button(bottom_frame, width=8, height=2, text="Clean", command=lambda: clean())
bttn_exit = tk.Button(bottom_frame, width=8, height=2, text="Exit", command=lambda: root.quit())
bttn_draw_koch = tk.Button(top_frame, width=8, height=2, text="Draw Fractal", command=lambda: koch_fractal_draw())
bttn_test = tk.Button(top_frame, width=8, height=2, text="Test")

# Konfiguracja rozmieszczenia przycisków
bttn_draw_koch.grid(row=1, column=0)
bttn_test.grid(row=2,column=0)
bttn_clean_window.grid(row=3, column=0)
bttn_exit.grid(row=4, column=0)

# Odstepy miedzy przyciskami
tk.Label(bottom_frame).grid(row=5)
tk.Label(top_frame).grid(row=0)


# Główna pętla programu
root.mainloop()