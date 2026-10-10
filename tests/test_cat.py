import unittest

from src.cat_breed import CatBreed

class TestCat(unittest.TestCase):
    def setUp(self):
        print("\nCat test ...")

        # CatBreed with all attributes 
        self.cat1 = CatBreed("Cat", "Norwegian Forest Cat", "Large", "6-10kg", "Long", "Medium", "Norwegian Forest Cats are known for their gentle and friendly temperament",  "The average lifespan of a Norwegian Forest Cat ranges from 12 to 16 years.", "White, black, blue, red, cream and silver, plus various patterns and shadings")

        # CatBreed with only required attributes added
        self.cat2 = CatBreed("Cat", "Ragdoll", "Medium", "4-9kg" )

    def test_if_Cat_exists(self):
        # self.assertIsInstance(self.cat1, CatBreed)
        self.assertIsInstance(self.cat2, CatBreed)

    def test_optional_attributes(self):
        self.assertEqual(self.cat1.coat, "Long")
        self.assertEqual(self.cat2.coat, "")