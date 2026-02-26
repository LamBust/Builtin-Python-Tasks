with open("find_words.bin", 'rb') as f:
    bytes_data = f.read()
    words = ["АКТИВАЦИЯ", "ЗАПУСК", "СИСТЕМА", "РЕЖИМ", "КОМАНДА", "ВЫПОЛНЕНИЕ"]
    encoded_words = [word.encode() for word in words]
    ans = dict()
    for i in range(len(words)):
        ans[words[i]] = bytes_data.count(encoded_words[i])
        print(words[i], '-', bytes_data.count(encoded_words[i]))