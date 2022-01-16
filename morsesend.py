import argparse

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

DOT_LENGTH = 50
MORSE_FREQ = 500

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