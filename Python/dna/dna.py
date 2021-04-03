# Find man by his DNA.

import sys
import csv


def input_data(database: str) -> list:
    """
    Read database file.
    :param database: Name of database csv-file.
    :return: List of dictionaries of people like {'name': 'Alice', 'AGATC': '2', 'AATG': '8', 'TATC': '3'}
    """
    with open(database) as csvfile:
        reader = csv.DictReader(csvfile)
        list_people = []
        for row in reader:
            list_people.append(dict(row))
    return list_people


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


def count_rsa(list_rsa: list, seq: str) -> list:
    """
    Calculate max numbers of repeated consequences.
    :param list_rsa: List of RSA
    :param seq: DNA sequence to check
    :return: List of max consequences of repeated RSAs
    """
    detected_dna = []
    for i in list_rsa:  # Loop consequently for each RSA.
        if i != 'name':
            length_rsa = len(i)   # Length of current RSA
            count = 0   # Counter of consequently repeated RSA
            count_max = 0  # Max counter of consequently repeated RSA
            j = int(0)
            index = int(0)  # Index of list detected_dna
            while j < len(seq) - length_rsa:
                while seq[j:(j + length_rsa)] == i:
                    count += 1
                    if count > count_max:
                        count_max = count
                    j += length_rsa
                count = 0
                j += 1
            detected_dna.append(count_max)
            index += 1
    return detected_dna


def final_search(data: list, dna_extract: list) -> str:
    # TODO: Complete function
    return "name"


def check_dna(database: str, sequence: str) -> str:
    """
    Check if DNA in sequence file belongs to any man from database file.
    :param database: Name of database file.
    :param sequence: Name of sequennce file.
    :return: Name of man or "No match".
    """
    if len(sys.argv) == 3:
        data = input_data(database)     # List of dictionaries
        seq = input_seq(sequence)       # String
        dna_extract = count_rsa(data[0].keys(), seq)
        name = final_search(data, dna_extract)
        # TODO: Complete the function
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
