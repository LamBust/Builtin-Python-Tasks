class Shop:
    def __init__(self, offline, online):
        self.offline = set(i for i in offline)
        self.online = set(i for i in online)

    def all(self):
        return self.online.union(self.offline)
    
    def add(self, where, *what):
        toadd = set(i for i in what)
        if where == "offline":
            self.offline = self.offline.union(toadd)
        else:
            self.online = self.online.union(toadd)
    def __str__(self):
        return f"""Оффлайн: {str({i for i in list(self.offline)})}
Онлайн: {str({i for i in list(self.online)})}
Все: {str({i for i in list(self.all())})}"""

if __name__ == "__main__":
    shop = Shop(["+09001112233", "+09002223344", "+09003334455"], ["+09004445566", "+09001112233", "+09005556677"])
    print(shop)
    shop.add("online", "+09006667788", "+09007778899")
    print(shop)