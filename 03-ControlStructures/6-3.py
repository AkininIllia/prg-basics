###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False
light_switch2 = False
light_switch3 = True
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 1
if light_switch3:
    bulbs_on += 1
print(f"The number of bulbs illuminating the house is: {bulbs_on}")