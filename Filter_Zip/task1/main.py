import json
import random

names = ["Александр", "Максим", "Марк", "Лев", "Артем", "Ян", "Игорь", "Олег", "Виктор", "Михаил", "София", "Анна", "Мария", "Ева", "Алиса", "Кира", "Вера", "Ника", "Мила", "Инна", "Леон", "Эрик", "Оскар", "Адам", "Лиам", "Белла", "Луна", "Мия", "Тея", "Адель"]
marks = [round(random.random() * 4 + 1, 2) for i in range(30)]

if __name__ == "__main__":
    ans = {name : mark for name, mark in zip(names, marks)}
    with open("marks.json", 'w', encoding='utf-8') as f:
        json.dump(ans, f, ensure_ascii=False)