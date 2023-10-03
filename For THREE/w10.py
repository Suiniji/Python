
q1_x = int(input("Enter the x-coordinate of the queen1: "))
q1_y = int(input("Enter the y-coordinate of the queen1: "))
q2_x = int(input("Enter the x-coordinate of the queen2: "))
q2_y = int(input("Enter the y-coordinate of the queen2: "))

x1, y1 = q1_x, q1_y
x2, y2 = q2_x, q2_y

if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("The queens can attack each other.")
else:
    print("The queens cannot attack each other.")