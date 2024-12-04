import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")


import re              # i prefer coffee than tea

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("searc found:", search.group())
else:
    print("No no match")