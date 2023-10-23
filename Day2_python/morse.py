class MorseCodeTranslator:
    def __init__(self):
        self.morse_dict = {
             ".-": "A"
            ,
            "-...": "B"
            ,
            "-.-.": "C"
            ,
            "-..": "D"
            ,
            ".": "E"
            ,
            "..-.": "F"
            ,
            "--.": "G"
            ,
            "....": "H"
            ,
            "..": "I"
            ,
            ".---": "J"
            ,
            "-.-": "K"
            ,
            ".-..": "L"
            ,
            "--": "M"
            ,
            "-.": "N"
            ,
            "---": "O"
            ,
            ".--.": "P"
            ,
            "--.-": "Q"
            ,
            ".-.": "R"
            ,
            "...": "S"
            ,
            "-": "T"
            ,
            "..-": "U"
            ,
            "...-": "V"
            ,
            ".--": "W"
            ,
            "-..-": "X"
            ,
            "-.--": "Y"
            ,
            "--..": "Z"
            ,
            "": " "
            ,
            }
        self.english_dict = {value:key for key, value in self.morse_dict.items()}

    def morse_to_english(self, morse_text):
        english_text = ""
        morse_words = morse_text.strip().split("  ")
        for morse_word in morse_words:
            morse_chars = morse_word.split(" ") 
            for morse_char in morse_chars:
                if morse_char in self.morse_dict:
                        english_text += self.morse_dict[morse_char]
                else:
                    pass
            english_text += " "     
            
            
        return english_text
        
    def english_to_morse(self, english_text):
        morse_text = ""
        for char in english_text:
            if char.upper() in self.english_dict:
                morse_text += self.english_dict[char.upper()] + " "
            else:
                pass
            
        return morse_text

morse_translator = MorseCodeTranslator()
morse_text = morse_translator.english_to_morse("coding time")
english_text = morse_translator.morse_to_english(morse_text)

print("morse = ", morse_text)
print("english = ", english_text)