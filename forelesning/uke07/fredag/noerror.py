if __name__ == "__main__":
    fd = open("index", "r")
    lines = fd.readlines()
    fd.close()
    for line in lines:
        current_file = open(line.strip(), "r")
        content = current_file.read()
        print(content)
        current_file.close()

