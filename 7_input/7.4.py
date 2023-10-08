prompt = "Enter the ingredients for pizza:"
while True:
    ingredient = input(prompt)
    if ingredient == 'quit':
        break
    else:
        print(f"Add {ingredient.title()} to the pizza")
