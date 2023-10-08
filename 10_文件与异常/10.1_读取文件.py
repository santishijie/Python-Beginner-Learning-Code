from pathlib import Path

path = Path('digit.txt')
contents = path.read_text()
print(contents)
