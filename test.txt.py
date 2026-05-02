
with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Hello!")

with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print(text)
