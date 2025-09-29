print("Equation solver 1.0")
print("Enter The Coefficient Of x, y, z In 3 Equations like:- ")
print(" x11 y12 z13 a1 \n x21 y22 z23 a2 \n x31 y32 z33 a3")

x11, y12, z13, d1 = map(float, input("First Equation: ").split())
x21, y22, z23, d2 = map(float, input("Second Equation: ").split())
x31, y32, z33, d3 = map(float, input("Third Equation: ").split())

q = [
    [x11, y12, z13, d1],
    [x21, y22, z23, d2],
    [x31, y32, z33, d3]
]


if q[0][0] == 0:
    if q[1][0] != 0:
        q[0], q[1] = q[1], q[0]
    elif q[2][0] != 0:
        q[0], q[2] = q[2], q[0]
    else:
        print("No solution exists.")
        exit()

b = q[1][0] / q[0][0]
q[1][1] -= b * q[0][1]
q[1][2] -= b * q[0][2]
q[1][3] -= b * q[0][3]
q[1][0] = 0

v = q[2][0] / q[0][0]
q[2][1] -= v * q[0][1]
q[2][2] -= v * q[0][2]
q[2][3] -= v * q[0][3]
q[2][0] = 0

if q[1][1] == 0:
    if q[2][1] != 0:
        q[1], q[2] = q[2], q[1]
    else:
        print("No solution exists.")
        exit()

c = q[2][1] / q[1][1]
q[2][2] -= c * q[1][2]
q[2][3] -= c * q[1][3]
q[2][1] = 0


if q[2][2] == 0:
    print("No solution exists.")
    exit()


Z = q[2][3] / q[2][2]
Y = (q[1][3] - Z * q[1][2]) / q[1][1]
X = (q[0][3] - (Z * q[0][2] + Y * q[0][1])) / q[0][0]

print(f"X = {X}, Y = {Y}, Z = {Z}")
