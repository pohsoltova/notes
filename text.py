while True:
    volba = input("1. pridat novy zapis 2. precist denik 3. ukoncit")
    print(volba)
    if volba == "1":
        input("jak se ted citis?")
        text= input("vypis svuj zapis do deniku")
        with open("denik.txt","a", encoding="utf-8")as soubor:
            soubor.write(text)
    elif volba == "2":
        with open("denik.txt","r", encoding="utf-8")as soubor:
            textZeSouboru = soubor.read()
            print(textZeSouboru)
    elif volba == "3":
        break