
from django.db import models

# Create your models here.
from django.db import models
class Human(models.Model):

    YEAR_IN_COLLEGE_CHOICES = [
    ('1', '1st Year'),
    ('2', '2nd Year'),
    ('3', '3rd Year'),
    ('4', '4th Year'),
    ('P', 'Passout'),
    ]

    BRANCH = [
    ('CSE', 'CSE'),
    ('IT', 'IT'),
    ('AI/DS', 'AI/DS'),
    ('ECE', 'ECE'),
    ('MECH', 'MECH'),
    ('CIVIL', 'CIVIL'),
    ('EEE', 'EEE'),
    ]

    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=60)
    college = models.CharField(max_length=60)
    year = models.CharField(max_length=1, choices=YEAR_IN_COLLEGE_CHOICES)
    branch = models.CharField(max_length=5, choices=BRANCH)
    nlp = models.TextField()

    def __str__(self):
        return self.name
