from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cust(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=15)

class Review(models.Model):
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    comment=models.CharField(max_length=1000, blank=True,null=True)
    satisfaction=models.CharField(max_length=20)

class Heart(models.Model):
    age=models.IntegerField()
    sex=models.IntegerField()
    cp=models.IntegerField()
    trestbps=models.IntegerField()
    chol=models.IntegerField()
    fbs=models.IntegerField()

    restecg=models.IntegerField()
    thalach=models.IntegerField()
    exang=models.IntegerField()

    oldpeak=models.IntegerField()
    slope=models.IntegerField()
    ca=models.IntegerField()
    thal=models.IntegerField()
    target=models.IntegerField(null=True,blank=True)
    def to_dict(self):
        return {
            'age':self.age,
            'sex':self.sex,
            'cp':self.cp,
            'trestbps':self.trestbps,
            'chol':self.chol,
            'fbs':self.fbs,
            'restecg':self.restecg,
            'thalach':self.thalach,
            'exang':self.exang,
            'oldpeak':self.oldpeak,
            'slope':self.slope,
            'ca':self.ca,
            'thal':self.thal,
            'target':self.target
        }
