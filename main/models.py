from django.db import models
from django.utils import timezone

# Create your models here.

class PortfolioModel(models.Model):
	name = models.CharField(max_length=255, blank=True)
	photo = models.ImageField(upload_to='media/images/', blank=True, null=True)
	email = models.CharField(max_length=255, blank=True)
	phone = models.CharField(max_length=255, blank=True)
	address = models.TextField(max_length=1000, blank=True)
	about = models.TextField(max_length=10000, blank=True)
	linkedin = models.CharField(max_length=255, blank=True)
	twitter = models.CharField(max_length=255, blank=True)
	github = models.CharField(max_length=255, blank=True)
	the_date = models.DateField(default=timezone.now, blank=True)

	def __str__(self):
		return f'{self.name} {self.email}'


class ExperienceModel(models.Model):
	position = models.CharField(max_length=255, blank=True)
	company = models.CharField(max_length=255, blank=True)
	about = models.TextField(max_length=1000, blank=True)
	start = models.CharField(max_length=255, blank=True)
	end = models.CharField(max_length=255, blank=True)
	show_first = models.IntegerField(default=1)

	def __str__(self):
		return 


class ProjectModel(models.Model):
	name = models.CharField(max_length=255, blank=True)
	photo = models.ImageField(upload_to='media/images/', blank=True, null=True)
	about = models.TextField(max_length=1000, blank=True)
	start = models.CharField(max_length=255, blank=True)
	end = models.CharField(max_length=255, blank=True)
	show_first = models.IntegerField(default=1)

	def __str__(self):
		return f'{self.name} {self.about[:50]}'


class EducationModel(models.Model):
	school = models.CharField(max_length=255, blank=True)
	degree = models.CharField(max_length=255, blank=True)
	gpa = models.CharField(max_length=255, blank=True)
	about = models.TextField(max_length=1000, blank=True)
	start = models.CharField(max_length=255, blank=True)
	end = models.CharField(max_length=255, blank=True)
	show_first = models.IntegerField(default=1)

	def __str__(self):
		return f'{self.school} {self.degree} {self.gpa} {self.about[:50]}'


class LanguageToolsModel(models.Model):
	css_class = models.CharField(max_length=255, blank=True)
	show_first = models.IntegerField(default=1)

	def __str__(self):
		return self.css_class


class WorkflowModel(models.Model):
	about = models.TextField(max_length=1000, blank=True)
	show_first = models.IntegerField(default=1)

	def __str__(self):
		return self.about[:50]


class InterestsModel(models.Model):
	about = models.TextField(max_length=1000, blank=True)
	show_first = models.IntegerField(default=1)

	def __str__(self):
		return self.about[:50]
