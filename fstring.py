rok = 2025
text = "vesele velikonoce"
cislo = 52168486
# f string
print(f"ahoj {text} {rok}")
# rozdelovac cisel
print(f"{cislo:,}")

# vypsat pocet pismen
print(f"{text:.6}")

#desetinna cisla
print(f"{cislo:.3f}")

#prevody jednotek
hodnota = 155
print(f"{hodnota:b}")
print(f"{hodnota:x}")

jmeno = input("zadej jmeno")
vek = input("zadej vek")
print(f"ahoj jmenuju se {jmeno} a je mi {vek}")

cislo1 = float(input("zadej desetinne cislo"))
cislo2 = float(input("zadej desetinne cislo"))
soucet = float(cislo1) + float(cislo2)
print(f"{soucet:.2f}")
podil = int(cislo1) / int(cislo2)
print(f"{podil:.2f}")
soucin = int(cislo1) + int(cislo2)
print(f"{soucin:.2f}")
rozdil = int(cislo1) - int(cislo2)
print(f"{rozdil:.2f}")
