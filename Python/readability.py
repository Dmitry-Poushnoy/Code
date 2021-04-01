def coleman_liau(text_in: str) -> int:
    """
    Calculate Coleman-Liau index.
    :param text_in: String for evaluation.
    :return: Grade like integer.
    """
    # Count letters
    count_letters = 0
    for char in text_in:
        if char.isalnum():
            count_letters += 1

    # Count words
    count_words = len(text_in.split(' '))

    # Count sentences
    count_sentences = 0
    for char in text_in:
        if char in ('.', '!', '?'):
            count_sentences += 1

    # Calculate Coleman-Liau index
    l_var = (count_letters / count_words) * 100
    s_var = (count_sentences / count_words) * 100
    grade = round(0.0588 * l_var - 0.296 * s_var - 15.8)

    return int(grade)


# MAIN PROGRAM
text = input("Text: ")

if coleman_liau(text) > 16:
    print("Grade 16+")
elif coleman_liau(text) < 1:
    print("Before Grade 1")
else:
    print("Grade " + str(coleman_liau(text)))
