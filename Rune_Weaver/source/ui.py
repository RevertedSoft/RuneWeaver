#Rune Weaver v. 0.01
#Copyright (c) 2013 - 2014 RevertedSoft <revertedsoft.com>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation file (the "Software"), to deal
#with the Software without limitation in the rights to use, copy, modify, merge
#publish, distribute, but NOT to sell copies of the Software, subject to the
#following condition:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

class Text():

    def __init__(self, text, position=(0,0)):

        self.text_ = text
        self.position = position

class UI():

    def __init__(self, position, size, surface, text=[], printBorder=False, borderColor=(0,255,0)):
        self.position = position
        self.size = size
        self.surface = surface
        self.text = text#must be passed as a text object
        print(self.text[0].text_)

        self.printBorder = printBorder
        self.borderColor = borderColor

    def printUI(self, position=(0,0), foregroundColor=(255,255,0),backgroundColor=(0,0,0)):
        self.printUIBorder(position)

        self.printString(position, foregroundColor, backgroundColor)
        
        

    def printString(self, position, foregroundColor, backgroundColor):
        for messages in self.text:
            #break the message text into a list of characters
            textList = list(messages.text_)
            #iterate i to move the x position of the message over 1 each cycle (to iterate through each character in string)
            i = 0
            for chars in textList:
                
                x = (messages.position[0] + i) + self.position[0] + position[0]
                y = (messages.position[1]) + self.position[1] + position[1]
                self.surface.putchar(str(chars), x, y, foregroundColor, backgroundColor)
                i += 1

    def printUIBorder(self, position=(0,0)):
        if self.printBorder:
            for x in range(self.position[0] + position[0], self.size[0] + self.position[0] + position[0]):
                for y in range(self.position[1] + position[1], self.size[1] + self.position[1] + position[1]):
                    if x == self.position[0] + position[0] or x == self.size[0] + self.position[0] + position[0] -1:
                        self.surface.putchar('|', x, y, self.borderColor, (0,0,0))
                    elif y == self.size[1] + self.position[1] + position[1] -1 or y == self.position[1] + position[1]:
                        self.surface.putchar('=', x, y, self.borderColor, (0,0,0))
                    

    def alterText(self, text):
        self.text = text



class Menu(UI):

    def __init__(self, position, size, surface, text=[], printBorder=False, borderColor=(0,255,0), uiControlList=[]):
        UI.__init__(self, position, size, surface, text, printBorder, borderColor)
        self.uiControlList = uiControlList

    def printMenu(self):
        self.printUI()

        for controllers in self.uiControlList:
            controllers.printController((self.position[0], self.position[1]))


class ScrollingDisplay(UI):

    def __init__(self, position, size, surface, text=[], printBorder=False, borderColor=(0,255,0), maxSize=100):
        #in this class, text can just be passed as a list of strings
        UI.__init__(self,position,size,surface,text,printBorder,borderColor)
        self.maxSize = maxSize #this will determine how many strings the dynamic display will keep in memory

    def printUI(self, foregroundColor=(0,255,0), backgroundColor=(0,0,0)):
        
        for i in range(len(self.text)-1, (len(self.text) - (self.size[1])), -1):
            if i > len(self.text) - (self.size[1] - 1):
                self.printString((self.position[0] + 1, self.position[1] + i - (len(self.text)) + self.size[1] - 1), self.text[i].text_, foregroundColor, backgroundColor)
                
        self.printUIBorder()

    def printString(self, position, string, foregroundColor=(0,255,0), backgroundColor=(0,0,0)):
        #string = string.text_
        #this method differs from the UI's base method as the position of the text is not given through the text attribute but is dynamically determined
        #break the message text into a list of characters
        textList = list(string)
        #iterate i to move the x position of the message over 1 each cycle (to iterate through each character in string)
        i = 0
        for chars in textList:
            x = position[0] + i
            y = position[1]
            self.surface.putchar(str(chars), x, y, foregroundColor, backgroundColor)
            i += 1

    def printToDisplay(self, text):
        #takes a list of strings to add to the current list
        if len(self.text) > self.maxSize:
            self.text = self.text[-(len(text) - self.maxSize):]

        self.text.append(Text(text))
            

class UIControls(UI):

    def __init__(self, position, size, surface, text=[], printBorder=True, borderColor=(0,255,0), backgroundColor=(0,0,0), foregroundColor=(255,255,255)):
        UI.__init__(self, position, size, surface, text, printBorder, borderColor)
        self.backgroundColor = backgroundColor
        self.foregroundColor = foregroundColor
        

    def printController(self, position):
        #later alter this to change the foreground color for mouse rollover
        self.printUI(position, self.foregroundColor, self.backgroundColor)


class Button(UIControls):

    def __init__(self, position, size, surface, text=[], printBorder=True, borderColor=(0,255,0), backgroundColor=(0,0,0), foregroundColor=(255,255,255), rolloverColor=(0,0,255), function=None):
        #pad white space to text
        if len(text[0].text_) < size[0]:
            spaceToAppend = ' ' * (size[0] - len(text[0].text_) - 2)
            text[0].text_ += (spaceToAppend)
            
            
        UIControls.__init__(self, position, size, surface, text, printBorder, borderColor, backgroundColor, foregroundColor)
        self.rolloverColor = rolloverColor
        self.function = function


class InputPrompt(UIControls):

    def __init__(self, position, size, surface, text=[], printBorder=False, borderColor=(0,0,0), backgroundColor=(0,0,0), foreGroundColor=(255,255,255)):

        UIControls.__init__(self, position, size, surface, text, printBorder, borderColor, backgroundColor, foreGroundColor)

        self.isActive = False#determines whether the player is currently trying to type to the input




    def typing(self, char):
        #if the input is active change the text according to events received
        #print(self.text.position)
        if char != "\b":
            self.text[0].text_ += char
        else:
            self.text[0].text_ = self.text[0].text_[:-1]



        
        
