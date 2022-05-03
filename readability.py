import re


def main():
    # Ask user for text input
    text = input("Text: ")

    # Count words by counting spaces, adding one more for the last word
    words = int(len(re.findall(' ', text))) + 1
    # Count sentences by counting the occurrence of periods, exclamation points, or question marks
    sentences = int(len(re.findall('\.|\?|\!', text)))
    # Count letters from the english alphabet
    letters = int(len(re.findall('[A-Za-z]', text)))

    # L is the average number of letters per 100 words in the text
    L = 100 * letters / words
    # S is the average number of sentences per 100 words in the text
    S = 100 * sentences / words

    # The Coleman-Liau formula
    grade = 0.0588 * L - 0.296 * S - 15.8

    # Print the grade level computed by the Coleman-Liau formula, rounded to the nearest integer
    if grade < 1:
        print("Before Grade 1")
    elif grade > 15:
        print("Grade 16+")
    else:
        print(f"Grade {round(grade)}")


if __name__ == "__main__":
    main()