import re

test_string = 'abc123ABC456789abc'

pattern = re.compile(r'.')
matches = pattern.finditer(test_string)

for match in matches:
    print(match.group())
