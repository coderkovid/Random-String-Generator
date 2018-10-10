import random

class random_str():
    def string():
        length = int(input("Enter the length of desired random word: "))
        dict1 = {
            "1": "a",
            "2": "b",
            "3": "c",
            "4": "d",
            "5": "e",
            "6": "f",
            "7": "g",
            "8": "h",
            "9": "i",
            "10": "j",
            "11": "k",
            "12": "l",
            "13": "m",
            "14": "n",
            "15": "o",
            "16": "p",
            "17": "q",
            "18": "r",
            "19": "s",
            "20": "t",
            "21": "u",
            "22": "v",
            "23": "w",
            "24": "x",
            "25": "y",
            "26": "z",
            }
        word = ""
        for i in range(0, length):
            x = str(random.randint(1, 26))
            word += dict1[x]
        return word


