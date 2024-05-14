#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name: str, job: str):
        self.set_name(name)
        self.set_job(job)

    def set_name(self, name: str):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name.title()

    def set_job(self, job: str):
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self.job = job

# Example usage:
# person = Person(name="guido van rossum", job="ITC")
# print(person.name)  # Should print "Guido Van Rossum"
# print(person.job)  # Should print "ITC"

# This will trigger the name validation
# person_invalid_name = Person(name="", job="ITC")

# This will trigger the job validation
# person_invalid_job = Person(name="Guido", job="Benevolent dictator for life")
