def wordCount (bookPath):
    with open(bookPath, "r") as f:
        book = f.read()
        print(len(book.split()))

wordCount('./books/frankenstein.txt')