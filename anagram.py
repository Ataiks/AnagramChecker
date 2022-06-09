word1=input('enter word1: ')
word2=input('enter word2: ')
def find_anagrams(word1, word2):
    return word2[:] == word1[::-1]

x=find_anagrams(word1,word2)
print(x)
