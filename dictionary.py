import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Spelling sudhaar be!! Did you mean %s (Y/N): "%get_close_matches(word,data.keys())[0])
        if yn is "Y" or yn is "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn is "N" or yn is "n":
            return "Aisa koi word nahi, kuch bhi mat type kar!!"
        else:
            return "Dimaag satakk gaya kya, answer only in Y or N"
    else:
        return "Kuch bhi mat type kar!!"

print("\n\tDICTIONARY HAI DICTIONARY!!! English Dictionary\n")
word = input("Enter a word: ")
output = dictionary(word)
if type(output) is list:
    for i in output:
        print(i)
else:
    print(output)
print(" ")
