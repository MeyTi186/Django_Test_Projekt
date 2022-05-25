#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 06:38:48 2022

@author: tanjameyer
"""

from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
