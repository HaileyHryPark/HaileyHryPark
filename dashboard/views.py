from django.shortcuts import render
from .models import Week, Location, Experience

# Create your views here.
def index(request):
	context = {
		'year_range': range(80),
        'week_range': range(52),
	}

	return render(request, 'index.html', context=context)