def main():
    print("Замена внутри фрагмента")
    sent = str(input("Введите строку: "))
    h_1 = sent.find("h") + 1 #убираем первую h из границы фрагмента
    h_2 = sent.rfind("h")
    h_middle = sent[h_1:h_2].replace("h", "H")
    new_sent = sent[:h_1] + h_middle + sent[h_2:]
    print("Строка с изменённым фрагментом = " + new_sent)

if __name__ == '__main__':
    main()
