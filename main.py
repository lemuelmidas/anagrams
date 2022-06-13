# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    #change words to lowercase
    word= word.lower()
    anagram= anagram.lower()

    #Remove whitespace
    word= word.replace(" ", "")
    anagram= anagram.replace(" ", "")

    #sorted(word) == sorted(anagram) #True or False
    return sorted(word)== sorted(anagram)


print("Find_anagrams with 'hello' and 'check' ", find_anagram("hello", "check"))
print("Find_anagrams with 'below' and 'elbow' ", find_anagram("below", "elbow"))

      
        

    

