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
    with open(sequence) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dna = row[0]
    return dna


def count_str(list_str: list, seq: str) -> list:
    """
    Calculate max numbers of repeated consequences.
    :param list_str: List of STR
    :param seq: DNA sequence to check
    :return: List of max consequences of repeated STRs
    """
    detected_dna = []
    for i in list_str:  # Loop consequently for each STR.
        if i != 'name':
            length_str = len(i)  # Length of current STR
            count = 0  # Counter of consequently repeated STR
            count_max = 0  # Max counter of consequently repeated STR
            j = int(0)
            index = int(0)  # Index of list detected_dna
            while j < len(seq) - length_str:
                while seq[j:(j + length_str)] == i:
                    count += 1
                    if count > count_max:
                        count_max = count
                    j += length_str
                count = 0
                j += 1
            detected_dna.append(count_max)
            index += 1
    return detected_dna


def final_search(data: list, dna_extract: list) -> str:
    """
    Finally compare detected STR numbers with list of people.
    :param data: List of dictionaries of people.
    :param dna_extract: List of calculated max consequenced STR.
    :return: Name of finded man or "No match."
    """
    num_of_str = len(dna_extract)
    norm_dna = ['No match']
    for i in range(num_of_str):
        dna_extract[i] = str(dna_extract[i])
        norm_dna.append(dna_extract[i])

    num_of_people = len(data)
    is_find = False
    man_to_check = []
    for i in range(num_of_people):
        man_to_check = list(data[i].values())
        for j in range(1, num_of_str + 1):
            if man_to_check[j] == norm_dna[j]:
                is_find = True
            else:
                is_find = False
        if is_find:
            break
    if is_find:
        return man_to_check[0]
    else:
        return "No match"


def check_dna(database: str, sequence: str) -> str:
    """
    Check if DNA in sequence file belongs to any man from database file.
    :param database: Name of database file.
    :param sequence: Name of sequennce file.
    :return: Name of man or "No match".
    """
    if len(sys.argv) == 3:
        data = input_data(database)  # List of dictionaries
        seq = input_seq(sequence)  # String
        dna_extract = count_str(data[0].keys(), seq)
        name = final_search(data, dna_extract)
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
