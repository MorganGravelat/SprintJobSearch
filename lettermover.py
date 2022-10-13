alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];

asking = True

def moveLetters(word):
    newWord = ""
    for letter in word:
        index = alphabet.index(letter) + 13
        if index > 26:
            index = index % 26
        if letter == "z":
            newWord += "a"
        elif letter == " ":
            newWord += " "
        else:
            newWord += alphabet[(alphabet.index(letter)+14)]

    return newWord

while(asking):
    word = input("Enter a word: ")
    print(moveLetters(word))
    if input("Do you want to continue? (y/n): ") == "n":
        asking = False
