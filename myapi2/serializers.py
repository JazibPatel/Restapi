from django.db.models import fields
from rest_framework import serializers
from .models import Employs

class EmploySerializre(serializers.ModelSerializer):

    class Meta:

        model = Employs
        fields = '__all__'