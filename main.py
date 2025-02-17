def main():
    fileContents = ""
    # open file and save content
    with open("books/frankenstein.txt") as f:
        fileContents = f.read()

    # print content
    #print(fileContents)
    
    # Book Report
    print("--- Begin report of books/frankenstein.txt ---")

    # count words
    print(f"{len(fileContents.split())} words found in the document")

    # count characters
    def countChar(fileContents):
        result = {}
        for char in fileContents:
            if char.lower() in result:
                result[char.lower()] += 1
            else:
                result[char.lower()] = 1
        return result

    def charAnalysis(result):
        for letter in result:
            if letter.isalpha():
                print(f"The '{letter}' character was found {result[letter]} times")
        return

    charAnalysis(countChar(fileContents))

main()
