#module contains the UI class which will feed info to the player

class UI():

    def __init__(self, position, size, surface, text=[], printBorder=False):
        self.position = position
        self.size = size
        self.surface = surface
        self.text = text#must be passed in as a list of tuples, first value to display the text, second to display the position(another tuple), position is relative to the ui's position

        self.printBorder = printBorder

    def printUI(self):
        if self.printBorder:
            for x in range(self.position[0], self.size[0] + self.position[0]):
                for y in range(self.position[1], self.size[1] + self.position[1]):
                    if x == self.position[0] or x == self.size[0] + self.position[0] -1:
                        self.surface.putchar('|', x, y, (0,255,0), (0,0,0))
                    elif y == self.size[1] + self.position[1] -1 or y == self.position[1]:
                        self.surface.putchar('=', x, y, (0,255,0), (0,0,0))

        
        for messages in self.text:
            #break the message text into a list of characters
            textList = list(messages[0])
            #iterate i to move the x position of the message over 1 each cycle
            print(textList)
            i = 0
            for chars in textList:
                x = (messages[1][0] + i) + self.position[0]
                y = (messages[1][1]) + self.position[1]
                self.surface.putchar(str(chars), x, y, (255,255,0), (0,0,0))
                i += 1

    def alterText(self, text):
        self.text = text
            




class Menu(UI):

    def __init__(self, position, size, surface, text, printBorder=False, uiControlList = {}):
        UI.__init__(self, position, size, printBorder)
        self.uiControlList = uiControlList



class UIControls():

    def __init__(self, text, position, size, surface):
        self.text = text
        self.position = position
        self.size = size
        self.surface = surface


class Button(UIControls):

    def __init__(self, text, position, size, surface, function):
        UIControls.__init__(self, text, position, size)
        self.function = function
