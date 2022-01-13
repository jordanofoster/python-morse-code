import winsound, time, argparse

#parser = argparse.ArgumentParser(description="Processes arguments for morsecode program.")
#parser.add_argument('-m', '--mode', choices=['receive','transmit'])
#parser.add_argument('-ms','--unit', type=int, metavar="milliseconds", required=True)
#parser.add_argument('-hz','--freq', type=int, metavar="hertz", choices=range(37,32767), required=True)
#parser.add_argument('-'))
#output = parser.add_mutually_exclusive_group(required=True)
#output.add_argument('-fo', '--tofile', type=argparse.FileType('w'))
#output.add_argument('-so','--tosound',)

#args = parser.parse_args(args=['receive','transmit','unit','freq','-fi','-ai','-mi','-fo','-so'])
#print(args)

DIT_LENGTH = int(input("DIT LENGTH (MS): "))
MORSE_FREQ = int(input("MORSE FREQ (HZ): "))

DAH_LENGTH = DIT_LENGTH*3
DIT_DAH_INTERVAL = DIT_LENGTH/1000
LETTER_INTERVAL = DIT_DAH_INTERVAL*3
WORD_INTERVAL = DIT_DAH_INTERVAL*7

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
        if x == " ":
            time.sleep(WORD_INTERVAL)
        elif x == "|":
            time.sleep(LETTER_INTERVAL)
        elif x == ".":
            winsound.Beep(MORSE_FREQ, DIT_LENGTH)
            time.sleep(DIT_DAH_INTERVAL)
        elif x == "-":
            winsound.Beep(MORSE_FREQ, DAH_LENGTH)
            time.sleep(DIT_DAH_INTERVAL)

def playFromAlphaNum(alphaNum):
    alphaNum = alphaNum.upper()
    for x in alphaNum:
        if x.isalnum():
            playFromMorse(alnumToMorseDict.get(x) + "|")
        else:
            playFromMorse(" ")

def playMorseFromFile(filename):
    fileToPlay = open(filename, "rt")
    for morseMsg in fileToPlay.readlines():
        playFromMorse(morseMsg)