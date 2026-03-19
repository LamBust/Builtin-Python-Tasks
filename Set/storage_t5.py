class Storage:
    def __init__(self, args):
        self.products = set(i for i in args)
    
    def __sub__(self, other):
        return Storage(list(self.products.difference(other.products)))
    
    def __isub__(self, other):
        return self - other
    
    def __str__(self):
        return str({i for i in list(self.products)})

if __name__ == "__main__":
    A = Storage(["ноутбук", "мышь", "клавиатура", "монитор"])
    B = Storage(["мышь", "клавиатура", "принтер", "сканер"])
    print(A-B)
    A -= B
    print(A)