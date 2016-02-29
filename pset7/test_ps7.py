#!/usr/bin/python

from ps7_skeleton import *

adoption_center=AdoptionCenter("SPA",{"Dog": 10, "Cat": 5, "Lizard":3,"Camel":1},(5.0,6.1))
species_dico=adoption_center.get_species_count()
print(species_dico)

#Oki: name, desired spec, list of allergic spec and a dict of med effectiveness
adopter=MedicatedAllergicAdopter("joe","Cat", ("Horse", "Camel", "Dog"), {"Dog":0.5,"Camel":0.0,"Horse":0.98})
#adopter=AllergicAdopter("joe","Cat", ("Horse", "Cat", "Dog"))
score=adopter.get_score(adoption_center)
print(score)
