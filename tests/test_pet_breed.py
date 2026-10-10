import unittest

from src.pet_breed import PetBreed

class TestPetBreed(PetBreed):
    # inherits constructor from PetBreed
    # pass 
    # Can't instantiate abstract class TestPetBreed without 
    # an implementation for abstract method 'display_breed_info'
    def display_breed_info(self):
        pass

class TestPetBreedConstructor(unittest.TestCase):

    def test_pet_breed_constructor(self):
        # inherited constructor inits attr on TestPetBreed class
        pet = TestPetBreed("Dog", "Border Collie", "Medium", "14-20kg")
        # test inherited attribute values
        self.assertEqual(pet.type, "Dog")
        self.assertEqual(pet.name, "Border Collie")
        self.assertEqual(pet.size, "Medium")
        self.assertEqual(pet.weight, "14-20kg")
        self.assertEqual(pet.coat, "")
        self.assertEqual(pet.energy, "")
        self.assertEqual(pet.temperament, "")
        self.assertEqual(pet.lifespan, "")