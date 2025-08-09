
TEXT = """what do you want from me. I will not be back so soon."""


def compute_readability(input_text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0
    
    #TODO
    #Note the usdage of split() as a solution to splitting strings into groups using spaces

    def count_word(input_text):
        word_count = 1 # 1 to account for the last wor in the text that does not have a space after it.
        for char in input_text:
            if char == " ":
                word_count = word_count + 1
        return word_count

    def count_sentences(input_text):
        sentence_count = 0 # 1 to account for the last word in the text that does not have a space after it.
        terminators = ".?:"
        for char in input_text:
            if char == ".":
                sentence_count = sentence_count + 1
        return sentence_count

    total_words = count_word(input_text)
    print("total words are ", total_words)
    total_sentences = count_sentences(input_text)
    print("total sentences are ", total_sentences)

compute_readability(TEXT)
# total_syllables= count_syllables(text)

# score = 206.835- 1.015 * (total_words/total_sentences) - 84.6 * (total_syllables/total_words)

# if score >= 90.0:
#     print('reading level of 5th grade')
# elif score >= 80.0
#     print('reading level of 6th grade')
# elif score >= 80.0
#     print('reading level of 6th grade')
# elif score >= 80.0
#     print('reading level of 6th grade')
