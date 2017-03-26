from rest_framework import serializers
from school_finder.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','name','address')