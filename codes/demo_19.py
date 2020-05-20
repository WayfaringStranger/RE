import re

test_string = 'hello 123_'

pattern = re.compile(r'[0-9]')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
