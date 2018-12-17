myTuple = ("valeur1","valeur2","valeur3","etc") # Tableau en lecture seule, plus performant
myList = ["valeur1","valeur2","valeur3","etc"] # Tableau aussi, mais en RW
myDict = {
    "Name": "Brissard",
    "Surname": "Gaetan",
    "Age": 23
} # Encore un tableau, JSON style !

"""
for i in myTuple: # Parcour d'un tableau
    print i

print myDict["Age"] # Appel d'une valeur dans un dict

myList[2:] # Les deux premiers éléments
myList[:2] # Tout sauf les deux premiers éléments
myList[-1] # Dernier élément
myList[:-1] # Tout sauf le dernier

"""

myList.append("test")
print myList