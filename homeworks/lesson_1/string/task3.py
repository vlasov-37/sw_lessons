def main():
    print("Удаление символа @ из строки")
    sent = str(input("Введите строку: "))
    if (sent.count("@")):
        sent = sent.replace("@", "")
    else:
        print("Строка не содержит символа @")
    print(sent)

if __name__ == '__main__':
    main()
