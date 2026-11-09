x = 5
y = 2

if x == 0 and y == 0:
    position = "at the origin (0,0)"
elif x == 0:
    position = "on the Y axis"
elif y == 0:
    position = "on the X axis"
elif x > 0 and y > 0:
    position = "in the first quadrant"
elif x < 0 and y > 0:
    position = "in the second quadrant"
elif x < 0 and y < 0:
    position = "in the third quadrant"
else:
    position = "in the fourth quadrant"

print(f"x = {x}")
print(f"y = {y}")
print(f"Point P({x},{y}) is {position} of the coordinate system")