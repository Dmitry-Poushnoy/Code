# Find man by his DNA.

import sys
import csv


def input_data(database: str) -> dict:
    """
    Read database file.
    :param database: Name of database csv-file.
    :return: Dictionary of people.
    """
    # TODO: Complete the function.
    return {'NotCompletedDictKey': 'NotCompletedDictValue'}


def input_seq(sequence: str) -> str:
    """
    Read sequence file.
    :param sequence: Name of sequence file.
    :return: String of sequence.
    """
    # TODO: Complete the function.
    return str('NotCompletedSequence')


def check_dna(database: str, sequence: str) -> str:
    """
    Check if DNA in sequence file belongs to any man from database file.
    :param database: Name of database file.
    :param sequence: Name of sequennce file.
    :return: Name of man or "No match".
    """
    if len(sys.argv) == 3:
        data = input_data(database)
        seq = input_seq(sequence)
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
