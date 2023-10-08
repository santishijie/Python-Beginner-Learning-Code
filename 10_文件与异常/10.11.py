from pathlib import Path
import json

number = int(input("Please input you favorite number:"))
path = Path('numbers.json')
contents = json.dumps(number)
path.write_text(contents)
