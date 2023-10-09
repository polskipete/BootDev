import re

def wordCount (bookPath):
    with open(bookPath, "r") as f:
        book = f.read()
        return(len(book.split()))
    
def letterCount(bookPath):
    letterDict = {}
    with open(bookPath, "r") as f:
        bookText = f.read().upper()
        bookCharactersOnly = re.sub(r'[^A-Za-z]+', '', bookText)
        for letter in bookCharactersOnly:
            if letter in letterDict:
                letterDict[letter] += 1
            else:
                letterDict[letter] = 1
    return(letterDict)

def buildReport (word, letter):
    print(f"--- Begin report for {bookFile} ---")
    print(f"{wordCountVar} words found in the document\n\n")
    for letterEntry, letterCount in letterCountVar.items():
        print(f"The \"{letterEntry}\" character was found {letterCount} times")


bookFile = 'frankenstein.txt'

wordCountVar = wordCount("./books/" + bookFile)
letterCountVar = letterCount("./books/" + bookFile)

buildReport(wordCountVar, letterCountVar)
