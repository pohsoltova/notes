
def vytvor_utulek():
    return {}

# 2. Přidání zvířete do útulku
def pridej_zvire(utulek, jmeno, druh, vek):
    utulek[jmeno] = {"druh": druh, "vek": vek}

# 3. Výpis všech zvířat
def vypis_zvirata(utulek):
    for jmeno, info in utulek.items():
        print(f"{jmeno} je {info['druh']} a je mu {info['vek']} let.")


# 5. Zavolání funkcí pro ověření
if __name__ == "__main__":
    utulek = vytvor_utulek()
    pridej_zvire(utulek, "Míca", "kočka", 3)
    pridej_zvire(utulek, "Baryk", "pes", 5)
    pridej_zvire(utulek, "Kája", "králík", 2)

    print("Všechna zvířata v útulku:")
    vypis_zvirata(utulek)

