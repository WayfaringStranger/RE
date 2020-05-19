import re

test_string = '123abc456789abcABC'

pattern1 = re.compile(r'abc')
match1 = pattern1.match(test_string)

pattern2 = re.compile(r'123')
match2 = pattern2.match(test_string)

print(match1)
print(match2)
