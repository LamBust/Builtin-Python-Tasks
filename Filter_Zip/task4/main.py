import json

langs = ["Python", "Java", "JavaScript"]

def filt(el):
    if 18 > el['age'] or 25 < el['age']:
        return False
    if not any(el['skills']['programming'][i] in langs for i in range(len(el['skills']['programming']))):
        return False
    if len(el['debts']) != 0:
        return False
    return el['grades']['average'] > 4

if __name__ == "__main__":
    with open("input.json", encoding='utf8') as f:
        data = json.load(f)
    filtered_data = list(filter(filt, data))
    with open("output.json", 'w', encoding='utf8') as f:
        json.dump(filtered_data, f, ensure_ascii=False)
