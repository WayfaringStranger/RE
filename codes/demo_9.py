import re

test_string = '123abc456789abcABC'

pattern = re.compile(r'^123')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
