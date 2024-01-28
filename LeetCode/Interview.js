function getSpamEmails(subjects, spam_words) {
    const lowercaseSpamWords = spam_words.map(word => word.toLowerCase());
    const spamDetection = [];

    for (let i = 0; i < subjects.length; i++) {
      const subject = subjects[i].toLowerCase();
      const words = subject.split(' ');
      let count = 0;

      for (let j = 0; j < words.length; j++) {
        if (lowercaseSpamWords.includes(words[j])) {
          count++;
        }
      }

      if (count >= 2) {
        spamDetection.push('spam');
      } else {
        spamDetection.push('not_spam');
      }
    }

    return spamDetection;
  }
console.log(getSpamEmails(["I paid him paid", "Summertime Sadness"],["I", "paid", "Sadness"]));
console.log(getSpamEmails(["Let it go", "The right thing to do"],["to", "do", "right","go","let"]));

function isPangram(pangram) {
    const result = [];

    for (let i = 0; i < pangram.length; i++) {
      const letters = pangram[i].toLowerCase().replace(/[^a-z]/g, '');
      const uniqueLetters = new Set(letters);

      if (uniqueLetters.size === 26) {
        result.push('1');
      } else {
        result.push('0');
      }
    }

    return result.join('');
  }

function missingWords(s, t) {
    const sWordArr = s.split(' ');
    const tWordArr = t.split(' ');
    const wordsMissing = [];

    let i = 0;
    for (let j = 0; j < sWordArr.length; j++) {
      if (i < tWordArr.length && sWordArr[j] === tWordArr[i]) {
        i++;
      } else {
        wordsMissing.push(sWordArr[j]);
      }
    }

    return wordsMissing;
}

const s = 'I like cheese';
const t = 'like';
const mwordsMissing = missingWords(s, t);
