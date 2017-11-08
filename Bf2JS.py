import argparse

# Adding args and description for pyhton3 file call on shell
# Exemple: python3 bf2JS.py example1.bf -o output1.js
parser = argparse.ArgumentParser(description='Process a brainfuck file to JS.')
parser.add_argument("bfFile")
parser.add_argument("-o")

# Creates a namespace object for the args
ARGUMENTS = parser.parse_args()

# Saves the args (Files) in constants for further use
INPUT_BF = ARGUMENTS.bfFile
OUTPUT_JS = ARGUMENTS.o

# This is the main function
def main():
    print "Initializing parser BF-2-JS"

main()
