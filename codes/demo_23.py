import re

test_string = 'hello_123'

pattern = re.compile(f'\d?')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
