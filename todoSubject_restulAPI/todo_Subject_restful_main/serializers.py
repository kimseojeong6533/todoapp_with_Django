# 객체와 같이 보기힘든 데이터를 JSON이나 XML처럼 보기쉽게 데이터를 바꾸어 통신하게 해주는 역할을 하는 파일

from .models import TodoList
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=TodoList
        fields=('no','title','content','is_complete','end_date','priority')
