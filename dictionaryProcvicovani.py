<<<<<<< HEAD
znamky={
    "anna":[4,2,5], "josef":[5,2,1]
}

studenti={
    "anna":{"vek":16, "trida":"1.A","znamky":{"matika":[1,2,3], "čeština":[2,4,5]}}
}
trida= studenti["anna"]["trida"]
print(trida)

znamky = studenti["anna"]["znamky"]["matika"]
soucet =sum(znamky)
prumer = soucet/3
print(prumer)




filmy ={
    "maska":{"herec": "jim carrey"}, "prelet nad kukaccim hnizdem":{"reziser":"milos forman", "zanr":"absolutni psycho"}, "scary movie":{"zanr":"komedie"}, "ace ventura":{"herec":"jim carrey", "zanr":"komedie"}
    
}
print(filmy["maska"]["herec"])
=======
znamky={
    "anna":[4,2,5], "josef":[5,2,1]
}

studenti={
    "anna":{"vek":16, "trida":"1.A","znamky":{"matika":[1,2,3], "čeština":[2,4,5]}}
}
trida= studenti["anna"]["trida"]
print(trida)

znamky = studenti["anna"]["znamky"]["matika"]
soucet =sum(znamky)
prumer = soucet/3
print(prumer)




filmy ={
    "maska":{"herec": "jim carrey"}, "prelet nad kukaccim hnizdem":{"reziser":"milos forman", "zanr":"absolutni psycho"}, "scary movie":{"zanr":"komedie"}, "ace ventura":{"herec":"jim carrey", "zanr":"komedie"}
    
}
print(filmy["maska"]["herec"])
>>>>>>> f3cb7ba59d81e12a52263a973b95e58b7cf7b2b5
print(filmy["prelet nad kukaccim hnizdem"]["zanr"])