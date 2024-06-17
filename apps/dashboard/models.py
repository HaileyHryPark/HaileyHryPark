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

	def get_location_label(self):
		loc = LocationInstance.objects.all().filter(start_date__lte=self.start_date, end_date__gte=self.start_date) | LocationInstance.objects.all().filter(start_date__gte=self.start_date, end_date__lte=self.end_date) | LocationInstance.objects.all().filter(start_date__gte=self.start_date, start_date__lte=self.end_date) | LocationInstance.objects.all().filter(end_date__gte=self.start_date, end_date__lte=self.end_date)
		return "\n".join(location.format_location_label() for location in loc)

	def get_experience_label(self):
		exp = ExperienceInstance.objects.all().filter(start_date__lte=self.start_date, end_date__gte=self.start_date) | ExperienceInstance.objects.all().filter(start_date__gte=self.start_date, end_date__lte=self.end_date) | ExperienceInstance.objects.all().filter(start_date__gte=self.start_date, start_date__lte=self.end_date) | ExperienceInstance.objects.all().filter(end_date__gte=self.start_date, end_date__lte=self.end_date)
		return "\n".join(experience.format_experience_label() for experience in exp)

	def get_location_color(self):
		loc = LocationInstance.objects.all().filter(start_date__lte=self.start_date, end_date__gte=self.start_date) | LocationInstance.objects.all().filter(start_date__gte=self.start_date, end_date__lte=self.end_date) | LocationInstance.objects.all().filter(start_date__gte=self.start_date, start_date__lte=self.end_date) | LocationInstance.objects.all().filter(end_date__gte=self.start_date, end_date__lte=self.end_date)
		current_loc = LocationInstance.objects.all().filter(location_type__exact = 'l').order_by("-end_date").first()
		## Progressive update for the current location
		if (self.end_date > current_loc.end_date) & (current_loc not in loc):	
			current_loc.end_date = self.end_date
			current_loc.save()
			self.location.add(loc)

		elif loc.count() == 0:
			return "#f4f4f4"

		## Update if there is any addition to experience instances
		elif self.location.count() < loc.count():
			""" if the week is not associated with any l location instance """
			self.location.set(loc)

		return self.location.all().order_by("-location_type").first().location.base_color

	def get_location_color_highlight(self):
		loc = LocationInstance.objects.all().filter(start_date__lte=self.start_date, end_date__gte=self.start_date) | LocationInstance.objects.all().filter(start_date__gte=self.start_date, end_date__lte=self.end_date) | LocationInstance.objects.all().filter(start_date__gte=self.start_date, start_date__lte=self.end_date) | LocationInstance.objects.all().filter(end_date__gte=self.start_date, end_date__lte=self.end_date)
		current_loc = LocationInstance.objects.all().filter(location_type__exact = 'l').order_by("-end_date").first()
		## Progressive update for the current location
		if (self.end_date > current_loc.end_date) & (current_loc not in loc):	
			current_loc.end_date = self.end_date
			current_loc.save()
			self.location.add(loc)

		elif loc.count() == 0:
			return "#f4f4f4"

		## Update if there is any addition to experience instances
		elif self.location.count() < loc.count():
			""" if the week is not associated with any l location instance """
			self.location.set(loc)

		return self.location.all().order_by("-location_type").first().location.highlight_color


	def get_experience_color(self):
		exp = ExperienceInstance.objects.all().filter(start_date__lte=self.start_date, end_date__gte=self.start_date) | ExperienceInstance.objects.all().filter(start_date__gte=self.start_date, end_date__lte=self.end_date) | ExperienceInstance.objects.all().filter(start_date__gte=self.start_date, start_date__lte=self.end_date) | ExperienceInstance.objects.all().filter(end_date__gte=self.start_date, end_date__lte=self.end_date)
		current_exp = ExperienceInstance.objects.all().filter(name__exact = "Duke-NUS Medical School").first()
		## Progressive update for the current experience
		if (self.end_date > current_exp.end_date) & (current_exp not in exp):	
			current_exp.end_date = self.end_date
			current_exp.save()
			self.experience.add(exp)

		elif exp.count() == 0:
			return "#f4f4f4"

		## Update if there is any addition to experience instances
		elif self.experience.count() < exp.count():
			""" if the week is not associated with any l location instance """
			self.experience.set(exp)

		return self.experience.all().order_by("-experience_type").first().base_color

	def get_experience_color_highlight(self):
		exp = ExperienceInstance.objects.all().filter(start_date__lte=self.start_date, end_date__gte=self.start_date) | ExperienceInstance.objects.all().filter(start_date__gte=self.start_date, end_date__lte=self.end_date) | ExperienceInstance.objects.all().filter(start_date__gte=self.start_date, start_date__lte=self.end_date) | ExperienceInstance.objects.all().filter(end_date__gte=self.start_date, end_date__lte=self.end_date)
		current_exp = ExperienceInstance.objects.all().filter(name__exact = "Duke-NUS Medical School").first()
		## Progressive update for the current experience
		if (self.end_date > current_exp.end_date) & (current_exp not in exp):	
			current_exp.end_date = self.end_date
			current_exp.save()
			self.experience.add(exp)

		elif exp.count() == 0:
			return "#f4f4f4"

		## Update if there is any addition to experience instances
		elif self.experience.count() < exp.count():
			""" if the week is not associated with any l location instance """
			self.experience.set(exp)

		return self.experience.all().order_by("-experience_type").first().highlight_color


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
	sublocation = models.CharField(max_length=200, blank=True)

	start_date = models.DateField()
	end_date = models.DateField()

	TYPE = (
		('t', 'Travel'),
		('h', 'Hybrid'),
		('l', 'Living'),
		('o', 'Other'),
	)

	location_type = models.CharField(
		max_length=1,
		choices=TYPE,
		default='o',
	)

	notes = models.TextField(max_length=1000, blank=True)

	def format_location_label(self):
		# if self.location_type == 'l':
		# 	location = f"Lived in {self.location.name}"
		# 	if self.sublocation:
		# 		location += f" ({self.sublocation})"
		# 	return location
		# elif self.location_type == 't':
		# 	location = f"Traveled to {self.location.name}"
		# 	if self.sublocation:
		# 		location += f" ({self.sublocation})"
		# 	return location

		# location = f"{self.location.name}"
		# if self.sublocation:
		# 	location += f" ({self.sublocation})"
		return f"{self.location.name}"	
		
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

	def format_experience_label(self):
		experience = f"{self.name}"
		if self.subname:
			experience += f" ({self.subname})"
		return experience	

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.name} ({self.start_date.strftime("%Y/%m/%d")} - {self.end_date.strftime("%Y/%m/%d")})'
