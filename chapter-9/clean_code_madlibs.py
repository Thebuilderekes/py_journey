def collect_text(text):
    """
    Collects the text and converts it to a list of words.
    """
    word_list = text.split()
    return word_list


def check_words(word_list):
    """
    Loops through the word list, prompts the user for replacements
    for specific placeholder words, and returns the completed text.
    """
    # Create a dictionary to map placeholders to their prompts.
    # This is more efficient than using multiple if statements.
    placeholders = {
        "VERB_ING": "verb ending in -ing",
        "ADJECTIVE": "adjective",
        "NOUN": "noun",
    }

    # Use a list comprehension to build the new list of words.
    # This is a more "Pythonic" and concise way to write the loop.
    new_words = [
        (
            input(f"Please enter an {placeholders[word]}: ")
            if word in placeholders
            else word
        )
        for word in word_list
    ]

    # Join the words back into a single sentence.
    return " ".join(new_words)


# Example usage:
TEXT = "The VERB_ING dog ran quickly. The ADJECTIVE sky was above the Noun."

# You can directly pass the output of the first function to the second.
# This makes the code cleaner and easier to follow.
completed_text = check_words(collect_text(TEXT))

# Print the final result.
print(completed_text)
