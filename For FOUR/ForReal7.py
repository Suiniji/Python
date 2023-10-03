
q1_x = int(input("Enter the x-coordinate of the piece1: "))
q1_y = int(input("Enter the y-coordinate of the piece1: "))
q2_x = int(input("Enter the x-coordinate of the piece2: "))
q2_y = int(input("Enter the y-coordinate of the piece2: "))


if (q1_x * q1_y)%2 == (q2_x * q2_y)%2:
    print(True)
else:
    print(False)