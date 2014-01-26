# a4.py
# Charles Lai(cjl223) and Tech Kuo(thk42)
# 10-23-12
from cturtle import *
from colormodel import *
import math
import inspect

"""Module to draw cool shapes with the Cornell Turtle.

The module can be run as an application to show off the various functions.
Unimplemented functions will do nothing."""


############# Helper functions for precondition verification #############

def is_number(x):
    """Return True is x is a float or int; False otherwise"""
    return (type(x) == float or type(x) == int)


def valid_window(w):
    """Return False if w is not a cturtle Window; True otherwise"""
    return type(w) == Window


def valid_turtle(t):
    """Return False if t is not a Turtle with drawmode True; True otherwise"""
    return type(t) == Turtle and t.drawmode


def valid_color(c):
    """Return False if c is wrong type to be a valid turtle color; True otherwise"""
    return (type(c) == RGB or
            type(c) == HSV or
            type(c) == tuple or
            type(c) == str)


def valid_speed(sp):
    """Return False if sp is not an int in 0..10; True otherwise"""
    return type(sp) == int and 0 <= sp and sp <=10


def valid_length(thelength):
    """Return False if thelength is not a number >=0; True otherwise"""
    return is_number(thelength) and 0 <= thelength


def valid_iterator(n):
    """Return False if n is not an int >=1; True otherwise"""
    return type(n) == int and 1 <= n


def valid_pen(p):
    """Return False if p is not a cturtle Pen with fillmode False; True otherwise"""
    return type(p) == Pen and not p.fill

#################### Two lines ####################


def draw_two_lines(w,sp):
    """In the middle of the window w, draw a green line 100 pixels to the
    west, then a red line 200 pixels to the south, using a new turtle
    that moves at speed sp, 0 <= sp <= 10, with 1 being slowest and
    10 fastest (and 0 being instant)

    Precondition: w is a cturtle Window object. sp is an int between 1 and 10 inclusive."""
    assert valid_window(w), `w`+' is an invalid Window argument'
    assert valid_speed(sp), `sp`+' is an invalid speed argument'

    t = Turtle(w)
    t.speed = sp
    t.color = 'green'
    t.forward(100) # draw a line 100 pixels in the current direction
    t.left(90)     # add 90 degrees to the angle
    t.color = 'red'
    t.forward(200)


#################### Geometric shapes ####################


# TASK 1
def draw_triangle(t, s, c):
    """Draw an equilateral triangle of side length s and color c at turtle t's
    current position.  If the turtle is facing west, the triangle points up and
    the turtle starts and ends at the east end of the base line.

    UPON COMPLETION, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS WHEN THE
    FUNCTION STARTED: position (x and y, within round-off errors), heading,
    color, and drawmode

    Precondition: t is a Turtle with drawmode True. s >= 0.
    c is a Turtle color, which can either be a string with a color name, or
    an RGB or HSV object from the colormodel module."""
    assert valid_turtle(t), `t`+' is an invalid Turtle argument'
    assert valid_length(s), `s`+' is an invalid length argument'
    assert valid_color(c), `c`+' is an invalid color argument'
    
    t.color = c
    for x in range(3):
        t.forward(s)
        t.right(120)
    t.color = 'red'


# TASK 2
def draw_hex(t, s):
    """Use turtle t to draw six equilateral triangles using the color 'orange'
    with side lengths s to form a hexagon, starting at the turtle's current
    position and heading. The middle of the hexagon is the turtle's starting
    position.

    UPON COMPLETION, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS WHEN THE
    FUNCTION STARTED: position (x and y, within round-off errors), heading,
    color, and drawmode

    Precondition: t is a Turtle with drawmode True. s >= 0."""
    assert valid_turtle(t), `t`+' is an invalid Turtle argument'
    assert valid_length(s), `s`+' is an invalid length argument'
    
    for x in range(6):
        draw_triangle(t,s,'orange')
        t.left(60)


#################### Spirals ####################


# TASK 3A
def draw_spiral(w, sp, z, ang, n):
    """Clear the window, then draw a spiral using
    draw_spiral_helper(t, sp, z, ang, n), where t is a newly created
    turtle that starts in the middle of the canvas facing east (NOT
    the default west). At
    the end, the turtle is left hidden (visible is False).

    Precondition: w is a cturtle Window object. sp is an int between
    0 and 10. n >= 1 an int. z >= 0. ang is a number."""
    assert valid_window(w), `w`+' is an invalid Window argument'
    assert valid_speed(sp), `sp`+' is an invalid speed argument'
    assert valid_length(z), `z`+' is an invalid length argument'
    assert valid_iterator(n), `n`+' is an invalid number-of-iterations arg'
    assert is_number(ang), `ang`+' is an invalid angle argument'
    
    w.clear()
    t = Turtle(w)
    t.speed = sp
    t.heading = 0
    draw_spiral_helper(t,sp,z,ang,n)
    t.visible = False


def draw_spiral_helper(t, sp, z, ang, n):
    """Draw a spiral of n lines beginning at turtle t's current position
    and heading, turning ang degrees to the left after each line.
    The turtle's speed is sp (1 is slowest, 10 fastest, 0 is instant).
    Line 0 is z pixels long; line 1, 2*z pixels; ...; so each line i is
    (i+1)*z pixels long. The lines alternate between red, blue, and green,
    in that order, with the first one red.

    UPON COMPLETION, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS WHEN THE
    FUNCTION STARTED: color, speed, visible, and drawmode.
    However, the final position and heading may be different.

    Precondition: t is a Turtle with drawmode True. sp is an int between
    0 and 10. n >= 1 an int. z >= 0. ang is a number"""
    assert valid_turtle(t), `t`+' is an invalid Turtle argument'
    assert valid_speed(sp), `sp`+' is an invalid speed argument'
    assert valid_length(z), `z`+' is an invalid length argument'
    assert valid_iterator(n), `n`+' is an invalid number-of-iterations arg'
    assert is_number(ang), `ang`+' is an invalid angle argument'
    
    zorig = z
    for x in range(1,n+1):
        if x%3 == 2:
            t.color = 'blue'
        elif x%3 == 1:
            t.color = 'red'
        else:
            t.color = 'green'
        t.forward(z)
        t.left(ang)
        z+=zorig


#################### Polygons ####################


# TASK 3B
def multi_polygons(w, sp, k, n, s):
    """Remove all drawings from the window. Draw polygons using
    multi_polygons_helper(t, sp, k, n, s), where t is a newly created turtle
    that starts in the middle of the window, facing north, and moves at
    speed sp. At the end, the turtle is left hidden (visible is False).

    Precondition: w is a cturtle Window object. sp is an int between
    0 and 10. k and n are ints with k >= 1, n >= 3. s >= 0."""
    assert valid_window(w), `w`+' is an invalid Window argument'
    assert valid_speed(sp), `sp`+' is an invalid speed argument'
    assert valid_length(s), `s`+' is an invalid length argument'
    assert n >= 3 and type(n) == int, `n`+' is an invalid n argument'
    assert valid_iterator(k), `k`+' is an invalid number-of-iterations arg'
    
    w.clear()
    t = Turtle(w)
    t.speed = sp
    t.heading = 90
    multi_polygons_helper(t, sp, k, n, s)
    t.visible = False


def multi_polygons_helper(t, sp, k, n, s):
    """Draw k n-sided polygons of side length s using turtle t, with t
    moving at speed sp (0 <= sp <= 10). The polygons are in alternating
    colors between red and green. Each polygon is drawn starting at the
    same place (within roundoff errors), but t turns left 360.0/k degrees
    after each polygon.

    At the end, ALL ATTRIBUTES of the turtle are the same as they were
    in the beginning (within roundoff errors).

    Precondition: t is a Turtle with drawmode True. sp is an int between
    0 and 10. k and n are ints with k >= 1, n >= 3. s >= 0."""
    assert valid_turtle(t), `t`+' is an invalid Turtle argument'
    assert valid_speed(sp), `sp`+' is an invalid speed argument'
    assert valid_length(s), `s`+' is an invalid length argument'
    assert n >= 3 and type(n) == int, `n`+' is an invalid n argument'
    assert valid_iterator(k), `k`+' is an invalid number-of-iterations arg'
    
    for x in range(1,k+1):
        if x%2 == 1:
            t.color = 'red'
        else:
            t.color = 'green'
        draw_polygon(t, sp, n, s)
        t.left(360.0/k)


# Useful helper function
def draw_polygon(t, sp, n, s):
    """Draw an n-sided polygon using turtle t. Each side is s pixels long.
    The polygon is drawn with turtle speed sp.

    UPON COMPLETION, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS WHEN THE
    FUNCTION STARTED: position (x and y, within round-off errors), heading,
    color, speed, visible, and drawmode

    Precondition: t is a Turtle with drawmode True. sp is an int between
    0 and 10. n is an int >= 3. s >= 0."""
    assert valid_turtle(t), `t`+' is an invalid Turtle argument'
    assert valid_speed(sp), `sp`+' is an invalid speed argument'
    assert (type(n) == int and n >=3), `n`+' is an invalid number of polygon sides'
    assert valid_length(s), `s`+' is an invalid length argument'
    
    initial_speed = t.speed
    t.speed = sp
    ang = 360.0/n # exterior angle between adjacent sides
    # Invariant: Just before the j-th iteration, j lines have been drawn,
    # t is in position and facing the direction to draw the next line.
    for _ in range(n):
        t.forward(s)
        t.left(ang)
    t.speed = initial_speed


#################### Radiating lines ####################


# TASK 3C
def radiate(w, sp, s, n):
    """Clear the window, then draw n straight radiating lines using
    radiate_helper(t, sp, s, n), where t is a new turtle starting
    at the middle of the screen and facing east. At the end,
    the turtle is left hidden (visible is False).

    Precondition: w is a cturtle Window object. sp is an int between
    1 and 10. n is an int >= 2. s >= 0."""
    assert valid_window(w), `w`+' is an invalid Window argument'
    assert valid_speed(sp), `sp`+' is an invalid speed argument'
    assert valid_length(s), `s`+' is an invalid length argument'
    assert n >= 2 and type(n)==int, `n`+' is an invalid n argument'
    
    w.clear()
    t = Turtle(w)
    t.speed = sp
    radiate_helper(t, sp, s, n)
    t.visible = False


def radiate_helper(t, sp, s, n):
    """Draw n straight radiating lines of length s at equal angles using
    turtle t with the turtle moving at speed sp.  A line drawn at
    angle ang, 0 <= ang < 360 has HSV color (ang % 360.0, 1, 1).

    UPON COMPLETION, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS WHEN THE
    FUNCTION STARTED: color, speed, visible, and drawmode.
    However, the final position and heading may be different.

    Precondition: t is a Turtle with drawmode True. sp is an int between
    0 and 10. n is an int >= 2. s >= 0."""
    assert valid_turtle(t), `t`+' is an invalid Turtle argument'
    assert valid_speed(sp), `sp`+' is an invalid speed argument'
    assert valid_length(s), `s`+' is an invalid length argument'
    assert n >= 2 and type(n)==int, `n`+' is an invalid n argument'
    
    for x in range(n):
        t.color=(HSV(t.heading%360.0, 1, 1))
        t.forward(s)
        t.backward(s)
        t.left(360.0/n)


#################### Sierpinski ####################


# TASK 4A
def sierpinski(w, d, s):
    """Remove all drawings from the graphics window and draw a
    'magenta' Sierpinski triangle with side length s, depth d, and bottom
    left corner (0, 0), using a newly created Pen (NOT Turtle).  The pen
    is left hidden (visible is False).

    Precondition: w is a cturtle Window object. d >= 0 is an int and s > 0."""
    assert valid_window(w), `w`+' is an invalid Window argument'
    assert type(d)== int and d>=0, `d`+' is an invalid depth argument'
    assert is_number(s) and s>0, `s`+'is an invalid side length argument'
    
    w.clear()
    p = Pen(w)
    p.pencolor = 'magenta'
    sierpinski_helper(p, 0.0, 0.0, d, s)
    p.visible = False


def sierpinski_helper(p, x, y, d, s):
    """Using pen p, draw a Sierpinksi triangle of depth d with side
    length s and bottom left corner (x, y).

    Precondition: p is a Pen with fill attribute False.
    x and y are floats or ints. d >= 0 is an int. s > 0."""
    assert valid_pen(p), `p`+' is an invalid Pen argument'
    assert type(d)== int and d>=0, `d`+' is an invalid depth argument'
    assert is_number(s) and s>0 , `s`+'is an invalid side length argument'
    
    h = (math.sqrt(3)/2)*s
    if d == 0:
        p.move(x,y)
        fill_triangle(p, s)
    else:
        sierpinski_helper(p,x,y,d-1,s/2.0)
        sierpinski_helper(p,x+(s/2.0),y,d-1,s/2.0)
        sierpinski_helper(p,x+(s/4.0),y+(h/2.0),d-1,s/2.0)


# Useful helper function
def fill_triangle(p, s):
    """Fill the equilateral triangle of side length s with left point of
    its base at the current position of p and triangle pointing up.
    When done, the position of Pen p should be as it was initially.

    Precondition: p is a Pen with fill attribute False. s > 0."""
    #assertion preconditions omitted (you do not need to add these)

    h = s * math.sqrt(.75);
    p.fill = True
    p.drawLine(s, 0)
    p.drawLine(-s/2, h)
    p.drawLine(-s/2, -h)
    p.fill = False


#################### Grisly snowflakes ####################


# TASK 4B
def grisly(w, d, s):
    """Remove all drawings from the window and draw a 'gray' grisly snowflake
    of depth d with side length s and center at (0, 0), using a newly created
    Pen (NOT Turtle). The pen is hidden during drawing and left hidden at the end.

    Precondition: w is a cturtle Window object. d >= 0 is an int. s > 0."""
    assert valid_window(w), `w`+' is an invalid Window argument'
    assert type(d)==int and d>=0,`d`+'is an invalid d argument'
    assert is_number(s) and s>0,`s`+'is an invalid s argument'
    
    w.clear()
    p = Pen(w)
    p.visible = False
    p.pencolor = 'gray'
    grisly_helper(p, 0.0, 0.0, d, s)


def grisly_helper(p, x, y, d, s):
    """Using Pen p, draw a grisly snowflake of depth d with side length s
    and center (x, y).

    Precondition: p is a Pen with fill attribute False.
    x and y are numbers (ints or floats). d >= 0 is an int. s > 0."""
    assert valid_pen(p), `p` + ' is an invalid Pen argument'
    assert is_number(x), `x` + ' is an invalid x argument'
    assert is_number(y), `y` + ' is an invalid y argument'
    assert type(d) == int and d >= 0,`d` + ' is an invalid d argument'
    assert is_number(s) and s>0,`s` + ' is an invalid s argument'
    
    h = (math.sqrt(3)/3)*s
    if d == 0:
        p.move(x,y)
        fill_hex(p,s,x,y)
    else:
        grisly_helper(p,x,y,d-1,s/3)
        grisly_helper(p,x-(s/3.0),y+h,d-1,s/3.0)
        grisly_helper(p,x+(s/3.0),y+h,d-1,s/3.0)
        grisly_helper(p,x-(2*s/3.0),y,d-1,s/3.0)
        grisly_helper(p,x+(2*s/3.0),y,d-1,s/3.0)
        grisly_helper(p,x-(s/3.0),y-h,d-1,s/3.0)
        grisly_helper(p,x+(s/3.0),y-h,d-1,s/3.0)


# Useful helper function
def fill_hex(p, s, x, y):
    """Fill a hexagon of side length s with center at (x, y) using pen p.

    Precondition: p is a Pen with fill attribute False. s > 0 .
    x and y are numbers (ints or floats)."""
    #assertion preconditions omitted (you do not need to add these)

    p.move(x + s, y)
    dx = s*math.cos(math.pi/3.0)
    dy = s*math.sin(math.pi/3.0)
    p.fill = True
    p.drawLine(-dx, dy);
    p.drawLine(-s, 0);
    p.drawLine(-dx, -dy);
    p.drawLine(dx, -dy);
    p.drawLine(s, 0);
    p.drawLine(dx, dy)
    p.fill = False


#################### HTrees ####################


# TASK 4C
#IGNORE the code below. It is unfinished.
def Htree(w, d, s):
    """Remove all drawings from the window and draw a 'black' H-tree centered
    at (0,0) using a newly created Pen (NOT Turtle). The pen is hidden during
    drawing and left hidden at the end.

    Precondition: w is a cturtle Window object. d >= 0 is an int. s > 0."""
    assert valid_window(w), `w`+' is an invalid Window argument'
    assert d >= 0 and is_number(d), `d` +" is an invalid d argument"
    assert s>0, `s` + "is an invalid s argument"
    
    w.clear()
    p = Pen(w)
    p.visible = False
    p.pencolor = 'black'
    Htree_helper(p, 0.0, 0.0, d, s)


def Htree_helper(p, x, y, d, s):
    """Draw an H-tree of depth d and size s with center (x, y) using pen p.

    Precondition: p is a Pen with fill attribute False.
    x and y are numbers. d >= 0 is an int. s > 0."""
    assert valid_pen(p), `w`+' is an invalid Pen argument'
    assert is_number(x), `x` + ' is an invalid x argument'
    assert is_number(y), `y` + ' is an invalid y argument'
    assert d >= 0 and type(d) == int,`d` + ' is an invalid d argument'
    assert s > 0,`s` + ' is an invalid s argument'
    
    if d == 0:
        p.move(x,y)
        drawH(p, x , y, s)
    else:
        Htree_helper(p,x+(s/2.0),y+(s/2.0),d-1,s/2.0)
        Htree_helper(p,x+(s/2.0),y-(s/2.0),d-1,s/2.0)
        Htree_helper(p,x-(s/2.0),y+(s/2.0),d-1,s/2.0)
        Htree_helper(p,x-(s/2.0),y-(s/2.0),d-1,s/2.0)



def drawH(p, x, y, s):
    """Draw an H at center (x, y) of size s using pen p.

    Precondition: p is a Pen with fill attribute False. s > 0.
    x and y are numbers."""
    assert valid_pen(p), `p`+' is an invalid Pen argument'
    assert is_number(x), `x` + ' is an invalid x argument'
    assert is_number(y), `y` + ' is an invalid y argument'
    assert s > 0,`s` + ' is an invalid s argument'
    
    p.drawLine(x+(s/2),0)
    p.drawLine(x-s,0)
    p.drawLine(0,y+(s/2))
    p.drawLine(0,y-s)
    p.drawLine(0,y+(s/2))
    p.drawLine(x+s,0)
    p.drawLine(0,y+(s/2))
    p.drawLine(0,y-s)


################ Test Function #################


def main():
    """Run each of the functions, pausing for a key press at each step"""
    w = Window()

    print 'Calling draw_two_lines'
    draw_two_lines(w,2)
    raw_input('Hit <return> ')

    # Need a new turtle to draw
    w.clear()
    turt = Turtle(w)



    print 'Calling draw_triangle'
    draw_triangle(turt,50,'green')
    raw_input('Hit <return> ')

    turt.clear()
    print 'Calling draw_hex'
    draw_hex(turt,50)
    raw_input('Hit <return> ')

    # The remaining functions provide their own turtle or pen
    turt.visible = False

    print 'Calling draw_spiral'
    draw_spiral(w, 10, 10, 75, 10)
    raw_input('Hit <return> ')

    print 'Calling multi_polygons'
    multi_polygons(w, 10, 40, 5, 35)
    raw_input('Hit <return> ')

    print 'Calling radiate'
    radiate(w, 10, 150, 45)
    raw_input('Hit <return> ')

    print 'Calling sierpinski'
    sierpinski(w, 3, 200)
    raw_input('Hit <return> ')

    print 'Calling grisly'
    grisly(w, 2, 150)
    raw_input('Hit <return> ')

    print 'Calling Htree'
    Htree(w, 0, 243)
    raw_input('Hit <return> ')


# Application code
if __name__ == '__main__':
    main()
