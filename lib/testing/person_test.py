#!/usr/bin/env python3

import pytest
from person import Person
import io
import sys

class TestPerson:
    '''Test cases for Person class in person.py'''

    @pytest.fixture(autouse=True)
    def capture_output(self):
        self.captured_out = io.StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.captured_out
        yield
        sys.stdout = self.original_stdout

    def test_is_class(self):
        '''Person is a class with the name "Person".'''
        guido = Person(name='Guido', job='Sales')
        assert isinstance(guido, Person), "guido should be an instance of Person"

    def test_name_not_empty(self):
        '''Prints error if name is an empty string.'''
        Person(name="", job="Sales")
        sys.stdout = self.original_stdout  # Ensure stdout is restored for further assertions
        assert self.captured_out.getvalue().strip() == "Name must be string between 1 and 25 characters.", \
            "Expected error message for empty name"

    def test_name_string(self):
        '''Prints error if name is not a string.'''
        Person(name=123, job='Sales')
        sys.stdout = self.original_stdout  # Ensure stdout is restored for further assertions
        assert self.captured_out.getvalue().strip() == "Name must be string between 1 and 25 characters.", \
            "Expected error message for non-string name"

    def test_name_under_25(self):
        '''Prints error if name string is over 25 characters.'''
        Person(name="What do Persons do on their day off? Can't lie around - that's their job.",
               job='Sales')
        sys.stdout = self.original_stdout  # Ensure stdout is restored for further assertions
        assert self.captured_out.getvalue().strip() == "Name must be string between 1 and 25 characters.", \
            "Expected error message for name over 25 characters"

    def test_valid_name(self):
        '''Saves name if string is between 1 and 25 characters.'''
        guido = Person(name="Guido", job="Sales")
        assert guido.name == "Guido", "Expected name to be saved correctly"

    def test_valid_name_title_case(self):
        '''Converts name to title case and saves if between 1 and 25 characters'''
        guido = Person(name="guido van rossum", job="Sales")
        assert guido.name == "Guido Van Rossum", "Expected name to be converted to title case"

    def test_job_not_in_list(self):
        '''Prints error if job is not in the list of approved jobs.'''
        Person(name="Guido", job="Benevolent dictator for life")
        sys.stdout = self.original_stdout  # Ensure stdout is restored for further assertions
        assert self.captured_out.getvalue().strip() == "Job must be in list of approved jobs.", \
            "Expected error message for unapproved job"

    def test_job_in_list(self):
        '''Saves job if it is in the list of approved jobs.'''
        guido = Person(name="Guido", job="ITC")
        assert guido.job == "ITC", "Expected job to be saved correctly"

# To run the tests, use the following command:
# pytest test_person.py
