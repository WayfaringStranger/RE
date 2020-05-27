import re

dates = """
Mr Simpson
Mrs Simpson
Mr.Brown
Ms Smith
Mr. T
competetiveprogrammer@gmail.com
python-developer@gmail.com
"""

pattern = re.compile(r'([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)')
matches = pattern.finditer(dates)

for match in matches:
    print(match.group())
