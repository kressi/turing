
BLANK = "#"


class Tape:
    def __init__(self, inputTape=""):
        self.__frontStack = []
        self.__endStack = []
        for s in inputTape:
            self.__endStack.append(s)
        self.__endStack.reverse()
        if self.__endStack:
            self.__current = self.__endStack.pop()
        else:
            self.__current = BLANK
            
    def current(self, *s):
        if s:
            self.__current = s[0]
        return self.__current
        
    def left(self, s):
        if self.__endStack or s != BLANK:
            self.__endStack.append(s)
        if self.__frontStack:
            self.__current = self.__frontStack.pop()
        else:
            self.__current = BLANK
        return self.__current
        
    def right(self, s):
        if self.__frontStack or s != BLANK:
            self.__frontStack.append(s)
        if self.__endStack:
            self.__current = self.__endStack.pop()
        else:
            self.__current = BLANK
        return self.__current
    
    def getCount(self, string='0'):
        count = self.__frontStack.count(string) + self.__endStack.count(string)
        if string == self.__current:
            count += 1
        return count
    
    def show(self):
        return (" ".join(self.__frontStack[:15]) or " ") + "[" + self.__current + "]" + " ".join(self.__endStack[15::-1])

class TuringMachine:
    def __init__(self,
                 tapesInput=[""],
                 initState=0,
                 transitions={},
                 tapeCount=1):
        self.__state = initState
        self.__transitions = transitions
        self.__stepCount = 0L
        self.__next = ""
        self.__tapes = []
        for t in tapesInput:
            self.__tapes.append(Tape(t))
        if tapeCount > len(self.__tapes):
            for _ in range(len(self.__tapes), tapeCount):
                self.__tapes.append(Tape())

    def __repr__(self):
        representation = "state: {s}  step: {c}\n".format(s=self.__state, c=self.__stepCount)
        for t in self.__tapes:
            representation += t.show()
            representation += '\n'
        return representation

    def getCount(self, string='0'):
        count = []
        for t in self.__tapes:
            count.append(t.getCount(string))
        return count

    def getStepCount(self):
        return self.__stepCount

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
            for tape, value, direction in zip(self.__tapes,
                                              trans[1][:len(trans[1])/2],
                                              trans[1][len(trans[1])/2:]):
                if direction == "R":
                    self.__next += tape.right(value)
                elif direction == "L":
                    self.__next += tape.left(value)
                else:
                    self.__next += tape.current(value)
            return True
        else:
            return False

