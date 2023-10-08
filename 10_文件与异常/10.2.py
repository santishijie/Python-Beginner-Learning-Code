from pathlib import Path
path = Path("learning_python.txt")
contents = path.read_text()
line = contents.splitlines()
for i in line:
    i = i.replace('python', 'C')
    print(i)
# path.replace('python', 'C')
# print(path)