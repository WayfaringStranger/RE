import re

test_string = 'hello_123'

pattern = re.compile(r'\d+')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
