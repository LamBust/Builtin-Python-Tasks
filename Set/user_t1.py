class User():
    def __init__(self, *channels):
        self.channels = set(channels[i] for i in range(len(channels)))
        print(self)

    def follow(self, channel):
        self.channels.add(channel)
        print(self)

    def unfollow_er(self, channel):
        try:
            self.channels.remove(channel)
        except:
            print("Пользователь не подписан на канал", channel)
        print(self)

    def unfollow(self, channel):
        self.channels.discard(channel)
        print(self)

    def unfollow_all(self):
        self.channels.clear()
        print(self)

    def __str__(self):
        return str({i for i in list(self.channels)})

if __name__ == "__main__":
    user = User("news", "music", "sports", "tech")
    user.follow("cinema")
    user.unfollow_er("music")
    user.unfollow("gaming")
    user.unfollow_all()