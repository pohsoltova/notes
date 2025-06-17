while True:
    vaha = input("zadej vahu kocky")
    davka = int(vaha) * 30 + 70
    print(f"Kočka váží {vaha} kg a měla by dostat {davka} gramů krmení denně.")
    y = input("chces dalsi kocku?")
    if y == "ne":
        break

