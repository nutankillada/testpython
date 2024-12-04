import re

text = "they have many cars in their garage"
pattern = r"garage"

replacement = "house"

new_text = re.sub(pattern, replacement, text)
print ("modified text:", new_text)