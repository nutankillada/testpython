import re

text = " she is good"
pattern = r"good"

match = re.match(pattern, text)
if match:
    print("match found:", match.group())
else:
    print("no matched")