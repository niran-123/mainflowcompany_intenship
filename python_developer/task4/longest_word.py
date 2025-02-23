def longest_word(sentence):
    words = sentence.split()  
    return max(words, key=len) if words else "" 
sentence = "The quick brown fox jumps over the lazy dog"
print("Longest word:", longest_word(sentence))  
