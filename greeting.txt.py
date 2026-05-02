with open("greeting.py", "w", encoding="utf-8") as file:
    file.write("Здравствуйте, спасибо за занятия!")

with open("greeting.py", "r", encoding="utf-8") as file:
    print(file.read())