import json

def balanced(s):
    if s.count('(') == s.count(')'): return True

def form_json():
    ans = []
    with open("Builtin-Python-Tasks/Eval_Enum/t1/t1.txt", encoding="UTF8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            if any(line[i] == ':' or line[i] == '=' for i in range(len(line))):
                continue
            line = line.split(' ')
            for i in range(len(line)):
                w = line[i]
                if any(w[i] == '(' for i in range(len(w))):
                    todo = w
                    while not balanced(todo) and i < len(line)-1:
                        i += 1
                        todo += ' '
                        todo += line[i]
                    if balanced(todo) and todo.find("print") == -1: 
                        ans.append(todo)
    with open("Builtin-Python-Tasks/Eval_Enum/t1/ans.json", 'w') as f:
        json.dump(ans, f)
        