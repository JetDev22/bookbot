import sys
from stats import get_num_words

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    print(sys.argv)
    sys.exit(1)
else:
    fileName = sys.argv[1]


def main(filename):
    fileContents = ""
    # open file and save content
    with open(filename) as f:
        fileContents = f.read()
 
    # Book Report
    print(f"--- Begin report of {fileName} ---")

    # count words
    #print(f"{len(fileContents.split())} words found in the document")
    get_num_words(fileContents)

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
                print(f"{letter}: {result[letter]}")
        return

    charAnalysis(countChar(fileContents))

main(fileName)
