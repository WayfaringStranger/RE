import re

test_string = '123abc456789abc123ABC'

pattern = re.compile(f'abc')
matches = pattern.findall(test_string)

for match in matches:
    print(match)
