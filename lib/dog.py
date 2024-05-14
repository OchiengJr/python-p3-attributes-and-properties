#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name: str, breed: str):
        self.set_name(name)
        self.set_breed(breed)

    def set_name(self, name: str):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name

    def set_breed(self, breed: str):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self.breed = breed

# Example usage:
# dog = Dog(name="Fido", breed="Pug")
# print(dog.name)  # Should print "Fido"
# print(dog.breed)  # Should print "Pug"

# This will trigger the name validation
# dog_invalid_name = Dog(name="", breed="Pug")

# This will trigger the breed validation
# dog_invalid_breed = Dog(name="Fido", breed="Human")
