import re

text = "The quick brown fox"
pattern = r"brown"

match = re.match(pattern, text)

if match:
    print("content present")
else:
    print("not present")