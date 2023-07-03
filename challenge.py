print('************Task1-Prefix************')
prefix_word = input ('Please key in word you want prefix(un) adding to:\n')

print('Adding \'un\' to the word keyed in above would be:')
print ('un'+prefix_word)

print('\n************Task2 - Word Group Prefix************')
def make_word_groups(vocab_words):
    prefix = vocab_words[0]  # Extract the prefix from the list
    
    # Apply the prefix to each word using list comprehension
    words_with_prefix = [prefix + word for word in vocab_words[1:]]
    
    # Join the words with the prefix using the "::" separator
    result = " :: ".join([prefix] + words_with_prefix)
    
    return result

sentence = input('Please type in the prefix and words you want to add the prefix to.\nPlease key it in the following format: en close joy light.\n')
vocab_words = sentence.split()

result = make_word_groups(vocab_words)
print(result)


print('\n************Task 3 - Remove Suffix************')

# Added in fail proof code to prevent the program from crashing
try:
    remove_suffix_ness = input('Key in the word where you want to remove the suffix -ness\n')
    word_without_suffix = remove_suffix_ness[:-4]
# This is to replace the i with y when the suffix is removed.
    if word_without_suffix[-1] == 'i':
        word_without_suffix = word_without_suffix[:-1] + 'y'
        
    print (word_without_suffix)
except IndexError:
    print('Error: invalid input please try again.')
    
    
print('\n************Task 4 - Extract and transform a word************')

# Sister inputs the sentence she wants to play with.
sentence_adj = input ('Please key in the sentence we want to examine\n')
index_adj = int(input('With the first word being 0, second word being 1, and so on, please key in the index for the word we want to into verb\n'))

# The following verbifies the adjective.

def adjective_to_verb(sentence_adj, index_adj):
    words = sentence_adj.split ()
    adjective = words[index_adj]
    return (adjective + 'en')
    
result4 = adjective_to_verb(sentence_adj, index_adj)
print (result4)

    

