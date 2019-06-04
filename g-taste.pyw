import keyboard as kb
import pyautogui as auto

# initial points for calculating other points based on resolution, these points are taken on a display of 1920x1080 resolution tested on all resolution below
# it but not above 1920x1080 resolution

point0 = (271,995)
point1 = (368,995)

# calculing the factors and new points based on that factor and resolution of current display

factorx0 = 1920/point0[0]
factory0 = 1080/point0[1]
factorx1 = 1920/point1[0]
factory1 = 1080/point1[1]
width, height = auto.size() # current resolution

newpoint0 = (int(width/factorx0), int(height/factory0))
newpoint1 = (int(width/factorx1), int(height/factory1))

difference = newpoint1[0]-newpoint0[0]
trigger = 0

while True:
    if kb.is_pressed('1'):
        trigger=1
        auto.moveTo(newpoint0[0],newpoint0[1],0)
#    elif auto.position()[1] != newpoint0[1]:
#        trigger=0
    
    if trigger is 1:
        if kb.is_pressed('left'):
            if auto.position()[0] == newpoint0[0]:
                auto.moveTo(newpoint0[0]+(13*difference),newpoint0[1],0)
            else:
                auto.move(0-difference,0)
        elif kb.is_pressed('right'):
            if auto.position()[0] == newpoint0[0]+(13*difference):
                auto.moveTo(newpoint0[0],newpoint0[1],0)
            else:
                auto.move(difference,0)
        elif kb.is_pressed('z'):
            auto.click()
    else:
        pass