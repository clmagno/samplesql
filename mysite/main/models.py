# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    job_company = models.CharField(max_length=250)
    job_desc = models.TextField()
    start_date = models.DateField("Date Hired")
    def __str__(self):
        return self.job_title
