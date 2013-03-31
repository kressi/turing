class Config:
    blank = "#"


class Tape:
    """Initial position on the leftmost element."""
    
    def __init__(self, inputTape=""):
        self.__frontStack = []
        self.__endStack = []
        for s in inputTape:
            self.__endStack.append(s)
        self.__endStack.reverse()
        if self.__endStack:
            self.__current = self.__endStack.pop()
        else:
            self.__current = Config.blank
            
    def current(self, *s):
        if s:
            self.__current = s[0]
        return self.__current
        
    def left(self, s):
        if self.__endStack or s != Config.blank:
            self.__endStack.append(s)
        if self.__frontStack:
            self.__current = self.__frontStack.pop()
        else:
            self.__current = Config.blank
        return self.__current
        
    def right(self, s):
        if self.__frontStack or s != Config.blank:
            self.__frontStack.append(s)
        if self.__endStack:
            self.__current = self.__endStack.pop()
        else:
            self.__current = Config.blank
        return self.__current
        
    def show(self):
        return " ".join(self.__frontStack) + "[" + self.__current + "]" +(" ".join(self.__endStack)[::-1])


class TuringMachine:
    def __init__(self, tapesInput=[""], initState=0, transitions={}, tapeCount=1):
        self.__state = initState
        self.__transitions = transitions
        self.__stepCount = 0L
        self.__next = ""
        self.__tapes = []
        for t in tapesInput:
            self.__tapes.append(Tape(t))
        if tapeCount > len(self.__tapes):
            for i in range(len(self.__tapes), tapeCount):
                self.__tapes.append(Tape())

    def show(self):
        print "state: {s}  step: {c}".format(s=self.__state, c=self.__stepCount)
        for t in self.__tapes:
            print t.show()

    def step(self):
        if self.__next == "":
            self.__next = "{0}-".format(self.__state)
            for t in self.__tapes:
                self.__next += t.current()
        if self.__next in self.__transitions:
            self.__stepCount += 1
            trans = self.__transitions[self.__next].split("-")
            self.__state = trans[0]
            self.__next = "{0}-".format(self.__state)
            values = trans[1][:len(trans[1])/2]
            directions = trans[1][len(trans[1])/2:]
            for i in range(len(values)):
                if directions[i] == "R":
                    self.__next += self.__tapes[i].right(values[i])
                elif directions[i] == "L":
                    self.__next += self.__tapes[i].left(values[i])
                else:
                    self.__next += self.__tapes[i].current(values[i])
            return True
                
        else:
            return False

