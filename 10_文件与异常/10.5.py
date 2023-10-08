from pathlib import Path

names = ""
ad = "请输入你的名字，写入你想记录的内容:"
user_input = input(ad)
while user_input != 'quit':
    names += user_input + '\n'
    user_input = input(ad)
path = Path("./book.txt")
path.write_text(names)
