ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def filt(string):
    if len(string) <= 5:
        return False
    if string[0].lower() == 'a':
        return False
    return any(string[i] in ints for i in range(len(string)))

if __name__ == "__main__":
    words = ["Apple123", "Banana456", "Cat7", "Dog2023", "Elephant", "Fish99", "Ant", "Python3", "A12345", "HelloWorld1"]
    needed_words = list(filter(lambda x: filt(x), words))
    print(needed_words)