import re

test_string = 'hello 123_ hey you'

pattern = re.compile(r'\S')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
