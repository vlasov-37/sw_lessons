def main():
    print("Удаление всех символов с индексами // 3")
    sent = str(input("Введите строку: "))
    new_sent = ""
    for i in range(0, len(sent), 3):
        first = len(new_sent) + 1
        second = i - 1
        print(i, sent[first], sent[second])
        new_sent += sent[first:second]
    print(new_sent)

if __name__ == '__main__':
    main()
