
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction

from rest_framework import exceptions, serializers, status, generics
from .models import *

from django.contrib.auth.tokens import default_token_generator


import logging
logger = logging.getLogger(__name__)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Column
        fields = '__all__'




class ParamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Param
        fields = '__all__'

class RecordParamSerializer(serializers.ModelSerializer):
    param = ParamSerializer(many=False, required=False, read_only=True)
    class Meta:
        model = RecordParam
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    params = RecordParamSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Record
        fields = '__all__'


class TabSerializer(serializers.ModelSerializer):
    records = RecordSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Tab
        fields = '__all__'

















