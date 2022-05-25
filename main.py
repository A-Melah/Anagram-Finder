# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    word_list = list(word)
    anagram_list = list(anagram)
    if len(word_list) == len(anagram_list):
        if word_list.sort() == anagram_list.sort():
            return True
    return False
     

print(find_anagram("game", "mage"))
