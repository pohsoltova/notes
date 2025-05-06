#dictionary
ovoce = {
    "nazev":"jablko",
    "cena":10,
    "fresh":True

}
#výpis z dictionary
print(ovoce["cena"])

#přidání klíčových slov a hodnot
klicoveSlovo = input("zadejte klíčové slovo")
hodnota = input("zadejte hodnotu")

ovoce["obchod"] = "Lidl"
ovoce[klicoveSlovo] = hodnota

#možnosti výpisu
for polozky in ovoce:
    print(polozky)

for polozky2 in ovoce.items():
    print(polozky2)

for klicoveSlovo,hodnota in ovoce.items():
    print(f"{klicoveSlovo}:{hodnota}")