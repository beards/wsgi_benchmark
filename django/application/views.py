#!/usr/bin/env python

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world! It's is Django!")

