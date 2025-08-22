# read file lib.txt

# Create a function that takes in the text from lib.txt
# convert the text string into an list of words using text.split()
# create a function to receive the words list
# Loop through words,
# if word is = VERB_ING
# index of that word to get its value = input('input a verb')
# if word is = NOUN
# index of that word to get its value = input('input a noun')
# if word is = ADJECTIVE
# index of that word to get its value = input('input a adjective')
# return list

if __name__ == "__main__":
    from lib import TEXT

    def collect_text(item):
        """collect the text and convert of list of words"""
        word_list = item.split()
        return word_list

    make_words = collect_text(TEXT)

    def check_words(list_items):
        """collect the list, loop over and replace the of words that match with input value"""
        verb = "VERB_ING"
        adjective = "ADJECTIVE"
        noun = "NOUN"
        seperator = " "
        for word in list_items:
            if word == verb:
                list_items[list_items.index(word)] = input("input a verb? ")
            if word == noun:
                list_items[list_items.index(word)] = input("input a noun? ")
            if word == adjective:
                list_items[list_items.index(word)] = input("input a adjective?")
        sentence = seperator.join(list_items)
        return sentence

    print(check_words(make_words))
