import winsound, time, argparse

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

DOT_LENGTH = 100
MORSE_FREQ = 500

DASH_LENGTH = DOT_LENGTH*3
DOT_DASH_INTERVAL = DOT_LENGTH/1000
LETTER_INTERVAL = DOT_DASH_INTERVAL*3
WORD_INTERVAL = DOT_DASH_INTERVAL*7

alnumToMorseDict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

def playFromMorse(morseCode):
    for x in morseCode:
        if x == "/":
            time.sleep(WORD_INTERVAL)
        elif x == " ":
            time.sleep(LETTER_INTERVAL)
        elif x == ".":
            winsound.Beep(MORSE_FREQ, DOT_LENGTH)
            time.sleep(DOT_DASH_INTERVAL)
        elif x == "-":
            winsound.Beep(MORSE_FREQ, DASH_LENGTH)
            time.sleep(DOT_DASH_INTERVAL)

def transcriptToMorse(plaintext):
    #TODO: handle non-alnumeric plaintexts
    plaintext = plaintext.upper().split()
    morseCode = []
    for word in plaintext:
        for letter in word:
            morseCode.append(alnumToMorseDict.get(letter))
            morseCode.append(" ")
        if plaintext.index(word) != len(plaintext)-1:
            morseCode.append("/")
    return ("".join(morseCode)).strip()
    
def playFromText(plaintext):
    playFromMorse(transcriptToMorse(plaintext))

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
            playFromMorse(morseCode + "/")
    else:
        for i in range(0,loopNum):
            print(("Loop number {}/{}").format(i+1,loopNum))
            playFromMorse(morseCode + "/")

loopMorse(transcriptToMorse("SOS"), 10, originalMsg="SOS")