from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# Models to blog page.
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='published')

class Post(models.Model):
	'''Component's information'''
	STATUS_CHOISES = (
			('draft', 'Daft'),
			('published','Published'),
		)

	title 	= models.CharField(max_length=100)
	slug 	= models.SlugField(max_length=100) 
	author  = models.ForeignKey(User, 
								on_delete=models.CASCADE,
								related_name='blog_post')
	body	= models.TextField()

	image	= models.ImageField(upload_to='blog/img', blank=True)
	publish	= models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add =True)
	modified = models.DateTimeField(auto_now=True)

	objects		= models.Manager() # Default manager
	published 	= PublishedManager() # A custom manage

	status 	= models.CharField(max_length=10,
								choices = STATUS_CHOISES,
								default = 'draft')

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title


class Resistors(models.Model):
	''' resistors '''
	SUBCOMPONENT = (
			('general', 'General'),
			('termistor', 'Termistor'),
			('carbon', 'Carbon'),
			('power','Power'),
			('potenciometer', 'Potenciometer'),
			('smd','SMD'),
			('accuracy', 'Accuracy')
		)

	STATUS_CHOISES = (
			('draft', 'Daft'),
			('published','Published'),
		)

	title 	= models.CharField(max_length=100)
	slug 	= models.SlugField(max_length=100) 
	author  = models.ForeignKey(User, 
								on_delete=models.CASCADE,
								related_name='blog_resistor')
	description	= models.TextField()
	features = models.TextField(max_length=1500, blank=True)
	# similar_components = models.TextField(max_length=1500, blank=True)
	aplications = models.TextField(max_length=1500, blank=True)

	image	= models.ImageField(upload_to='blog/img', blank=True)
	image_1	= models.ImageField(upload_to='blog/img', blank=True)
	image_2	= models.ImageField(upload_to='blog/img', blank=True)
	image_3	= models.ImageField(upload_to='blog/img', blank=True)
	image_4	= models.ImageField(upload_to='blog/img', blank=True)

	publish	= models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add =True)
	modified = models.DateTimeField(auto_now=True)
	datasheet = models.URLField(blank = True) 
	division = models.CharField(max_length=15,
								choices = SUBCOMPONENT,
								blank = True)

	status 	= models.CharField(max_length=10,
								choices = STATUS_CHOISES,
								default = 'draft')

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title


class Capacitors(models.Model):
	''' resistors '''
	SUBCOMPONENT = (
			('general', 'General'),
			('ceramic', 'Ceramic'),
			('electrolitic','Electrolitic'),
			('variable', 'Variable'),
			('smd','SMD'),
			('tantalio', 'Tantalio'),
			('polyester', 'Polyester')
		)

	STATUS_CHOISES = (
			('draft', 'Daft'),
			('published','Published'),
		)

	title 	= models.CharField(max_length=100)
	slug 	= models.SlugField(max_length=100) 
	author  = models.ForeignKey(User, 
								on_delete=models.CASCADE,
								related_name='blog_capacitor')
	description	= models.TextField()
	features = models.TextField(max_length=1500, blank=True)
	aplications = models.TextField(max_length=1500, blank=True)

	image	= models.ImageField(upload_to='blog/img', blank=True)
	image_1	= models.ImageField(upload_to='blog/img', blank=True)
	image_2	= models.ImageField(upload_to='blog/img', blank=True)
	image_3	= models.ImageField(upload_to='blog/img', blank=True)
	image_4	= models.ImageField(upload_to='blog/img', blank=True)

	publish	= models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add =True)
	modified = models.DateTimeField(auto_now=True)
	datasheet = models.URLField(blank = True) 
	division = models.CharField(max_length=15,
								choices = SUBCOMPONENT,
								blank = True)

	status 	= models.CharField(max_length=10,
								choices = STATUS_CHOISES,
								default = 'draft')

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title


class Diodes(models.Model):
	''' resistors '''
	SUBCOMPONENT = (
			('general', 'General'),
			('l.e.d', 'L.E.D'),
			('rectifier','Rectifier'),
			('zener', 'Zener'),
			('shottky','Shottky'),
			('device','Device'),
			)

	STATUS_CHOISES = (
			('draft', 'Daft'),
			('published','Published'),
		)

	title 	= models.CharField(max_length=100)
	slug 	= models.SlugField(max_length=100) 
	author  = models.ForeignKey(User, 
								on_delete=models.CASCADE,
								related_name='blog_diode')
	description	= models.TextField()
	features = models.TextField(max_length=1500, blank=True)
	aplications = models.TextField(max_length=1500, blank=True)

	image	= models.ImageField(upload_to='blog/img', blank=True)
	image_1	= models.ImageField(upload_to='blog/img', blank=True)
	image_2	= models.ImageField(upload_to='blog/img', blank=True)
	image_3	= models.ImageField(upload_to='blog/img', blank=True)
	image_4	= models.ImageField(upload_to='blog/img', blank=True)

	publish	= models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add =True)
	modified = models.DateTimeField(auto_now=True)
	datasheet = models.URLField(blank = True) 
	similar_components = models.TextField(max_length=1500, blank=True)
	division = models.CharField(max_length=15,
								choices = SUBCOMPONENT,
								blank = True)

	status 	= models.CharField(max_length=10,
								choices = STATUS_CHOISES,
								default = 'draft')

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title


class Transistors(models.Model):
	''' resistors '''
	SUBCOMPONENT = (
			('general', 'General'),
			('bjt_npn', 'BJT_NPN'),
			('bjt_pnp','BJT_PNP'),
			('device','DEVICE'),
		)

	STATUS_CHOISES = (
			('draft', 'Daft'),
			('published','Published'),
		)

	title 	= models.CharField(max_length=100)
	slug 	= models.SlugField(max_length=100) 
	author  = models.ForeignKey(User, 
								on_delete=models.CASCADE,
								related_name='blog_transistor')
	description	= models.TextField()
	features = models.TextField(max_length=1500, blank=True)
	aplications = models.TextField(max_length=1500, blank=True)

	image	= models.ImageField(upload_to='blog/img', blank=True)
	image_1	= models.ImageField(upload_to='blog/img', blank=True)
	image_2	= models.ImageField(upload_to='blog/img', blank=True)
	image_3	= models.ImageField(upload_to='blog/img', blank=True)
	image_4	= models.ImageField(upload_to='blog/img', blank=True)

	publish	= models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add =True)
	modified = models.DateTimeField(auto_now=True)
	datasheet = models.URLField(blank = True) 
	similar_components = models.TextField(max_length=1500, blank=True)
	division = models.CharField(max_length=15,
								choices = SUBCOMPONENT,
								blank = True)

	status 	= models.CharField(max_length=10,
								choices = STATUS_CHOISES,
								default = 'draft')

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title