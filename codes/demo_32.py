import re

dates = """
Mr Simpson
Mrs Simpson
Mr.Brown
Ms Smith
Mr. T
"""

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')
matches = pattern.finditer(dates)

for match in matches:
    print(match)
