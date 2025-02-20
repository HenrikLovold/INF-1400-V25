if __name__ == "__main__":
    fd = open("index", "r")
    lines = fd.readlines()
    fd.close()
    for line in lines:
        try:
            current_file = open(line.strip(), "r")
        except FileNotFoundError:
            continue
        try:
            content = current_file.read()
        except:
            current_file.close()
            continue
        print(content)
        current_file.close()
