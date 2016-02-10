from django.shortcuts import render
from django.utils import timezone
from .models import Project

def portfolio_list(request):
    projects = Project.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'portfolio/portfilio_list.html', {'projects': projects})
