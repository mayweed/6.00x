#!/usr/bin/python

from ps7_skeleton import *

#PART 1
#adoption_center=AdoptionCenter("SPA",{"Dog": 10, "Cat": 5, "Lizard":3,"Camel":1},(5.0,6.1))
#species_dico=adoption_center.get_species_count()
#print(species_dico)

#PART 2
#Oki: name, desired spec, list of allergic spec and a dict of med effectiveness
#adopter=MedicatedAllergicAdopter("joe","Cat", ("Horse", "Camel", "Dog"), {"Dog":0.5,"Camel":0.0,"Horse":0.98})
#adopter=AllergicAdopter("joe","Cat", ("Horse", "Cat", "Dog"))
#score=adopter.get_score(adoption_center)
#print(score)

#adopter=SluggishAdopter("joe","Horse Cat Dog",(5.0,6.1)) 
#d=adopter.get_linear_distance(adoption_center.get_location())
#s=adopter.get_score(adoption_center)
#print(d,s)

#PART 3
adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'],{"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))
#3.1
# how to test get_ordered_adoption_center_list
get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])
# you can print the name and score of each item in the list returned
#print(isinstance(adopter,FearfulAdopter)) # ==> yield False!!
