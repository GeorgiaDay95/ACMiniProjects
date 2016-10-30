from graphics import *

def main():
    window = GraphWin("my window", 900, 600)
    
    myList = []
    # adding text file into doc
    textFile = open("data.txt")
    #reading file
    fileContent = textFile.read()
#    print fileContent
#splitting
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

    # creating lines and dots and numbers to display on screen all offset by 30 in x direction
    for i in range (len(numberData)):
        line1 = Line(Point(x,bottomY), Point(x,bottomY-y))
        line1.setFill("green")
        line1.draw(window)
        linesDrawn.append(line1)
        movingCircle = Circle(Point(x,bottomY-y), 4.5)
        #make cirlces white (invisible)
        movingCircle.setFill("white")
        movingCircle.setOutline("white")
        movingCircle.draw(window)
        shapesDrawn.append(movingCircle)
        myText = Text(Point(x, 40), str(numberData[i]))
        score = int(numberData[i])
        #decing colour based on grade
        colour = "black"
        if (score > 0 and score < 50):
            colour = "red"
        if (score >= 50 and score < 60):
            colour = "orange"
        if (score >= 60 and score < 70):
            colour = "yellow"
        if (score >= 70):
            colour = "green"
        myText.setTextColor(colour)
        myText.setSize(15)
        myText.draw(window)
        # moving each one created next to each other on the screen
        x = x + xOffset
    
        
    y = 20
    while True:
        x = 30
        for i in range (len(numberData)):
            y = yDataArray[i]
            maxY = int(numberData[i])*6
#            print directionArray[i]
# if y is bigger than the height of each grade then change direction array
            if ( y > maxY):
                y = maxY
                directionArray[i] = 1
                # turn circles to black and move to top of line
                shapesDrawn[i].setFill("black")
                shapesDrawn[i].move(0,-maxY)
                #when lines hit bottom of the drop lines to bottom of screen
            if ( y < minY):
                y = minY
                directionArray[i] = 0
                moveY = 10
                howFar = 0
                while howFar < maxY:
                    #circles should drop by ten every time
                    howFar = howFar + 10
                    shapesDrawn[i].setFill("black")
                    shapesDrawn[i].move(0, moveY)
                shapesDrawn[i].setFill("white")
        
            # sorting out the direction of the lines
            if (directionArray[i] == 0):
                yDataArray[i] = yDataArray[i] + 10
                colour = "green"
            if (directionArray[i] == 1):
                yDataArray[i] = yDataArray[i] - 10
                colour = "red"
           

        
#            print y, maxY, directionArray[i]
#undraws line so that you can see when it is going bakc doen
            linesDrawn[i].undraw()
            line1 = Line(Point(x,bottomY), Point(x,bottomY-y))
            line1.setFill(colour)
            line1.draw(window)
            linesDrawn[i] = line1
            x = x + xOffset

            
    window.getMouse() # Pause to view result
    window.close()    # Close window when done

main()
   