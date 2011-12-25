from django.db import models

class Question(models.Model):
	text = models.CharField(max_length=500)
	answer = models.CharField(max_length=100)
	
	def __unicode__(self):
		return u'%s' % self.text

class Tema(models.Model):
	name = models.CharField(max_length=100)
	teacher = models.CharField(max_length=200)
	
	def __unicode__(self):
		return u'%s' % self.name

class Test(models.Model):
	test_id = models.CharField(max_length=50)
	tema = models.ForeignKey(Tema)
	questions = models.ManyToManyField(Question)
	
	def __unicode__(self):
		return u'%s' % self.test_id
	
class TestResult(models.Model):
	test_id = models.CharField(max_length=50)
	result = models.IntegerField()
	
	def __unicode__(self):
		return u'%s, mark: %i' % (self.test_id, self.result)
	
class Practice(models.Model):
	name = models.CharField(max_length=100)
	is_done = models.BooleanField()
	
	def __unicode__(self):
		return u'%s' % self.name
	
class Lecture(models.Model):
	name = models.CharField(max_length=100)
	is_read = models.BooleanField()
	
	def __unicode__(self):
		return u'%s' % self.name

	
class DE(models.Model):
	lectures = models.ManyToManyField(Lecture)
	practics = models.ManyToManyField(Practice)
	tests = models.ManyToManyField(TestResult)
	tema = models.ForeignKey(Tema)
	
	def __unicode__(self):
		return u'%s' % self.tema.name

class Student(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	de = models.ManyToManyField(DE)
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)
	
class Group(models.Model):
	spec = models.CharField(max_length=5)
	year = models.CharField(max_length=2)
	students = models.ManyToManyField(Student)
	
	def __unicode__(self):
		return u'%s-%s' % (self.spec, self.year)
	
	
