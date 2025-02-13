def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()
print(is_anagram(s1, s2))
