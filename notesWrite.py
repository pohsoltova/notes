#write - otevře soubor vše smaže a připíše něco nového
with open("denik.txt","w", encoding="utf-8")as soubor:
    soubor.write("w připisuje text do souboru ale původní to maže")

#append - otevře soubor a připíše něco nového
with open("denik.txt","a", encoding="utf-8")as soubor:
    soubor.write("a připisuje text do souboru a původní ponechá")

#read - otevře soubor a vše přečte
with open("denik.txt","r", encoding="utf-8")as soubor:
    textZeSouboru = soubor.read()
    print(textZeSouboru)

