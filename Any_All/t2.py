if __name__ == "__main__":
    filenames = ["dsdsa.py", "file.txt", "app.exe", "file.bin"]
    ext = "exe"
    if any(filenames[i].split('.')[1] == ext for i in range(len(filenames))):
        print(ext, "есть")
    else: print(ext, "нет")