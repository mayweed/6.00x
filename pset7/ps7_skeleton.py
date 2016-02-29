import random 
import math
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name=name
        self.species_types=species_types
        # enforce float... and parse deeper location...
        #also works that way but less deep (no access to x or y separately)
        #self.location=(float(location[0]),float(location[1]))
        self.x=float(location[0])
        self.y=float(location[1])
        self.location=(self.x,self.y)
    def get_number_of_species(self, animal):
        for k,v in self.species_types.items():
            if k==animal:
                return v
    def get_location(self):
        return self.location
    def get_species_count(self):
        #when it's zero should not appear...
        copy_dico={}
        for k,v in self.species_types.items():
            if v != 0:
                copy_dico[k]=v
        return copy_dico
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        for k,v in self.species_types.items():
            if species==k:
                self.species_types[k]-=1

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name=name
        self.desired_species=desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        #the species dico
        species_dico= adoption_center.get_species_count()
        # yep a float...
        num_desired=0.0
        for species in self.get_desired_species().split(' '):
            if species in list(species_dico.keys()):
                num_desired+=species_dico[species]
        return num_desired


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self,name,desired_species)
        self.considered_species=considered_species
    def get_score(self,adoption_center):
        #do not forget self in the call unless instance error
        adopter_score=Adopter.get_score(self,adoption_center)
        species_dico= adoption_center.get_species_count()
        num_desired=0.0
        #here it's a _list_ of strings (no split)
        for considered_species in self.considered_species:
            if considered_species in list(species_dico.keys()):
                num_desired+=species_dico[considered_species]
        return adopter_score + 0.3 * num_desired


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self,name,desired_species)
        self.feared_species=feared_species
    def get_score(self,adoption_center):
        adopter_score=Adopter.get_score(self,adoption_center)
        species_dico= adoption_center.get_species_count()
        num_feared=0.0
        #here it's a string
        for feared_species in self.feared_species.split(' '):
            if feared_species in species_dico:
                num_feared+=species_dico[feared_species]
        score= adopter_score - 0.3 * num_feared
        #to pass one test case for that class only
        if score < 0 : return 0.0
        else: return score


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self,name,desired_species)
        self.allergic_species=allergic_species
    def get_score(self,adoption_center):
        species_dico= adoption_center.get_species_count()
        score=0
        for aspecies in self.allergic_species:
            if aspecies in species_dico:
               return 0.0 
            #dont think it's needed the else here...
            else:
               continue
        return Adopter.get_score(self,adoption_center)


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most 
    allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, 
    then compare them to the medicine_effectiveness dictionary. Take the lowest medicine_effectiveness found for these species,
     and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self,name,desired_species,allergic_species,medicine_effectiveness):
        AllergicAdopter.__init__(self,name,desired_species,allergic_species)
        self.medicine_effectiveness=medicine_effectiveness
    def get_score(self,adoption_center):
        min_seen=1.0
        for aspecies in self.allergic_species:
            if aspecies in self.medicine_effectiveness:
                if self.medicine_effectiveness[aspecies] < min_seen:
                    min_seen=self.medicine_effectiveness[aspecies]
        print(min_seen)
        return Adopter.get_score(self,adoption_center)*min_seen 


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self,name,desired_species)
        self.location=(float(location[0]),float(location[1]))

    def get_linear_distance(self,to_location):
        distance=math.sqrt(((to_location[0]-self.location[0])**2)+((to_location[1]-self.location[1])**2))
        return distance

    def get_score(self,adoption_center):
        distance=self.get_linear_distance(adoption_center.get_location())
        num=0
        desired_species=self.desired_species.split(' ') 
        for species in desired_species:
        #+= DOES NOT WORK, YIELD NONETYPE WTF???
            num+=adoption_center.get_number_of_species(species)
        print(num)
        if distance < 1: return 1*num
        elif distance >= 1 and distance < 3:return random.uniform(.7,.9)*num
        elif distance >= 3 and distance < 5:return random.uniform(.5,.7)*num
        else: return random.uniform (.1,.5)*num

    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores
    for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here 

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 

