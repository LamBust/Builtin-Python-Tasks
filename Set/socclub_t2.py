class SocialMedia:
    def __init__(self, args):
        self.users = set(i for i in args)

    def copy(self):
        return self
    
    def __sub__(self, other):
        return SocialMedia(list(self.users.difference(other.users)))
    
    def __isub__(self, other):
        return self - other
    
    def __str__(self):
        return str({i for i in list(self.users)})

if __name__ == "__main__":
    A = SocialMedia(["Alice", "Bob", "Charlie", "David"])
    B = SocialMedia(["Charlie", "David", "Eve", "Frank"])
    A_1 = A.copy()
    print(A == A_1)
    print(A-B)
    A -= B
    print(A)