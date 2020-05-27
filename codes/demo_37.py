import re

test_string = 'hello world, you are the best world'

pattern = re.compile(r'world')
subbed_string = pattern.sub('planet', test_string)
print(subbed_string)
