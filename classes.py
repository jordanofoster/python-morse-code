import winsound, time

class dictConstructor:
    def __init__(self, sourceTuple):
        self._sourceTuple = sourceTuple
        self._alnumLookupDict = self._constructDict(0,1)
        self._morseLookupDict = self._constructDict(1,0)
    
    def updateLookupDicts(self, sourceTuple):
        self.__init__(sourceTuple)

    def _constructDict(self, key, value):
        constructedDict = {}
        for element in self._sourceTuple:
            constructedDict.update({self._sourceTuple[self._sourceTuple.index(element)][key]:self._sourceTuple[self._sourceTuple.index(element)][value]})
        return constructedDict
    
    def alnumLookup(self, morseStr):
        return self._alnumLookupDict.get(morseStr)
    
    def morseLookup(self, morseStr):
        return self._morseLookupDict.get(morseStr)

class transcriptor():
    def __init__(self, morseStandard):
        self._morseStandard = morseStandard
    
    def updateMorseStandard(self, newMorseStandard):
        self.__init__(newMorseStandard)

    def toMorse(self, plaintext):
        #TODO: handle non-alnumeric plaintexts
        plaintext = plaintext.upper().split()
        tempDict = dictConstructor(self._morseStandard)
        morseCode = []
        for word in plaintext:
            for letter in word:
                morseCode.append(" " + tempDict.get(letter) + " ")
            if plaintext.index(word) != len(plaintext):
                morseCode.append("|")
        return ("".join(morseCode)).strip()
    
    def toAlnum(self, morse):
        tempDict = dictConstructor(self._morseStandard)
        charList = []
        message = morse.split()
        for character in message:
            if character != "|":
                charList.append(tempDict.get(character))
            elif character == "|":
                charList.append(" ")
        return ("".join(charList)).strip()

class morseConfigurator():
    def __init__(self, dotLength, morseFrequency):
        self.dotLength = dotLength
        self.morseFrequency = morseFrequency

        self._dashLength = self.dotLength*3
        self._dotDashInterval = self.dotLength/1000
        self._letterInterval = self._dotDashInterval*3
        self._wordInterval = self._dotDashInterval*7
    
    def returnConfig(self):
        return self.dotLength, self.morseFrequency, self._dashLength, self._dotDashInterval, self._letterInterval,

    def setFrequency(self, morseFrequency):
        self.morseFrequency = morseFrequency

    def setNewConfig(self, dotLength, morseFrequency):
        self.__init__(dotLength, morseFrequency)

class morsePlayer(morseConfigurator):

    def playMorseFromFile(self, filename, encoding):
        fileToPlay = open(filename, "rt")
        if encoding == "morse":
            for morseMsg in fileToPlay.readlines():
                self.playFromMorse(morseMsg)
        elif encoding == "alnumeric":
            for alnumMsg in fileToPlay.readlines():
                self.playFromText(alnumMsg)
        else:
            raise Exception("EncodingMismatchException")

    def playFromMorse(self, morseCode):
        if morseCode.isalnum() == True:
            raise Exception("InvalidEncodingMethodException")
        else:
            for x in morseCode:
                if x == "|":
                    time.sleep(self._wordInterval)
                elif x == " ":
                    time.sleep(self._letterInterval)
                elif x == ".":
                    winsound.Beep(self.morseFrequency, self.dotLength)
                    time.sleep(self._dotDashInterval)
                elif x == "-":
                    winsound.Beep(self.morseFrequency, self._dashLength)
                    time.sleep(self._dotDashInterval)
    
    def playFromText(self, plaintext):
        self.playFromMorse(transcriptor.toMorse(plaintext))

    def loopMorse(self, morseCode, loopNum):
        print(("Looping morse code [{}], signalling the following plaintext: [{}]").format(morseCode,transcriptor.toAlnum(morseCode)))
        if loopNum == 0:
            try:
                print("Looping endlessly... [Press ^C to quit]")
                while True:
                    self.playFromMorse(morseCode)
            except KeyboardInterrupt:
                return
        else:
            for i in range(0,loopNum):
                print(("Loop number {}/{}").format(i+1,loopNum))
                self.playFromMorse(morseCode)

    def loopAlnum(self, plaintext, loopNum):
        self.loopMorse(transcriptor.toMorse(plaintext), loopNum)