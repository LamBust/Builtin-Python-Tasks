import json

def give_anses():
    anses = []
    with open("Builtin-Python-Tasks/Eval_Enum/t1/ans.json") as f:
        data = json.load(f)
        for el in data:
            anses.append(eval(el))
    return anses

give_anses()