def main():
    print("Замена подстроки")
    sent = str(input("Введите строку: "))
    sent = sent.replace("1", "one")
    print(sent)

if __name__ == '__main__':
    main()
