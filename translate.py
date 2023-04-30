tha = {
    "ฟ" ,
    "ิ" ,
    "แ" ,
    "ก" ,
    "ำ" ,
    "ด" ,
    "เ" ,
    "้" ,
    "ร" ,
    "่" ,
    "า" ,
    "ส" ,
    "ท" ,
    "ื" ,
    "น" ,
    "ย" ,
    "ๆ" ,
    "พ" ,
    "ห" ,
    "ะ" ,
    "ี" ,
    "อ" ,
    "ไ" ,
    "ป" ,
    "ั" ,
    "ผ" ,
    "ฐ" ,
    "ฅ" ,
    "ฤ" ,
    "ฺ" ,
    "ฉ" ,
    "ฏ" ,
    "ฎ" ,
    "โ" ,
    "ฌ" ,
    "็" ,
    "ณ" ,
    "๋" ,
    "ษ" ,
    "ศ" ,
    "์" ,
    "ฯ" ,
    "ญ" ,
    "๐" ,
    "ฑ" ,
    "ฆ" ,
    "ธ" ,
    "๊" ,
    "ฮ" ,
    "ํ" ,
    "บ" ,
    "ฅ" ,
    "ล" ,
    "ู" ,
    "๘" ,
    "ม",
    "ใ",
    "ง",
    "ภ",
    "ภ",
    "ุ",
    "ึ",
    "ค",
    "ต",
    "ข",
    "ช",
    "ว",
    "ซ",
    "@",
    "!",
    "1",
    "2",
    "3"
}
eng = {
    "a" ,
    "b" ,
    "c" ,
    "d" ,
    "e" ,
    "f" ,
    "g" ,
    "h" ,
    "i" ,
    "j" ,
    "k" ,
    "l" ,
    "m" ,
    "n" ,
    "o" ,
    "p" ,
    "q" ,
    "r" ,
    "s" ,
    "t" ,
    "u" ,
    "v" ,
    "w" ,
    "x" ,
    "y" ,
    "z" ,
    "{" ,
    "|" ,
    "}" ,
    "A" ,
    "B" ,
    "C" ,
    "D" ,
    "E" ,
    "F" ,
    "G" ,
    "H" ,
    "I" ,
    "J" ,
    "K" ,
    "L" ,
    "M" ,
    "N" ,
    "O" ,
    "P" ,
    "Q" ,
    "R" ,
    "S" ,
    "T" ,
    "U" ,
    "V" ,
    "W" ,
    "X" ,
    "Y" ,
    "Z" ,
    "[" ,
    "\\" ,
    "]" ,
    "^" ,
    "_" ,
    "`" ,
    ",",
    ".",
    "'",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "-",
    "=",
    ";",
    ":",
    " "
}
engTotha = {
    "a": "ฟ" ,
    "b": "ิ" ,
    "c": "แ" ,
    "d": "ก" ,
    "e": "ำ" ,
    "f": "ด" ,
    "g": "เ" ,
    "h": "้" ,
    "i": "ร" ,
    "j": "่" ,
    "k": "า" ,
    "l": "ส" ,
    "m": "ท" ,
    "n": "ื" ,
    "o": "น" ,
    "p": "ย" ,
    "q": "ๆ" ,
    "r": "พ" ,
    "s": "ห" ,
    "t": "ะ" ,
    "u": "ี" ,
    "v": "อ" ,
    "w": "ไ" ,
    "x": "ป" ,
    "y": "ั" ,
    "z": "ผ" ,
    "{": "ฐ" ,
    "|": "ฅ" ,
    "}": "," ,
    "A": "ฤ" ,
    "B": "ฺ" ,
    "C": "ฉ" ,
    "D": "ฏ" ,
    "E": "ฎ" ,
    "F": "โ" ,
    "G": "ฌ" ,
    "H": "็" ,
    "I": "ณ" ,
    "J": "๋" ,
    "K": "ษ" ,
    "L": "ศ" ,
    "M": "?" ,
    "N": "์" ,
    "O": "ฯ" ,
    "P": "ญ" ,
    "Q": "๐" ,
    "R": "ฑ" ,
    "S": "ฆ" ,
    "T": "ธ" ,
    "U": "๊" ,
    "V": "ฮ" ,
    "W": "_" ,
    "X": ")" ,
    "Y": "ํ" ,
    "Z": "(" ,
    "[": "บ" ,
    "\\": "ฅ" ,
    "]": "ล" ,
    "^": "ู" ,
    "_": "๘" ,
    "`": "." ,
    ",": "ม",
    ".": "ใ",
    "'": "ง",
    "4": "ภ",
    "5": "ภ",
    "6": "ุ",
    "7": "ึ",
    "8": "ค",
    "9": "ต",
    "-": "ข",
    "=": "ช",
    ";": "ว",
    ":": "ซ",
    " ": " "
}
from english_words import english_words_set

def swapp(str):
    if(str.find('#t') != -1):
        str = str.replace("#t","")
        return convert(str)
    if(not checkTha(str) and checkEng(str)):
        words = str.split()
        for i in words:
            if(i in english_words_set):
                return "-1"
        
        same = []
        c = 0
        for i in str:
            if(i not in same):
                c+=1
                same.append(i)
        if(c <= 5): return "-1"

        return convert(str)
    else: return "-1"

def checkEng(str):
    for i in str:
        if(i in eng):
            return True
    return False

def checkTha(str):
    for i in str:
        if(i in tha):
            return True
    return False

def convert(str):
    a = ''
    for i in str:
        try:
            a += engTotha[i]
        except:
            a += '_'
    return a

if __name__ == "__main__":
    str = input()
    print(swapp(str))