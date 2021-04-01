def coleman_liau(text: str) -> int:
    return int(0)


# MAIN PROGRAM
text = input("Text: ")

if coleman_liau(text) > 16:
    print("Grade 16+")
elif coleman_liau(text) < 1:
    print("Before Grade 1")
else:
    print("Grade " + str(coleman_liau(text)))
