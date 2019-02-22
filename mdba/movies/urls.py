#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:04:14 2019

This is the urls file for the "movies" app.

@author: Akshay Rajmane
"""

from django.urls import include, path

from . import views

urlpatterns = [
                path('', views.index, name='index'),
                path('<int:movie_idx>/', views.detail, name='detail'),
                path('search/', views.search, name='search'),
                path('accounts/', include('django.contrib.auth.urls')),
                path('signup/', views.SignUp.as_view(), name='signup')
              ]
