import turtle
t = turtle.Turtle()
sc = turtle.Screen()
sc.bgcolor("black")
list = ["green", "red", "purple", "blue", "yellow", "cyan"]

for i in range(250):
    t.color(list[i % 5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)

turtle.mainloop()
