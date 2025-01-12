import re

text = "The quick brown fox"
#pattern = r"quick"
pattern = "The quick brown fox"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

print(match.group())