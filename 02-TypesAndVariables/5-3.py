###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
volume = float(a) * float(b) * float(c)
surface_area = 2 * (float(a) * float(b) + float(a) *float(c) + float(b) * float(c))
print('Volume =', volume)
print('Surface area =', surface_area)