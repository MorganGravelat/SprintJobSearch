alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
let asking = true;

function moveLetters(word){
    let newWord = "";

    for (let i = 0; i < word.length; i++) {
        ltr = word[i];
        if (ltr == "z") {
            newWord += "a";
        }
        else {
            newWord += alphabet[alphabet.indexOf(ltr) + 1];
        }
    }
    return newWord
}
while (asking) {
    let word = prompt("Enter a word to move the letters");
    if (word == "stop") {
        asking = false;
    }
    else {
        console.log(moveLetters(word));
    }
}
