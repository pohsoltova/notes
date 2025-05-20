

def ziskej_prichute(pocet):
    prichute = []
    for i in range(pocet):
        prichut = input(f"Zadej příchuť číslo {i+1}: ")
        prichute.append(prichut)
    return prichute

def vypis_vrstvy_dortu(pocet_vrstev, prichute):
    print("Vrstvy dortu:")
    for i in range(pocet_vrstev):
        prichut = prichute[i % len(prichute)]
        print(f"Vrstva {i+1}: {prichut}")

def shrnuti(jmeno, pocet_vrstev, prichute):
    print(f"{jmeno} vytvořil dort s {pocet_vrstev} vrstvami a příchutěmi: {', '.join(prichute)}.")

def ozdob_dort():
    ozdoby = input("\nChceš dort ozdobit? (můžeš zadat více ozdob, odděluj čárkami): ")
    ozdoby_list = [ozdoba.strip() for ozdoba in ozdoby.split(",") if ozdoba.strip()]
    print(f"Tvoje dort je ozdobený: {', '.join(ozdoby_list)}!")

def hlavni():
    print("Ahoj! Jak se jmenuješ?")
    jmeno = input("> ")

    pocet_vrstev = int(input("\nKolik vrstev má mít tvůj dort?\n> "))
    pocet_prichuti = int(input("\nKolik různých příchutí chceš použít?\n> "))

    prichute = ziskej_prichute(pocet_prichuti)
    vypis_vrstvy_dortu(pocet_vrstev, prichute)
    shrnuti(jmeno, pocet_vrstev, prichute)
    ozdob_dort()

hlavni()
