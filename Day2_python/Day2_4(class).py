class AutoMobile:
    
    def __init__(self, str):
        self.name = str
    def velocityPlus(self):
        self.velocity = self.velocity + 10
    def velocityDown(self):
        self.velocity = self.velocity - 10

        if self.velocity < 0:
            self.velocity = 0

# ac = AutoMobile("현대")
# ac.velocity = 200
# ac.velocityPlus()
# print(ac.name + "의 속도는 %d 입니다." %ac.velocity)


class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    def in_inside(self, i, j):
        return (i-self.x)**2+(j-self.y)**2 < self.r**2
    
    # def in_inside(self, i, j):
    #     if((i-self.x)**2+(j-self.y)**2 < self.r):
    #         return True
    #     else:
    #         return False
    
# my_circle = Circle(1.0, 1.5, 0.8)

# print(my_circle.in_inside(1.5, 0.9))
# print(my_circle.in_inside(0.4, 0.5))




class Calculator:

    def __init__(self, num):
        self.num = num

    def sum(self):
        self.sum  = 0
        for i in self.num:
            self.sum += i
        return self.sum
    
    def func_sum(self):
        return sum(self.num)

    def avg(self):
        self.avg = 0.0
        self.avg = self.sum / len(self.num)
        return self.avg

# cal1 = Calculator([1,2,3,4,5])
# print(cal1.sum())
# print(cal1.func_sum())
# print(cal1.avg())

# print()

# cal2 = Calculator([6,7,8,9,10,11])
# print(cal2.sum())
# print(cal2.func_sum())
# print(cal2.avg())


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