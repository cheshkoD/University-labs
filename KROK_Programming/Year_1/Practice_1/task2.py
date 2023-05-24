import math

# (1) Assume that we specify two points in space by definint the x and y
#       coordinate of each using x1, y1, x2, and y2 all which are float.
#       Write an expression that computes

x1=float(input('x1 = '))
x2=float(input('x2 = '))
y1=float(input('y1 = '))
y2=float(input('y2 = '))
print('--------------------')

    #(1.1)...the distance between these points
print('Distance between these two points:',  math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

    #(1.2)...the slope of the line from the first point to the second
a=int((y2-y1)/(x2-x1))
print('The slope of the line from the first point to the second: ',math.atan(a))

    #(1.3)...whether both points lie on the same line from the origin

    #(1.4)...whether the first point is above the second
print('Is the first point above the second?',  (y1 > y2) )

    #(1.5)...what quadrant the first point lies in (1st, 2nd, 3rd, or 4th)
def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x > 0 > y:
        return 4
    elif x < 0 < y:
        return 2
    elif x < 0 and y < 0:
        return 3
print('First point lies in ', quadrant(x1, y1),'Quadrant')

    #(1.6)..whether the two points lie in the same quadrant
print('Do this two points lie in the same quadrant?', quadrant(x1, y1) == quadrant(x2, y2))
