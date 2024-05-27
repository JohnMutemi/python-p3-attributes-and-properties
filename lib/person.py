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
    def __init__(self, name='John Doe', job='Admin'):
        self._name = None
        self._job = None
        self.name = name
        self._set_job_without_print(job)  # Set job without printing

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print('Name must be string between 1 and 25 characters.')

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print('Job must be in the list of approved jobs.')

    def _set_job_without_print(self, job):
        """Sets the job without printing (used in __init__)."""
        if job in APPROVED_JOBS:
            self._job = job
        else:
            self._job = "Admin"

    job = property(get_job, set_job)
