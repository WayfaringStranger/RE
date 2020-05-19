import re

test_string = '123abc456789abc123ABC'

pattern = re.compile(r'abc') # in r'abc' here r mean input string is raw-string
matches = pattern.finditer(test_string)

# matches = re.finditer(r'abc', test_string)

for match in matches:
    print(match)
