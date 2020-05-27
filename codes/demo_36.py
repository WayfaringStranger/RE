import re

test_string = 'xyz123abcABC123890xyz'

pattern = re.compile(r'123')
splitted = pattern.split(test_string)
print(splitted)
