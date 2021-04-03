# Find man by his DNA.

import sys
import csv


def input_data(database: str) -> dict:
    """
    Read database file.
    :param database: Name of database csv-file.
    :return: Dictionary of people like {'name': 'Alice', 'AGATC': '2', 'AATG': '8', 'TATC': '3'}
    """
    with open(database) as csvfile:
        reader = csv.DictReader(csvfile)
    return reader


def input_seq(sequence: str) -> str:
    """
    Read sequence file.
    :param sequence: Name of sequence file.
    :return: String of sequence.
    """
    # TODO: Complete the function.
    with open(sequence) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dna = row[0]
    return dna


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
