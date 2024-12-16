def write_to_file(filename: str, text: str):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print("Я записал")


def read_file(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
    print("Я прочитал")


if __name__ == "__main__":
    filename = "123.txt"
    text = "Привет Путон я Саша"
    # write_to_file(filename=filename,text=text)
    read_file(filename=filename)
