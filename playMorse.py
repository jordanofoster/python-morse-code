import winsound, time, transcript

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
        self.playFromMorse(transcript.transcriptor.toMorse(plaintext))

    def loopMorse(self, morseCode, loopNum):
        print(("Looping morse code [{}], signalling the following plaintext: [{}]").format(morseCode,transcript.transcriptor.toAlnum(morseCode)))
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
        self.loopMorse(transcript.transcriptor.toMorse(plaintext), loopNum)