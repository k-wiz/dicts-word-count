# put your code here.

# open file 
def create_list_of_words(filename):
    """Returns list of words from file."""

    the_file = open(filename)

    big_word_list = []

    for line in the_file:
        line = line.rstrip()
        word_list = line.split()
        big_word_list = big_word_list + word_list #Turn separate lists into one large list
    
    return big_word_list

big_word_list = create_list_of_words("test.txt")

def word_count(word_list):
    """Returns word count from a file.""" 

    word_count_dict = {}

    for word in word_list:
    
        if word_count_dict.get(word,0) == 0:
            word_count_dict[word] = 1
        else:
            word_count_dict[word] += 1
 
    print word_count_dict

word_count(big_word_list)



