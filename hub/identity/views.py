#hub imports
from identity.connector.FileConnector import DelimitedFileConnector

#django imports
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    delimFile = DelimitedFileConnector()
    delimFile.importUsersFull()
    return HttpResponse("Hello, world!")