import argparse

# Adding args and description for pyhton3 file call on shell
# Exemple: python3 bf2JS.py example1.bf -o output1.js
parser = argparse.ArgumentParser(description='Process a brainfuck file to JS.')
parser.add_argument('bfFile')
parser.add_argument('-o')

# Creates a namespace object for the args
ARGUMENTS = parser.parse_args()

# Saves the args (Files) in constants for further use
INPUT_BF = ARGUMENTS.bfFile
OUTPUT_JS = ARGUMENTS.o

##
ARRAY_NAME = 'bfArray'
COUNTER_NAME = 'tapeReader'
BFCHAR_TO_JS = {
    # Increments the cell value
    '+': '%s[%s]++\n' % (ARRAY_NAME, COUNTER_NAME),
    # Decrements the cell value
    '-': '%s[%s]--\n' % (ARRAY_NAME, COUNTER_NAME),
    # Moves the pointer to the right
    '>': '%s++\n' % (COUNTER_NAME),
    # Moves the pointer to the left
    '<': '%s--\n' % (COUNTER_NAME),
    # Prints the cell value - ASCII
    '.': 'String.fromCharCode(%s[%s])\n' % (ARRAY_NAME, COUNTER_NAME),
    # Gets a char and saves the value on cell
    ',': '%s[%s] = prompt(\"Type a char\").charAt(0)' % (ARRAY_NAME, COUNTER_NAME),
    # Starts the loop - If the cell is 0, goto matching ]
    '[': 'while(%s) {\n' % (COUNTER_NAME),
    # Finishes the loop - Back to matching [ if cell not null
    ']': '}\n'
}

# This is the main function
def main():
    print ('Initializing parser BF-2-JS')

    fileBF = open(INPUT_BF, 'r')
    fileJS = open(OUTPUT_JS, 'w')

    readedFile = fileBF.read()

    fileJS.write('var %s = [0]\nvar %s = 0\n\n' % (ARRAY_NAME, COUNTER_NAME)) 

    for char in readedFile:
        print('Reading %s' % (char))
        if char in BFCHAR_TO_JS:
            result = BFCHAR_TO_JS[char]
            print('Printing %s' % (result))
            fileJS.write(result)

    fileBF.close()
    fileJS.close()

main()
