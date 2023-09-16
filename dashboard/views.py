from django.shortcuts import render
from .models import Week, Location, Experience
from datetime import date, time, datetime, timedelta

# Create your views here.
def index(request):
	weeks = Week.objects.all()

	# year_list = [str(i) for i in range(1998,2077)]
	# week_count = [Week.objects.filter(start_date__year=year).count() for year in year_list]

	# year_week_count = {year_list[i]: week_count[i] for i in range(len(year_list))}

	current_date = datetime.now().date()
	current_week_num = Week.objects.get(start_date__lte=current_date, end_date__gte=current_date).week_num
	total_week_count = Week.objects.all().count()

	year_week_count = {str(i)[-2:]: Week.objects.filter(start_date__year=str(i)).all() for i in range(1998,2078)}

	context = {
		'current_week_num' : current_week_num,
		'total_week_count' : total_week_count,
		'year_week_count': year_week_count,
	}

	return render(request, 'index.html', context=context)