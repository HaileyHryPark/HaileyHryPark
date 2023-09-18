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

	location = models.ManyToManyField('LocationInstance', blank=True)

	experience = models.ManyToManyField('ExperienceInstance', blank=True)

	log = models.TextField(max_length=1000, blank=True)

	def __str__(self):
		"""String for representing the Model object."""
		return f'Week {self.id}'

	def get_absolute_url(self):
		"""Returns the URL to access a detail record for this week."""
		return reverse('week-detail', args=[str(self.id)])

	# def update_week(self):

    # def display_calendar_name(self):
    #     """Create a string for the Calendar Name. """
    #     return f'Week {self.week_of_month}, {self.month.name} {self.year.name}'



class Location(models.Model):
	name = models.CharField(max_length=200)
	color = models.CharField(max_length=7)

	# weeks = models.ManyToManyField('Week', blank=True)

	def __str__(self):
		"""String for representing the Model object."""
		return self.name

class LocationInstance(models.Model):
	"""docstring for LocationInstane"""
	location = models.ForeignKey('Location', on_delete=models.PROTECT, null=True)

	start_date = models.DateField()
	end_date = models.DateField()

	notes = models.TextField(max_length=1000, blank=True)

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.location.name} ({self.location.start_date.strftime("%Y/%m/%d")} - {self.location.end_date.strftime("%Y/%m/%d")})'
		


class Experience(models.Model):
	name = models.CharField(max_length=200)
	color = models.CharField(max_length=7)

	# weeks = models.ManyToManyField('Week', blank=True)

	TYPE = (
        ('e', 'Education'),
        ('w', 'Work'),
        ('o', 'Other'),
    )

	experience_type = models.CharField(
        max_length=1,
        choices=TYPE,
        blank=True,
        default='o',
    )

	def __str__(self):
		"""String for representing the Model object."""
		return self.name


class ExperienceInstance(models.Model):
	"""docstring for LocationInstane"""
	experience = models.ForeignKey('Experience', on_delete=models.PROTECT, null=True)

	start_date = models.DateField()
	end_date = models.DateField()

	# notes = models.TextField(max_length=1000, blank=True)

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.experience.name} ({self.experience.start_date.strftime("%Y/%m/%d")} - {self.experience.end_date.strftime("%Y/%m/%d")})'
