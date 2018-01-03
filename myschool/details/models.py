# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
# Create your models here.

class cl(models.Model):
	branch = models.CharField(max_length=10)

	def __str__(self):
		return self.branch

class Teacher(models.Model):
	name_T = models.CharField(max_length=50)
	emails_T= models.EmailField()
	hw = models.TextField(max_length=1000)
	branch=models.ForeignKey(cl,null=False)

	def __str__(self):
		return self.name_T

class Student(models.Model):
	name_S= models.CharField(max_length=50)
	emails_S=models.EmailField()
	rollnumber=models.IntegerField()
	branch=models.ForeignKey(cl,null=False)

	def __str__(self):
		return self.name_S









			


	