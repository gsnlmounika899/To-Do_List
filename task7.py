import re
Text = input("Enter your text:\n")
words = re.findall(r'\b\w+\b', Text)
count = len(words)
print(f"The total number of words in the text is: {count}")