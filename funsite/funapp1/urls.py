# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:34:17 2018

@author: john3
"""
from django.urls import path
from . import views



urlpatterns = [
    path("funapp1/", views.index, name="index"),
]
