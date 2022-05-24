#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 06:51:10 2022

@author: tanjameyer
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="view 1"),
    ]
