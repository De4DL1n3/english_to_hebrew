def main():
    strEng = input("English String: \n")
    print(f"Your fixed Hebrew text is: {switchLetters(strEng)}")

def switchLetters(strEng):
    list_eng_lc = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/','\n',' ']
    list_eng_uc = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/','\n',' ']
    list_heb = ['/', "'", 'ק', 'ר', 'א', 'ט', 'ו', 'ן', 'ם', 'פ', 'ש', 'ד', 'ג', 'כ', 'ע', 'י', 'ח', 'ל', 'ך', 'ף', ',', 'ז', 'ס', 'ב', 'ה', 'נ', 'מ', 'צ', 'ת', 'ץ', '.','\n',' ']
    strFixed = ""
    for i in range(len(strEng)):
        if strEng[i] in list_eng_lc:
            strFixed += list_heb[list_eng_lc.index(strEng[i])]
        elif strEng[i] in list_eng_uc:
            strFixed += list_heb[list_eng_uc.index(strEng[i])]
    return strFixed

if __name__ == "__main__":
    main()
