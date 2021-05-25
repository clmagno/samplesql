# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Experience

# Create your views here.
def home(self):
	return render (request=self, template_name= 'main/index.html', context={'experiences':Experience.objects.order_by('start_date')[::-1]})