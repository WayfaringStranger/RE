import re

test_string = 'hello 123_HELLO'

pattern = re.compile(r'[a-zA-Z0-9]')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
