# Find man by his DNA.

import sys


def check_dna(database: str, sequence: str) -> str:
    """
    Check if DNA in sequence file belongs to any man from database file.
    :param database: Name of database file.
    :param sequence: Name of sequennce file.
    :return: Name of man or "No match".
    """
    if len(sys.argv) == 3:
        name = 'NotYetCompleted Man'
        return name
    else:
        raise IndexError


# MAIN PROGRAM
try:
    man = check_dna(sys.argv[1], sys.argv[2])
    print(man)
except IndexError:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(0)

if __name__ == '__main__':
    check_dna(sys.argv[1], sys.argv[2])
