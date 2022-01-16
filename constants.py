#Tuples:
#These are tuples containing the standard morse code 'alphabets' that are in use.
#TODO: allow the definition of different morse standards (perhaps from a file).

ITU_R_M_1677_1 = ( # Tuple that represents Internation Morse Code, as defined in Recommendation ITU-R M.1677-1 (10/2009).
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
    (".", ".-.-.-"),
    (",", "--..--"),
    (":", "---..."),
    ("?", "..--.."),
    ("'", ".----."),
    ("-", "-....-"),
    ("/", "-..-."),
    ("(", "-.--."),
    (")", "-.--.-"),
    ("\"", ".-..-."),
    ("=", "-...-"),
    ("+", ".-.-."),
    ("@", ".--.-."),
    #Prosigns:
    ("<Understood>", "...-.")
    ("<Error>", "........")
    #("<Invitation to transmit>", "-.-") # Included in spec, but equivalent to 'K' so left out here.
    ("<Wait>", ".-...")
    ("<End of Work>", "...-.-")
    ("<Starting Signal>", "-.-.-")
    
    #If "_", add empty string - this is used for the letters between a prosign, which require no pause between letters (removal of letter interval).
    ("_", "")
)