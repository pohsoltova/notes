import random
for i in range(10):
    moznosti = ["kolo","mic","kocku","psa","hru","obleceni","sperky"]

   
  
    
    osoba1 = random.choice(moznosti)
    osoba2 = random.choice(moznosti)
    
    if osoba1 == osoba2:
        print(f"ne kupme jiny {osoba1}")
    print(f"koupime {osoba1}")
    print(f"ne koupime {osoba2}")