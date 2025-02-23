def count_words(sentence):
    words = sentence.split()  
    return len(words)  
sentence = "The quick brown fox jumps over the lazy dog"
print("Word count:", count_words(sentence))  
