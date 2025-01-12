import re

text = "The quick brown fox"
#pattern = r"brown"
pattern = "fox"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

print(pattern)