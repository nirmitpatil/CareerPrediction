from django.db import models

# Create your models here.
class Tests(models.Model):
    Test_Id = models.IntegerField()
    Question = models.TextField()
    Option = models.TextField(default=0)
    Answer =models.CharField(max_length=10)
    
class General_Test(models.Model):
    Test_Id = models.IntegerField()
    Question = models.TextField()
    Option = models.TextField(default=0)
    Answer =models.CharField(max_length=10)

class Advance_Test(models.Model):
    Test_Id = models.IntegerField()
    Test_Section = models.IntegerField()
    Question = models.TextField()
    Option = models.TextField(default=0)
    Answer =models.CharField(max_length=10)


class College(models.Model):
    section = models.IntegerField()
    C_name = models.TextField()
    C_img = models.TextField(default="https://upload.wikimedia.org/wikipedia/commons/1/1a/Chapin_Hall%2C_Williams_College_-_Williamstown%2C_Massachusetts.jpg")
    nirf = models.IntegerField()
    rating = models.TextField()
    fee = models.TextField()
    salary = models.TextField()
    C_web = models.TextField()
    C_details = models.TextField()
    Placements = models.TextField(default="4.0")
    Infrastructure = models.TextField(default="4.0")
    Faculty_Course_Curriculum = models.TextField(default="4.0")
    Crowd_Campus_Life = models.TextField(default="4.0")
    Value_for_Money = models.TextField(default="4.0")


class Review(models.Model):
    C_id = models.IntegerField()
    name = models.TextField()
    designation = models.TextField()
    rate = models.TextField()
    comment = models.TextField()
