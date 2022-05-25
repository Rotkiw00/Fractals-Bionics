import turtle

MIN_BRANCH_LEN = 5
color = 'green'
speed = 0

def drawingTree(object, branch_len, shorten_by, angle):
    if branch_len > MIN_BRANCH_LEN:
        object.forward(branch_len)
        new_len = branch_len - shorten_by

        object.left(angle)
        drawingTree(object,new_len,shorten_by,angle)

        object.right(angle*2)
        drawingTree(object,new_len,shorten_by,angle)

        object.left(angle)
        object.backward(branch_len)

tree = turtle.Turtle()
tree.hideturtle()
tree.setheading(90)
tree.color(color)
tree.speed(speed)

drawingTree(tree,50,5, 30)
turtle.mainloop()