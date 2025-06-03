
moznosti = ["stastne", "smutne", "znudene", "nastvane", "okay", "znechucene", "uzkostne", "unavene", "plny energie"]
print(moznosti)
mood = input("jak se dneska mame?")
if mood == "stastne":
    print("skvely, uzivej si dnesni den")
elif mood == "smutne":
    print("to me mrzi, zkus se nekomu vypovidat nebo si zapsat sem sve emoce")
    input()
elif mood == "znudene":
    dotaz = input("zahrajeme si hru? ano/ne")
    if dotaz == "ano":
        import random
        def hadani_cisla():
            print("Vítej ve hře: Hádej číslo!")
            cislo = random.randint(1, 20)
            pokusy = 0

            while True:
                tip = input("Hádej číslo mezi 1 a 20: ")

                if not tip.isdigit():
                    print("Zadej platné číslo!")
                    continue

                tip = int(tip)
                pokusy += 1

                if tip < cislo:
                    print("Moc nízko!")
                elif tip > cislo:
                    print("Moc vysoko!")
                else:
                    print(f"Správně! Uhodl jsi číslo za {pokusy} pokusů.")
    hadani_cisla()



elif mood == "nastvane":
    print("odreaguj se, zkus delat neco tvurciho a bud sam")
elif mood == "okay":
    print("to jsem rad")
elif mood == "znechucene":
        print("zapal si svicku, mysli na neco jineho")
elif mood == "uzkostne":
        print("hlavne dychej a vypovidej se nebo se vybrec")
        input()
elif mood == "unavene":
    print("bez spat, spanek je dulezity a zaslouzis si to")
elif mood == "plny energie":
    print("krasa, bez si zacvicit treba")
else: 
    print("tohle neznam")