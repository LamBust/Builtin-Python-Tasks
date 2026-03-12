def compare(ver1, ver2):
    ver1 = list(map(int, ver1.split('.')))
    ver2 = list(map(int, ver2.split('.')))
    while (len(ver1) < len(ver2)):
        ver1.append(0)
    while (len(ver2) < len(ver1)):
        ver2.append(0)
    for el1, el2 in zip(ver1, ver2, strict=True):
        if el1 > el2:
            return 1
        elif el1 < el2:
            return -1
    return 0

if __name__ == "__main__":
    ver1 = '1.2.1'
    ver2 = '1.2'
    print(compare(ver1, ver2))