from graphics import *

def main():
    window = GraphWin("my window", 850, 500)
    
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
    
#    line2 = Line(Point(20,500), Point(20,100))
#    line2.draw(window)
    
    x = 30
    xOffset = 30
    y = 20
    bottomY = 500
    minY = 20
    
    for i in range (len(numberData)):
        line1 = Line(Point(x,bottomY), Point(x,bottomY-y))
        line1.setFill("green")
        line1.draw(window)
        linesDrawn.append(line1)
        x = x + xOffset
    y = 20
    while True:
        x = 30
        xOffset = 30
        bottomY = 500
        for i in range (len(numberData)):
            y = yDataArray[i]
            maxY = int(numberData[i])*6
#            print directionArray[i]
            if (directionArray[i] == 0):
                yDataArray[i] = yDataArray[i] + 10
                colour = "green"
            if (directionArray[i] == 1):
                yDataArray[i] = yDataArray[i] - 10
                colour = "red"
                   
            if ( y >= maxY):
                directionArray[i] = 1
            if ( y <= minY):
                directionArray[i] = 0

        
#            print y, maxY, directionArray[i]
            linesDrawn[i].undraw()
            line1 = Line(Point(x,bottomY), Point(x,bottomY-y))
            line1.setFill(colour)
            line1.draw(window)
            linesDrawn[i] = line1
            x = x + xOffset

#    
#    
#    keyPressedG = True
#    while (keyPressedG == True):
#        line1 = Line(Point(20,500), Point(20,200))
#        line1.draw(window)
#        time.sleep(3000)
#        line1 = Line(Point(20,500), Point(20,400))
#        line1.draw(window)
#        
#    
    
    window.getMouse() # Pause to view result
    window.close()    # Close window when done

main()


    
#    for results in fileContent:
#        myList.append(int(results))
#        
#    textFile.close()
#    myResults = Text(Point(425, 470), myList)
#    myResults.setSize(20)
#    myResults.draw(window)
#    
#    