import re


def compute_readability(input_text):
    def count_words(input_text):
        # Using split() to directly split the text into words.
        words = input_text.split()
        return len(words)

    def count_sentences(input_text):
        # Using regex to count sentence-ending punctuations
        sentence_endings = re.findall(r"[.!?;]", input_text)
        return len(sentence_endings)

    def count_syllables(input_text):
        # Using a simple method to count vowels in the text.
        vowels = "aeiouAEIOU"
        syllable_count = sum(1 for char in input_text if char in vowels)
        return syllable_count

    # Count total words, sentences, and syllables
    total_words = count_words(input_text)
    total_sentences = count_sentences(input_text)
    total_syllables = count_syllables(input_text)

    print(f"Total words: {total_words}")
    print(f"Total sentences: {total_sentences}")
    print(f"Total syllables: {total_syllables}")

    # Calculate the readability score
    if total_sentences > 0:
        score = (
            206.835
            - 1.015 * (total_words / total_sentences)
            - 84.6 * (total_syllables / total_words)
        )
    else:
        score = 0  # In case there are no sentences

    print(f"Readability score: {score}")

    # Determine the reading level based on the score
    if score >= 90.0:
        print("Reading level: 5th grade")
    elif score >= 80.0:
        print("Reading level: 6th grade")
    elif score >= 70.0:
        print("Reading level: 7th grade")
    elif score >= 60.0:
        print("Reading level: 8-9th grade")
    elif score >= 50.0:
        print("Reading level: 10-12th grade")
    elif score >= 30.0:
        print("Reading level: College student")
    else:
        print("Reading level: College graduate")


if __name__ == "__main__":
    from text import TEXT

    compute_readability(TEXT)
