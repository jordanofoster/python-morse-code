import winsound 
import time

class DictConstructor:
    def __init__(self, sourceTuple):
        self._sourceTuple = sourceTuple
        self._alnumLookupDict = self._construct_dict(0,1) # Alum:Morse
        self._morseLookupDict = self._construct_dict(1,0) # Morse:Alnum
    
    def update_lookup_dicts(self, sourceTuple):
        self.__init__(sourceTuple)

    def _construct_dict(self, key, value):
        constructedDict = {}
        for element in self._sourceTuple:
            xVal = self._sourceTuple[self._sourceTuple.index(element)] # Current elememnt position of unnested (x) tuple
            constructedDict.update({xVal[key]:xVal[value]}) #Update with key, value from nested tuple
        return constructedDict
    
    def alnum_lookup(self, alnumStr):
        return self._alnumLookupDict.get(alnumStr)
    
    def morse_lookup(self, morseStr):
        return self._morseLookupDict.get(morseStr)

class Transcriptor():
    def __init__(self, morseStandard):
        self._morseStandard = morseStandard
    
    def update_morse_standard(self, newMorseStandard):
        self.__init__(newMorseStandard)

    def to_morse(self, plaintext):
        #TODO: handle non-alnumeric plaintexts
        plaintext = plaintext.upper().split()
        tempDict = DictConstructor(self._morseStandard)
        morseCode = []
        for word in plaintext:
            for letter in word:
                morseCode.append(" " + tempDict.get(letter) + " ")
            if plaintext.index(word) != len(plaintext):
                morseCode.append("|")
        return ("".join(morseCode)).strip()
    
    def to_alnum(self, morse):
        if morse.isalnum() == True:
            raise Exception("NonMorseInput")
        tempDict = DictConstructor(self._morseStandard)
        charList = []
        message = morse.split()
        for character in message:
            if character != "|":
                charList.append(tempDict.get(character))
            elif character == "|":
                charList.append(" ")
        return ("".join(charList)).strip()

class MorseConfigurator():
    def __init__(self, dotLength, morseFrequency):
        self.dotLength = dotLength
        self.morseFrequency = morseFrequency

        self._dashLength = self.dotLength*3
        self._dotDashInterval = self.dotLength/1000
        self._letterInterval = self._dotDashInterval*3
        self._wordInterval = self._dotDashInterval*7
    
    def return_config(self):
        return self.dotLength, self.morseFrequency, self._dashLength, self._dotDashInterval, self._letterInterval,

    def set_freq(self, morseFrequency):
        self.morseFrequency = morseFrequency

    def set_config(self, dotLength, morseFrequency):
        self.__init__(dotLength, morseFrequency)

class MorsePlayer(MorseConfigurator):

    def play_morse_from_file(self, filename, encoding):
        fileToPlay = open(filename, "rt")
        if encoding == "morse":
            for morseMsg in fileToPlay.readlines():
                self.playFromMorse(morseMsg)
        elif encoding == "alnumeric":
            for alnumMsg in fileToPlay.readlines():
                self.playFromText(alnumMsg)
        else:
            raise Exception("EncodingMismatchException")

    def play_sound_from_morse(self, morseCode):
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
    
    def play_sound_from_plaintext(self, plaintext):
        self.playFromMorse(Transcriptor.toMorse(plaintext))

    def loop_morse(self, morseCode, loopNum):
        print(("Looping morse code [{}], signalling the following plaintext: [{}]").format(morseCode,Transcriptor.toAlnum(morseCode)))
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

    def loop_alnum(self, plaintext, loopNum):
        self.loopMorse(Transcriptor.toMorse(plaintext), loopNum)
