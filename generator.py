def vytvor_prezdivku(jmeno, barva, zvire):
    prezdivka = [jmeno[0]+jmeno[1]+jmeno[2]+barva[len(barva)-1]+zvire[0]+zvire[1]]
    print(prezdivka)


if __name__ == "__main__":
    vytvor_prezdivku("mnau","modra","lama")
