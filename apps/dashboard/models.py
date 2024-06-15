from django.db import models
from django.urls import reverse

# class Year(models.Model):
# 	# How to define the week..

# 	month = models.ForeignKey('Month', on_delete=models.PROTECT, null=True)
# 	year = models.ForeignKey('Year', on_delete=models.PROTECT, null=True)

# 	location = models.ManyToManyField('Location', on_delete=models.SET_NULL, null=True)

# 	experience = models.ManyToManyField('Experience', on_delete=models.SET_NULL, null=True)

# 	log = models.TextField(max_length=1000)

# 	def __str__(self):
#         """String for representing the Model object."""
#         return self.title

#     def get_absolute_url(self):
#         """Returns the URL to access a detail record for this week."""
#         return reverse('week-detail', args=[str(self.id)])


# class Month(models.Model):
# 	# How to define the week..

# 	month = models.ForeignKey('Month', on_delete=models.PROTECT, null=True)
# 	year = models.ForeignKey('Year', on_delete=models.PROTECT, null=True)

# 	location = models.ManyToManyField('Location', on_delete=models.SET_NULL, null=True)

# 	experience = models.ManyToManyField('Experience', on_delete=models.SET_NULL, null=True)

# 	log = models.TextField(max_length=1000)

# 	def __str__(self):
#         """String for representing the Model object."""
#         return self.title

#     def get_absolute_url(self):
#         """Returns the URL to access a detail record for this week."""
#         return reverse('week-detail', args=[str(self.id)])


class Week(models.Model):
	# How to define the week..
	week_num = models.IntegerField()

	start_date = models.DateField()
	end_date = models.DateField()

	# week_of_month = models.IntegerField()
	# month = models.ForeignKey('Month', on_delete=models.PROTECT, null=True)
	# year = models.ForeignKey('Year', on_delete=models.PROTECT, null=True)

	location = models.ManyToManyField('LocationInstance', blank=True, null=True)

	experience = models.ManyToManyField('ExperienceInstance', blank=True)

	log = models.TextField(max_length=1000, blank=True)

	def __str__(self):
		"""String for representing the Model object."""
		return f'Week {self.id}'

	def get_absolute_url(self):
		"""Returns the URL to access a detail record for this week."""
		return reverse('week-detail', args=[str(self.id)])

	def get_location_l_color(self):
		if self.location.filter(location_type__exact = 'l').count() == 0:
			""" if the week is not associated with any l location instance """
			loc = LocationInstance.objects.all().filter(location_type__exact = 'l', start_date__lte=self.start_date, end_date__gte=self.start_date).first()
			if loc is not None:
				self.location.add(loc)
			
			else:
				""" if the current l location instance is not yet updated """
				latest_loc = LocationInstance.objects.all().filter(location_type__exact = 'l', start_date__lte=self.end_date).order_by('-end_date').first()
				latest_loc.end_date = self.end_date
				latest_loc.save()
				self.location.add(latest_loc)

		return self.location.all().filter(location_type__exact = 'l').first().location.base_color

	def get_location_l_color_highlight(self):
		if self.location.filter(location_type__exact = 'l').count() == 0:
			""" if the week is not associated with any l location instance """
			loc = LocationInstance.objects.all().filter(location_type__exact = 'l', start_date__lte=self.start_date, end_date__gte=self.start_date).first()
			
			if loc is not None:
				self.location.add(loc)
			
			else:
				""" if the current l location instance is not yet updated """
				latest_loc = LocationInstance.objects.all().filter(location_type__exact = 'l', start_date__lte=self.end_date).order_by('-end_date').first()
				latest_loc.end_date = self.end_date
				latest_loc.save()
				self.location.add(latest_loc)

		return self.location.all().filter(location_type__exact = 'l').first().location.highlight_color

	def get_experience_color(self):
		if self.experience.count() == 0:
			""" if the week is not associated with any l location instance """
			exp = ExperienceInstance.objects.all().filter(start_date__lte=self.start_date, end_date__gte=self.start_date).order_by("experience_type").first()
			if exp is None:
				return "#f4f4f4"
			
			else:
				self.experience.add(exp)

		return self.experience.all().first().base_color

	def get_experience_color_highlight(self):
		if self.experience.count() == 0:
			""" if the week is not associated with any l location instance """
			exp = ExperienceInstance.objects.all().filter(start_date__lte=self.start_date, end_date__gte=self.start_date).order_by("experience_type").first()
			if exp is None:
				return "#999999"
			
			else:
				self.experience.add(exp)

		return self.experience.all().first().highlight_color



class Location(models.Model):
	name = models.CharField(max_length=200)
	base_color = models.CharField(max_length=7)
	highlight_color = models.CharField(max_length=7)

	# weeks = models.ManyToManyField('Week', blank=True)

	def __str__(self):
		"""String for representing the Model object."""
		return self.name

class LocationInstance(models.Model):
	"""docstring for LocationInstane"""
	location = models.ForeignKey('Location', on_delete=models.PROTECT, null=True, blank=True)

	start_date = models.DateField()
	end_date = models.DateField()

	TYPE = (
		('l', 'Living'),
		('h', 'Hybrid'),
		('t', 'Travel'),
		('o', 'Other'),
	)

	location_type = models.CharField(
		max_length=1,
		choices=TYPE,
		default='o',
	)

	notes = models.TextField(max_length=1000, blank=True)

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.location.name} ({self.start_date.strftime("%Y/%m/%d")} - {self.end_date.strftime("%Y/%m/%d")})'
		


class ExperienceInstance(models.Model):
	name = models.CharField(max_length=200)
	subname = models.CharField(max_length=200, blank=True)
	
	TYPE = (
		('w', 'Work'),
		('e', 'Education'),
		('o', 'Other'),
		)

	experience_type = models.CharField(
		max_length=1,
		choices=TYPE,
		default='o',
		)
	
	start_date = models.DateField()
	end_date = models.DateField()

	base_color = models.CharField(max_length=7)
	highlight_color = models.CharField(max_length=7)
	
	notes = models.TextField(max_length=1000, blank=True)

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.name} ({self.start_date.strftime("%Y/%m/%d")} - {self.end_date.strftime("%Y/%m/%d")})'
