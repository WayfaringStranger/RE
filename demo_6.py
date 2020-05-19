import re

test_string = '123abc56789abc123ABC'

pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)

for match in matches:
    print(match.start(), match.end())
