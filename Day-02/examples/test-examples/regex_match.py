import re

text = "the climate is cool"
pattern = r"climate"

match = re.match(pattern, text)
if match:
    print("match found:",match.group())
else:
    print("no match")