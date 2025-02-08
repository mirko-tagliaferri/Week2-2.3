#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 16:50:46 2025

@author: ntoni15
"""

web_data = ["techresearch and computervision"]

if "@" in web_data:
    print("e-mail address")
elif "0123456789" in web_data:
    print("phone number")
else:
    print("not e-mail nor phone number")
