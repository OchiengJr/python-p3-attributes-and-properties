#!/usr/bin/env python3

import pytest
from dog import Dog
import io
import sys

class TestDog:
    '''Test cases for Dog class in dog.py'''

    @pytest.fixture(autouse=True)
    def capture_output(self):
        self.captured_out = io.StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.captured_out
        yield
        sys.stdout = self.original_stdout

    def test_is_class(self):
        '''Dog is a class with the name "Dog".'''
        fido = Dog()
        assert isinstance(fido, Dog), "fido should be an instance of Dog"

    def test_name_not_empty(self):
        '''Prints error if name is an empty string.'''
        Dog(name="")
        sys.stdout = self.original_stdout  # Ensure stdout is restored for further assertions
        assert self.captured_out.getvalue().strip() == "Name must be string between 1 and 25 characters.", \
            "Expected error message for empty name"

    def test_name_string(self):
        '''Prints error if name is not a string.'''
        Dog(name=123)
        sys.stdout = self.original_stdout  # Ensure stdout is restored for further assertions
        assert self.captured_out.getvalue().strip() == "Name must be string between 1 and 25 characters.", \
            "Expected error message for non-string name"

    def test_name_under_25(self):
        '''Prints error if name string is over 25 characters.'''
        Dog(name="What do dogs do on their day off? Can't lie around - that's their job.")
        sys.stdout = self.original_stdout  # Ensure stdout is restored for further assertions
        assert self.captured_out.getvalue().strip() == "Name must be string between 1 and 25 characters.", \
            "Expected error message for name over 25 characters"

    def test_valid_name(self):
        '''Saves name if string is between 1 and 25 characters.'''
        fido = Dog(name="Fido")
        assert fido.name == "Fido", "Expected name to be saved correctly"

    def test_breed_not_in_list(self):
        '''Prints error if breed is not in the list of approved breeds.'''
        Dog(breed="Human")
        sys.stdout = self.original_stdout  # Ensure stdout is restored for further assertions
        assert self.captured_out.getvalue().strip() == "Breed must be in list of approved breeds.", \
            "Expected error message for unapproved breed"

    def test_breed_in_list(self):
        '''Saves breed if it is in the list of approved breeds.'''
        fido = Dog(breed="Pug")
        assert fido.breed == "Pug", "Expected breed to be saved correctly"

# To run the tests, use the following command:
# pytest test_dog.py
