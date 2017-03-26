from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from school_finder.models import School
from school_finder.serializers import SchoolSerializer


class ListCreateSchool(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
