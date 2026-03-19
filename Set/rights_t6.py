class Rights:
    def __init__(self, *rights):
        self.allowed = set(i for i in rights)
        self.admin = {"read", "write", "execute", "delete", "admin"}

    def isr(self):
        return "read" in self.allowed
    
    def isadmin(self):
        return self.admin <= self.allowed
    
    def is_in_admins(self):
        return self.allowed <= self.admin
    
    def __str__(self):
        return f"""{self.isr()}
{self.isadmin()}
{self.is_in_admins()}"""

if __name__ == "__main__":
    print(Rights("read", "write"), '\n')
    print(Rights("write", "delete"), '\n')
    print(Rights("read", "write", "execute", "delete", "admin"), '\n')