if __name__ == "__main__":
    blocked = ["block", "verybadword"]
    text = "affsa asdsfsasaf verybadwor dsadadsa qpsa".split()
    if any(any(text[i] == blocked[j] for j in range(len(blocked))) for i in range(len(text))):
        print("присутсвует запрещённое слово")
    else: print("Запрещённых слов в тексте нет")