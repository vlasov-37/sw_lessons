def main():
    print("Обращение фрагмента")
    sent = str(input("Введите строку: "))
    h_1 = sent.find("h")
    h_2 = sent.rfind("h")
    h_middle = sent[h_2:h_1:-1]
    reverse_sent = sent[:h_1] + h_middle + sent[h_2:]
    print("Строка с обращённым фрагментом = " + reverse_sent)

if __name__ == '__main__':
    main()
