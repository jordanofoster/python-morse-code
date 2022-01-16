DOT_LENGTH = 50
MORSE_FREQ = 500

DASH_LENGTH = DOT_LENGTH*3
DOT_DASH_INTERVAL = DOT_LENGTH/1000
LETTER_INTERVAL = DOT_DASH_INTERVAL*3
WORD_INTERVAL = DOT_DASH_INTERVAL*7

MORSE_ALNUM_TUPLE = ( #TODO: move this to seperate module, and allow the definition of different morse standards (perhaps from a file).
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

    #If "_", add empty string - this is used for the letters between a prosign, which require no pause between letters (removal of LETTER_INTERVAL).
    ("_", "")
)