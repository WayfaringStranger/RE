import re

test_string = 'hello 123_HELLO'

pattern = re.compile(r'[A-Z]')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
