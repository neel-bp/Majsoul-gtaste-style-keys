import keyboard as kb
import pyautogui as auto

# initial points for calculating other points based on resolution, these points are taken on a display of 1920x1080 resolution tested on all resolution below
# it but not above 1920x1080 resolution

point0 = (271,995)
point1 = (368,995)
skipcall = (1310,823)
call1 = (1046,823)

# calculing the factors and new points based on that factor and resolution of current display

factorx0 = 1920/point0[0]
factory0 = 1080/point0[1]
factorx1 = 1920/point1[0]
factory1 = 1080/point1[1]
factorxskip = 1920/skipcall[0]
factoryskip = 1080/skipcall[1]
factorxcall = 1920/call1[0]
factorycall = 1080/call1[1]

width, height = auto.size() # current resolution

newpoint0 = (int(width/factorx0), int(height/factory0))
newpoint1 = (int(width/factorx1), int(height/factory1))
newskip = (int(width/factorxskip), int(height/factoryskip))
newcall = (int(width/factorxcall), int(height/factorycall))

tiledifference = newpoint1[0]-newpoint0[0]
calldifference = newskip[0]-newcall[0]
trigger = 0

while True:
    if kb.is_pressed('1'):
        trigger=1
        auto.moveTo(newpoint0[0],newpoint0[1],0)
#    elif auto.position()[1] != newpoint0[1]:
#        trigger=0
    
    if trigger is 1:
        if kb.is_pressed('left'):
            if auto.position()[1] == newpoint0[1]:
                if auto.position()[0] == newpoint0[0]:
                    auto.moveTo(newpoint0[0]+(13*tiledifference),newpoint0[1],0)
                else:
                    auto.move(0-tiledifference,0)

            elif auto.position()[1] == newskip[1]:
                if auto.position()[0] == newskip[0]-calldifference:
                    auto.moveTo(newskip[0],newskip[1],0)
                else:
                    auto.move(0-calldifference,0)

        
        
        
        elif kb.is_pressed('right'):
            if auto.position()[1] == newpoint0[1]:
                if auto.position()[0] == newpoint0[0]+(13*tiledifference):
                    auto.moveTo(newpoint0[0],newpoint0[1],0)
                else:
                    auto.move(tiledifference,0)

            elif auto.position()[1] == newskip[1]:
                if auto.position()[0] == newskip[0]:
                    auto.moveTo(newskip[0]-calldifference,newskip[1],0)
                else:
                    auto.move(calldifference,0)
        
        elif kb.is_pressed('up'):
            if auto.position()[1] == newskip[1]:
                auto.moveTo(newpoint0[0],newpoint0[1],0)
            else:
                auto.moveTo(newskip[0],newskip[1],0)
        
        elif kb.is_pressed('down'):
            if auto.position()[1] == newpoint0[1]:
                auto.moveTo(newskip[0],newskip[1],0)
            else:
                auto.moveTo(newpoint0[0],newpoint0[1],0)    
        
        
        
        elif kb.is_pressed('z'):
            auto.click()
    else:
        pass