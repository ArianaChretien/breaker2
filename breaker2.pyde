xCoordinate = random (50, 200)
yCoordinate = random (50, 200)
ySpeed = 3
xSpeed = 5
brick1 = True
brick2 = True
brick3 = True
brick4 = True
brick5 = True
brick6 = True
brick7 = True
brick8 = True
brick9 = True
brick10 = True

ellipseSize = 20

def setup ():
    size(800, 800)
    
def draw():
    background(0, 0, 0)
    if brick1:
        fill(0, 156, 159)
    else: 
        fill(0, 0, 0)
    rect(0, 0, 80, 30) #brick 1
    if brick2:
        fill(255, 102, 204)
    else:
        fill(0, 0, 0)
    rect(80, 0, 80, 30)#brick 2
    if brick3:
        fill(0, 102, 0)
    else:
        fill(0, 0, 0)
    rect(160, 0, 80, 30)#brick 3
    if brick4:
        fill(102, 0, 255)
    else:
        fill(0, 0, 0)
    rect(240, 0 , 80, 30)#brick 4
    if brick5:
        fill(255, 204, 0)
    else:
        fill(0, 0, 0)
    rect(240, 0 , 80, 30)#brick 5
    if brick6:
        fill(255, 153, 0)
    else:
        fill(0, 0, 0)
    rect(400, 0, 80, 30)#brick 6
    if brick7:
        fill(255, 0, 0)
    else:
        fill(0, 0, 0)
    rect(480, 0, 80, 30)#brick 7
    if brick8:
        fill(153, 255, 102)
    else:
        fill(0, 0, 0)
    rect(560, 0, 80, 30)#brick 8
    if brick9:
        fill(0, 204, 255)
    else:
        fill(0, 0, 0)
    rect(640, 0, 80, 30)#brick 9
    if brick10:
        fill(204, 153, 255)
    else:
        fill(0, 0, 0)
    rect(720, 0, 80, 30) #end of bricks
    fill(255, 255, 255) # color of paddle
    rect(mouseX, 790, 80, 10, 80) #this is the paddle
    
    if yCoordinate <= 40:
       if xCoordinate>=0 and xCoordinate <80: #1
           brick1 = False
           fill (0, 0, 0)
           #rect(0, 0, 80, 30)
       if xCoordinate > 80 and xCoordinate <= 160:#2
           brick2 = False
           fill(0, 0, 0)
           rect(80, 0, 80, 30)
       if xCoordinate > 160 and xCoordinate <= 240:#3
           brick3 = False
           fill(0, 0, 0)
           rect(160, 0, 80, 30)
       if xCoordinate >240 and xCoordinate <= 320:#4
           brick4 = False
           fill(0, 0, 0)
           rect(240, 0 , 80, 30)
       if xCoordinate >320 and xCoordinate <= 400:#5
           brick5 = False
           fill(0, 0, 0)
           rect(240, 0 , 80, 30)
       if xCoordinate >400 and xCoordinate <= 480:#6
           brick6 = False
           fill(0, 0, 0)
           rect(400, 0, 80, 30)
       if xCoordinate >480 and xCoordinate <= 560:#7
           brick7 = False
           fill(0, 0, 0)
           rect(480, 0, 80, 30)
       if xCoordinate >560 and xCoordinate <= 640:#8
           brick8 = False
           fill(0, 0, 0)
           rect(560, 0, 80, 30)
       if xCoordinate >640 and xCoordinate <= 720:#9
           brick9 = False
           fill(0, 0, 0)
           rect(640, 0, 80, 30)
       if xCoordinate >720 and xCoordinate <= 800:#10
           brick10 = False
           fill(0, 0, 0)
           rect(204, 153, 255)
    
       
       
    
    r = random (50, 400)
    global xCoordinate, yCoordinate, xSpeed, ySpeed, ellipseSize
    topBoundary = ellipseSize / 2+30
    bottomBoundary =800 - ellipseSize /2
    
    leftBoundary = ellipseSize / 2
    rightBoundary =800 - ellipseSize /2
    
    if yCoordinate >= bottomBoundary or yCoordinate <= topBoundary:
      ySpeed = -ySpeed  
    
    if xCoordinate >= rightBoundary or xCoordinate <= leftBoundary:
       xSpeed =-xSpeed
    
    yCoordinate += ySpeed
    xCoordinate += xSpeed
    noStroke()
    fill(0,255,0)
    ellipse (xCoordinate, yCoordinate, ellipseSize, ellipseSize)
