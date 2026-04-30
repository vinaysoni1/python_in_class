# Q2. Reverse the order of words without reversing individual words
text = input("Enter a sentence: ")
words = text.split()
reversed_words = words[::-1]
result = " ".join(reversed_words)
print("Reversed sentence:", result)