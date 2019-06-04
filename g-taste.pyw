# push pull taste
import keyboard as kb
import pyautogui as auto

# initial points for calculating other points based on resolution, these points are taken on a display of 1920x1080 resolution tested on all resolution below
# it but not above 1920x1080 resolution

point0 = (271,995)
x0,y0=point0
point1 = (368,995)
x1, y1 = point1

# calculing the factors and new points based on that factor and resolution of current display

factorx0 = float(1920/x0)
factory0 = float(1080/y0)
factorx1 = float(1920/x1)
factory1 = float(1080/y1)
width, height = auto.size() # current resolution

newpoint0 = (width/factorx0, height/factory0)
newpoint1 = (width/factorx1, height/factory1)
newx0, newy0 = newpoint0
newx1, newy1 = newpoint1
difference = newx1-newx0
trigger = 0

while True:
    if kb.is_pressed('1'):
        trigger=1
        auto.moveTo(newx0,newy0,0)
    
    if trigger is 1:
        if kb.is_pressed('left'):
            if auto.position() == (newx0,newy0):
                auto.moveTo(newx0+(13*difference),newy0,0)
            else:
                auto.move(0-difference,0)
        elif kb.is_pressed('right'):
            if auto.position() == (newx0+(13*difference),newy0):
                auto.moveTo(newx0,newy0,0)
            else:
                auto.move(difference,0)
        elif kb.is_pressed('z'):
            auto.click()
    else:
        pass