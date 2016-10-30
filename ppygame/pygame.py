from graphics import *

def main():
    window = GraphWin("my window", 900, 600)
    
    myList = []
    textFile = open("data.txt")
    fileContent = textFile.read()
#    print fileContent
    numberData = fileContent.split("\r\n")
#    print len(numberData)


    #creating Y data array
    yDataArray = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    directionArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    linesDrawn = []
    shapesDrawn = []
    
#    line2 = Line(Point(20,500), Point(20,100))
#    line2.draw(window)
    
    
    
    
    x = 30
    xOffset = 30
    y = 20
    bottomY = 600
    minY = 20

    
    for i in range (len(numberData)):
        line1 = Line(Point(x,bottomY), Point(x,bottomY-y))
        line1.setFill("green")
        line1.draw(window)
        linesDrawn.append(line1)
        movingCircle = Circle(Point(x,bottomY-y), 4.5)
        movingCircle.setFill("white")
        movingCircle.setOutline("white")
        movingCircle.draw(window)
        shapesDrawn.append(movingCircle)
        
        myText = Text(Point(x, 40), str(numberData[i]))
        myText.setTextColor("black")
        myText.setSize(15)
        myText.draw(window)
        
        x = x + xOffset
    
        
    y = 20
    while True:
        x = 30
        for i in range (len(numberData)):
            y = yDataArray[i]
            maxY = int(numberData[i])*6
#            print directionArray[i]
            if ( y > maxY):
                y = maxY
                directionArray[i] = 1
                shapesDrawn[i].setFill("black")
                shapesDrawn[i].move(0,-maxY)
            if ( y < minY):
                y = minY
                directionArray[i] = 0
                moveY = 10
                howFar = 0
                while howFar < maxY:
                    howFar = howFar + 10
                    shapesDrawn[i].setFill("black")
                    shapesDrawn[i].move(0, moveY)
                shapesDrawn[i].setFill("white")
            
            
            
            
            
            if (directionArray[i] == 0):
                yDataArray[i] = yDataArray[i] + 10
                colour = "green"
            if (directionArray[i] == 1):
                yDataArray[i] = yDataArray[i] - 10
                colour = "red"
           

        
#            print y, maxY, directionArray[i]
            linesDrawn[i].undraw()
            line1 = Line(Point(x,bottomY), Point(x,bottomY-y))
            line1.setFill(colour)
            line1.draw(window)
            linesDrawn[i] = line1
            x = x + xOffset

            
    window.getMouse() # Pause to view result
    window.close()    # Close window when done

main()
   