import unittest

# running tests from root Assignment3/
from src.dog_breed import DogBreed

class TestDog(unittest.TestCase):

    def setUp(self):
        print("\nDog test ...")

        # DogBreed with all attributes added
        self.dog1 = DogBreed("Dog", "Alaskan Malimut", "Giant", "38-56kg", "Medium", "High", "Alaskan Malamutes are known for their friendly and affectionate temperament",  "The average lifespan of an Alaskan Malamute is around 10 to 14 years.", "Agility, Dog Sledding, Obedience, Rally Obedience, Therapy")

        # DogBreed with only required attributes added
        self.dog2 = DogBreed("Dog", "Border Collie", "Medium", "14-20kg" ) 

    def test_if_dog_exists(self):
        self.assertIsInstance(self.dog1, DogBreed)
        self.assertIsInstance(self.dog2, DogBreed)

    def test_optional_attributes(self):
        self.assertEqual(self.dog1.coat, "Medium")
        self.assertEqual(self.dog2.coat, "")