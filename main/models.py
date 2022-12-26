from django.db import models
from django.utils import timezone

# Create your models here.


class PortfolioModel(models.Model):
	name = models.CharField(max_length=255, blank=True)
	photo = models.ImageField(upload_to='images/', blank=True, null=True)
	email = models.CharField(max_length=255, blank=True)
	phone = models.CharField(max_length=255, blank=True)
	address = models.TextField(max_length=1000, blank=True)
	about = models.TextField(max_length=10000, blank=True)
	website = models.URLField(blank=True)
	linkedin = models.URLField(blank=True)
	twitter = models.URLField(blank=True)
	github = models.URLField(blank=True)
	the_date = models.DateField(default=timezone.now, blank=True)

	def __str__(self):
		return f'{self.name} {self.email}'


class ExperienceModel(models.Model):
	position = models.CharField(max_length=255, blank=True)
	company = models.CharField(max_length=255, blank=True)
	url = models.URLField(blank=True)
	about = models.TextField(max_length=1000, blank=True)
	start = models.CharField(max_length=255, blank=True)
	end = models.CharField(max_length=255, blank=True)
	show_first = models.IntegerField(default=1)

	def about_split(self):
		about = self.about
		if isinstance(about, str):
			sentences = about.split('\n')
			no_empty_str = filter(lambda i: i not in {'\r', '', '\n'}, sentences)
			return no_empty_str
		return []

	def __str__(self):
		return self.company


class ProjectModel(models.Model):
	name = models.CharField(max_length=255, blank=True)
	url = models.URLField(blank=True)
	photo = models.ImageField(upload_to='images/', default='/main/static/assets/img/profile.jpg', blank=True, null=True)
	about = models.TextField(max_length=1000, blank=True)
	start = models.CharField(max_length=255, blank=True)
	end = models.CharField(max_length=255, blank=True)
	show_first = models.IntegerField(default=1)

	def about_split(self):
		about = self.about
		if isinstance(about, str):
			sentences = about.split('\n')
			no_empty_str = filter(lambda i: i not in {'\r', '', '\n'}, sentences)
			return no_empty_str
		return []

	def __str__(self):
		return f"name: {self.name} - show first: {self.show_first} - about: {self.about[:50]}"


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
	# css_class = models.CharField(max_length=255, blank=True)
	name = models.CharField(max_length=255, blank=True)
	show_first = models.IntegerField(default=1)

	def __str__(self):
		return f"name: {self.name} - show_first: {self.show_first}"


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


class OthersModel(models.Model):
	header = models.CharField(max_length=255, blank=True)
	photo = models.ImageField(upload_to='images/', blank=True, null=True)
	about = models.TextField(max_length=1000, blank=True)
	show_first = models.IntegerField(default=1)
	date = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return f'{self.header[:50]} - {self.about[:50]}'
