import winsound, time, argparse, constants

#parser = argparse.ArgumentParser(description="Processes arguments for morsecode program.")
#parser.add_argument('-u','--unit', type=int, nargs=1, default=100, required=True)
#parser.add_argument('-hz','--hertz', type=int, nargs=1, default=500, required=True)
#parser.add_argument('--inputType', type=ascii, nargs=1, choices=['alphanumeric','morse','file'], default='morse')
#parser.add_argument('--input', nargs=1, type=ascii)
#output = parser.add_mutually_exclusive_group()
#output.add_argument('-fo', '--tofile', type=argparse.FileType('w'))
#output.add_argument('-so','--tosound', type=

#a = parser.parse_args(['-u', 'unit', '-hz', 'hertz'])
#output = output.parse_args()
#print(a)
#print(output)

class morseInterval():
    def __init__(self, dotLength, morseFrequency):
        self.dotLength = dotLength
        self.morseFrequency = dotLength


DOT_LENGTH = 50
MORSE_FREQ = 500

DASH_LENGTH = DOT_LENGTH*3
DOT_DASH_INTERVAL = DOT_LENGTH/1000
constants.LETTER_INTERVAL = DOT_DASH_INTERVAL*3
constants.WORD_INTERVAL = DOT_DASH_INTERVAL*7

constants.MORSE_ALNUM_TUPLE = ( #TODO: move this to seperate module, and allow the definition of different morse standards (perhaps from a file).
    #Letters:
    ("A", ".-"),
    ("B", "-..."),
    ("C", "-.-."),
    ("D", "-.."),
    ("E", "."),
    ("F", "..-."),
    ("G", "--."),
    ("H", "...."),
    ("I", ".."),
    ("J", ".---"),
    ("K", "-.-"),
    ("L", ".-.."),
    ("M", "--"),
    ("N", "-."),
    ("O", "---"),
    ("P", ".--."),
    ("Q", "--.-"),
    ("R", ".-."),
    ("S", "..."),
    ("T", "-"),
    ("U", "..-"),
    ("V", "...-"),
    ("W", ".--"),
    ("X", "-..-"),
    ("Y", "-.--"),
    ("Z", "--.."),
    #Numbers:
    ("0", "-----"),
    ("1", ".----"),
    ("2", "..---"),
    ("3", "...--"),
    ("4", "....-"),
    ("5", "....."),
    ("6", "-...."),
    ("7", "--..."),
    ("8", "---.."),
    ("9", "----."),
    #Punctuation:
    #"Error": "........",
    ("&", ".-..."),
    ("'", ".----."),
    ("@", ".--.-."),
    (")", "-.--.-"),
    ("(", "-.--."),
    (":", "---..."),
    (",", "--..--"),
    ("=", "-...-"),
    #Exclamation mark not in ITU-R
    ("!", "-.-.--"),
    (".", ".-.-.-"),
    ("-", "-....-"),
    #("%", "----- -..-. -----"), #This is '0/0' in morse. #TODO: implement this somehow (morse-to-alnum).
    ("+", ".-.-."),
    ("\"", ".-..-."),
    ("?", "..--.."),
    ("/", "-..-."),

    #If "_", add empty string - this is used for the letters between a prosign, which require no pause between letters (removal of constants.LETTER_INTERVAL).
    ("_", "")
)

class dictConstructor:
    def constructAlnumLookupDict(): # Make a dictionary with alnumeric as key, morse as value
        alnumLookupDict = {}
        for element in constants.constants.MORSE_ALNUM_TUPLE: # 0 is letter, 1 is morse - enters dictionary as {0:1}
            alnumLookupDict.update({constants.MORSE_ALNUM_TUPLE[constants.MORSE_ALNUM_TUPLE.index(element)][0]:constants.MORSE_ALNUM_TUPLE[constants.MORSE_ALNUM_TUPLE.index(element)][1]})
        return alnumLookupDict
    
    def constructMorseLookupDict(): # Make a dictionary with morse as key, alnumeric as value
        morseLookupDict = {}
        for element in constants.MORSE_ALNUM_TUPLE: # enters dictionary as {1:0} this time
            morseLookupDict.update({constants.MORSE_ALNUM_TUPLE[constants.MORSE_ALNUM_TUPLE.index(element)][1]:constants.MORSE_ALNUM_TUPLE[constants.MORSE_ALNUM_TUPLE.index(element)][0]})
        return morseLookupDict

    #TODO: can probably merge these functions into one

class transcriptor():
    def toMorse(plaintext):
        #TODO: handle non-alnumeric plaintexts
        plaintext = plaintext.upper().split()
        lookupDict = dictConstructor.constructAlnumLookupDict()
        morseCode = []
        for word in plaintext:
            for letter in word:
                morseCode.append(" " + lookupDict.get(letter) + " ")
            if plaintext.index(word) != len(plaintext):
                morseCode.append("|")
        return ("".join(morseCode)).strip()
    
    def toAlnum(morse):
        lookupDict = dictConstructor.constructMorseLookupDict()
        charList = []
        currentWord = ""
        message = morse.split()
        for character in message:
            if character != "|":
                charList.append(lookupDict.get(character))
            elif character == "|":
                charList.append(" ")
        return ("".join(charList)).strip()
                
def playFromMorse(morseCode):
    if morseCode.isalnum() == True:
        raise Exception("InvalidEncodingMethod")
    else:
        for x in morseCode:
            if x == "|":
                time.sleep(constants.WORD_INTERVAL)
            elif x == " ":
                time.sleep(constants.LETTER_INTERVAL)
            elif x == ".":
                winsound.Beep(MORSE_FREQ, DOT_LENGTH)
                time.sleep(DOT_DASH_INTERVAL)
            elif x == "-":
                winsound.Beep(MORSE_FREQ, DASH_LENGTH)
                time.sleep(DOT_DASH_INTERVAL)
    
def playFromText(plaintext):
    playFromMorse(transcriptor.transcriptToMorse(plaintext))

def playMorseFromFile(filename, encoding):
    fileToPlay = open(filename, "rt")
    if encoding == "morse":
        for morseMsg in fileToPlay.readlines():
            playFromMorse(morseMsg)
    elif encoding == "alnumeric":
        for alnumMsg in fileToPlay.readlines():
            playFromText(alnumMsg)
    else:
        return 0

def loopMorse(morseCode, loopNum=0, originalMsg="UNDEFINED"):
    print(("Looping morse code [{}], signalling the following plaintext: [{}]").format(morseCode,originalMsg))
    if loopNum == 0:
        print("Looping endlessly... [Press ^C to quit]")
        while True:
            playFromMorse(morseCode + "|")
    else:
        for i in range(0,loopNum):
            print(("Loop number {}/{}").format(i+1,loopNum))
            playFromMorse(morseCode + "|")

def freeInput(mode="morse"):
    if (mode != "morse") and (mode != "alnumeric"):
        raise Exception("UnknownEncodingMethod")
    else:
        while True:
            transmissionMsg = input("Enter the next message to transmit. [^C to exit]\n")
            if mode == "morse":
                playFromMorse(transmissionMsg)
            elif mode == "alnumeric":
                playFromText(transmissionMsg)