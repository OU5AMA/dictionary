import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(w):
    w = w.lower().strip()
    if w in data:
        w = data[word]
        ENUM_w = enumerate(w,1)
        for i in ENUM_w:
            print(f'{i[0]} - {i[1]}\n')
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? Enter Y if yes, or N if no: ").upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = search(word)

#convert the following condition to list comprehension
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
