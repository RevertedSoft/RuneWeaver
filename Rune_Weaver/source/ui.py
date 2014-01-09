#module contains the UI class which will feed info to the player

class UI():

    def __init__(self, position, size, surface, text=[], printBorder=False):
        self.position = position
        self.size = size
        self.surface = surface
        self.text = text#must be passed in as a list of tuples, first value to display the text, second to display the position(another tuple), position is relative to the ui's position

        self.printBorder = printBorder

    def printUI(self, position=(0,0), foregroundColor=(255,255,0),backgroundColor=(0,0,0)):
        if self.printBorder:
            self.printUIBorder(position)
        
        for messages in self.text:
            #break the message text into a list of characters
            textList = list(messages[0])
            #iterate i to move the x position of the message over 1 each cycle
            print(textList)
            i = 0
            for chars in textList:
                x = (messages[1][0] + i) + self.position[0] + position[0]
                y = (messages[1][1]) + self.position[1] + position[1]
                self.surface.putchar(str(chars), x, y, foregroundColor, backgroundColor)
                i += 1

    def printUIBorder(self, position=(0,0)):
        for x in range(self.position[0] + position[0], self.size[0] + self.position[0] + position[0]):
            for y in range(self.position[1] + position[1], self.size[1] + self.position[1] + position[1]):
                if x == self.position[0] + position[0] or x == self.size[0] + self.position[0] + position[0] -1:
                    self.surface.putchar('|', x, y, (0,255,0), (0,0,0))
                elif y == self.size[1] + self.position[1] + position[1] -1 or y == self.position[1] + position[1]:
                    self.surface.putchar('=', x, y, (0,255,0), (0,0,0))
                    

    def alterText(self, text):
        self.text = text



class Menu(UI):

    def __init__(self, position, size, surface, text=[], printBorder=False, uiControlList=[]):
        UI.__init__(self, position, size, surface, text, printBorder)
        self.uiControlList = uiControlList

    def printMenu(self):
        self.printUI()

        for controllers in self.uiControlList:
            print(controllers)
            print(controllers.text)
            controllers.printController((self.position[0], self.position[1]))
            print("printing button")
            #pass



class UIControls(UI):

    def __init__(self, position, size, surface, text=[], printBorder=True, backgroundColor=(0,0,0), foregroundColor=(255,255,255)):
        UI.__init__(self, position, size, surface, text, printBorder)
        self.backgroundColor = backgroundColor
        self.foregroundColor = foregroundColor
        

    def printController(self, position):
        #later alter this to change the foreground color for mouse rollover
        self.printUI(position, self.foregroundColor, self.backgroundColor)


class Button(UIControls):

    def __init__(self, position, size, surface, text=[], printBorder=True, backgroundColor=(0,0,0), foregroundColor=(255,255,255), rolloverColor=(0,0,255), function=None):
        #pad white space to text
        if len(text[0][0]) < size[0]:
            spaceToAppend = ' ' * (size[0] - len(text[0][0]) - 2)
            print("here to" + spaceToAppend + "here")
            text[0][0] += (spaceToAppend)
            
            
        UIControls.__init__(self, position, size, surface, text, printBorder, backgroundColor, foregroundColor)
        self.rolloverColor = rolloverColor
        self.function = function
