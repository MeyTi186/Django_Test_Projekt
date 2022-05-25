#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 06:51:10 2022

@author: tanjameyer
"""

from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    ]
