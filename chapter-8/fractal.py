import turtle


def setup(pencil):
    pencil.color("blue")
    pencil.penup()
    pencil.goto(-200, 100)
    pencil.pendown()


def koch(pencil, size, order):
    if order == 0:
        pencil.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(pencil, size / 3, order - 1)
            pencil.left(angle)


def main():
    turtle.tracer(0)  # Turn off animation for faster drawing
    pencil = turtle.Turtle()
    pencil.speed(0)  # Set max drawing speed
    setup(pencil)

    order = 4  # You can change the order here
    size = 400
    koch(pencil, size, order)

    turtle.update()  # Update screen after drawing
    turtle.mainloop()


if __name__ == "__main__":
    main()
