alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];

asking = True

def moveLetters(word):
    newWord = ""

    for letter in word:
        if letter == "z":
            newWord += "a"
        elif letter == " ":
            newWord += " "
        else:
            newWord += alphabet[alphabet.index(letter)+1]

    return newWord

while(asking):
    word = input("Enter a word: ")
    print(moveLetters(word))
    if input("Do you want to continue? (y/n): ") == "n":
        asking = False
