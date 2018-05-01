from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Profile, Courses
from .forms import ProfileForm
from .tables import CourseTable, RegisteredTable
import sys

# Create your views here.

@login_required
@transaction.atomic
def get_parameters(request):
    data = dict()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            data['is_valid'] = True
        else:
            messages.error(request, 'Please correct the error below.')
            data['is_valid'] = False
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    
    return JsonResponse(data)

@login_required
def CourseView(request):
    table = CourseTable(Courses.objects.all())
    subject = Courses.objects.values("subject").distinct()
    
    if request.method == "POST":
        request.method == ''
        print("HELLOOOOOOOO", file=sys.stderr)
    #    p = optimize()
    #else:
    p = list(Profile.objects.values_list('coursePlan', flat=True))[0]
    print(p, file=sys.stderr)
    objs = Courses.objects.none()    
    for j in p['Fall 2018']:
        #print(j[0], file=sys.stderr)
        objs = objs | Courses.objects.filter(crse = j[1], subject = j[0])
    fall_2018 = RegisteredTable(objs, attrs = {'id':'fall-2018'}, row_attrs={'class':'fall-2018'})
    #print(objs, file=sys.stderr)
    objs = Courses.objects.none()
    #print(RegisteredTable, file=sys.stderr)    
    for j in p['Spring 2019']:
        #print(j[0], file=sys.stderr)
        objs = objs | Courses.objects.filter(crse = j[1], subject = j[0])
    spring_2019 = RegisteredTable(objs, attrs = {'id':'spring-2019'}, row_attrs={'class':'spring-2019'})
    
    return render(request, 'course.html', {'course':table, 'subject':subject, 'fall_2018': fall_2018, 'spring_2019' : spring_2019})
"""
def optimize():
    p = list(Profile.objects.values_list('coursePlan', flat=True))[0]
    challenge = list(Profile.objects.values_list('challenge'))[0][0]
    hrsPerWeek = list(Profile.objects.values_list('hrsPerWeek'))[0][0]
    print(challenge, file=sys.stderr)
    print(hrsPerWeek, file=sys.stderr)
    objs = Courses.objects.none()
    for j in p['Fall 2018']:
        objs = Courses.objects.filter(crse = j[1], subject = j[0])
    print(objs.values())
"""





