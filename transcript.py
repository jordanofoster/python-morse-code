import morseDict

class transcriptor():
    def __init__(self, morseStandard):
        self._morseStandard = morseStandard
    
    def updateMorseStandard(self, newMorseStandard):
        self.__init__(newMorseStandard)

    def toMorse(self, plaintext):
        #TODO: handle non-alnumeric plaintexts
        plaintext = plaintext.upper().split()
        tempDict = morseDict.dictConstructor(self._morseStandard)
        morseCode = []
        for word in plaintext:
            for letter in word:
                morseCode.append(" " + tempDict.get(letter) + " ")
            if plaintext.index(word) != len(plaintext):
                morseCode.append("|")
        return ("".join(morseCode)).strip()
    
    def toAlnum(self, morse):
        tempDict = morseDict.dictConstructor(self._morseStandard)
        charList = []
        currentWord = ""
        message = morse.split()
        for character in message:
            if character != "|":
                charList.append(tempDict.get(character))
            elif character == "|":
                charList.append(" ")
        return ("".join(charList)).strip()