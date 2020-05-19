import re

test_string = '123abc456789abc123ABC'

pattern = re.compile(r'abc')
match = pattern.search(test_string) # search first one

print(match)
