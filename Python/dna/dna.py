# Find man by his DNA.

import sys


def check_dna(database: str, sequences: str) -> str:
    # TODO: Complete check of right number of arguments.
    if len(sys.argv) != 3:
        return "Usage: python dna.py data.csv sequence.txt"

    name = 'NotYetCompleted Man'
    return name


# MAIN PROGRAM
man = check_dna(sys.argv[1], sys.argv[2])
print(man)

if __name__ == '__main__':
    check_dna(sys.argv[1], sys.argv[2])
