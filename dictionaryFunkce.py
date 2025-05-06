
def vytvor_utulek():
    return {}

def pridej_zvire(utulek, jmeno, druh, vek):
    utulek[jmeno] = {"druh": druh, "vek": vek}

def vypis_zvirata(utulek):
    for jmeno, info in utulek.items():
        print(f"{jmeno} je {info['druh']} a je mu {info['vek']} let.")


if __name__ == "__main__":
    utulek = vytvor_utulek()
    pridej_zvire(utulek, "Míca", "kočka", 3)
    pridej_zvire(utulek, "Baryk", "pes", 5)
    pridej_zvire(utulek, "Kája", "králík", 2)

    print("Všechna zvířata v útulku:")
    vypis_zvirata(utulek)

