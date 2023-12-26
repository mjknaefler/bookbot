
def main():
    book_path = "books/frankenstein.txt"
    text = getBookText(book_path)
    numWords = getNumWords(text)
    numLetters = getLetterCount(text)
    report(book_path,numWords,numLetters)

def getNumWords(text):
    words = text.split()
    return len(words)

def getBookText(path):
    with open(path) as f:
        return f.read()

def getLetterCount(text):
    lowerCaseText = text.lower()
    letterDict = {}
    for letter in lowerCaseText:
        if letter in letterDict:
            letterDict[letter] += 1
        else:
            letterDict[letter] = 1
    return letterDict

def report(path,wordCount,letterCount):
    letterCountList = list(letterCount.items())
    letterCountList.sort()
    print(f"--- Begin report of {path} ---")
    print(f"{wordCount} words found in the document")
    print()
    for x,y in letterCountList:
        if(x.isalpha()):
            print(f"The '{x}' character was found {y} times")
    print("--- End report ---")

main()