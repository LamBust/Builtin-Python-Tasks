class Books:
    def __init__(self, *books):
        self.books = set(i for i in books)

    def __mul__(self, other):
        return self.books.intersection(other.books)
    
    def __imul__(self, other):
        return self*other

    def __str__(self):
        return str({i for i in list(self.books)})
    
if __name__ == "__main__":
    A = Books("Война и мир", "Преступление и наказание", "Анна Каренина", "Идиот")
    B = Books("Идиот", "Братья Карамазовы", "Преступление и наказание", "Бесы")
    print(A * B)
    A *= B
    print(A)