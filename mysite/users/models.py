from django.db import models

class Username(models.Model):
    email = models.CharField(max_length=200)
    userpassword = models.CharField(max_length=200)
    recovery_question = models.CharField(max_length=200)
    recovery_answer = models.CharField(max_length=200)

class PersonalDetails(models.Model):
    id_number = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)  
    user = models.ForeignKey(Username, on_delete=models.CASCADE)

class Course(models.Model):
    course_text = models.CharField(max_length=200)
    course_code = models.CharField(max_length=200)
    course_desc = models.CharField(max_length=200)    

class Choices(models.Model):
    #year_of_study = models.DateTimeField(max_length=)
    wits_choice1 = models.CharField(max_length=20)
    wits_choice2 = models.CharField(max_length=20)
    wits_choice3 = models.CharField(max_length=20)
    uj_choice1 = models.CharField(max_length=20)
    uj_choice2 = models.CharField(max_length=20)
    user = models.ForeignKey(Username, on_delete=models.CASCADE)

    





#class AcademicDetails(models.Model):
    
    

# Create your models here.
