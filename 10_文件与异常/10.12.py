from pathlib import Path
import json

path = Path('number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = int(input("Please input you favorite number:"))
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks,I will remember that")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")