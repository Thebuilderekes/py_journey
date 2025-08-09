"""function compute_readability going to be checking the readability
level of any piece of text passed to it.
"""

## Incomplete exercise coded by me and yet to be solved


# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
import text


def compute_readability(input_text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    # ALTERNATE SOLUTIONS
    # Note the usage of split() as a possible solution to
    # splitting strings into an array containing words
    # and then getting the length of the words using len() function.
    # This would be the solution to word count in TEXT

    # def word_count(input_text):
    # words = input_text.split()
    # return len(words)
    # total_words = word_count(text.TEXT)
    # Also note that using this method would include words that have
    # commas, question marks and other marks attatched to them when they are split.

    def count_word(input_text):
        word_count = 1  # 1 to account for the last word
        # in the text that does not have a space after it.
        for char in input_text:
            if char == " ":
                word_count = word_count + 1
        return word_count

    def count_sentences(input_text):
        terminators = ".?:!;"
        sentence_count = 0  # 1 to account for the last word in
        # the text that does not have a space after it.
        for char in input_text:
            if char in terminators:
                sentence_count = sentence_count + 1
        return sentence_count

    def count_syllables(input_text):
        vowels = "aeiou"
        syllable_count = sum(1 for vowel_letter in vowels if vowel_letter in input_text)
        return syllable_count

        # This function is incomplete and has to calculate the total
        # number of syllables which includes the sum of single syllable words and multi syllable words

    total_syllables = count_syllables(input_text)
    print("total syllables are", total_syllables)

    total_words = count_word(input_text)
    print("total words are ", total_words)
    total_sentences = count_sentences(input_text)
    print("total sentences are ", total_sentences)

    # total_syllables= count_syllables(text)

    score = (
        206.835
        - 1.015 * (total_words / total_sentences)
        - 84.6 * (total_syllables / total_words)
    )

    if score >= 90.0:
        print("reading level of 5th grade")
    elif score >= 80.0:
        print("reading level of 6th grade")
    elif score >= 70.0:
        print("reading level of 7th grade")
    elif score >= 60.0:
        print("reading level of 8-9th grade")
    elif score >= 50.0:
        print("reading level of 10-12th grade")
    elif score >= 30.0:
        print("reading level of college student")
    else:
        print("reading level of college graduate")


compute_readability(text.TEXT)
