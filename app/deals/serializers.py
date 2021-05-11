from rest_framework import serializers
from .models import File
from .models import Test

class DealsSerializer(serializers.Serializer):
  customer = serializers.CharField(max_length=50)
  item = serializers.CharField(max_length=50)
  total = serializers.IntegerField()
  quantity = serializers.IntegerField()
  date = serializers.DateTimeField()

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('deals',)

class TestSer(serializers.ModelSerializer):
  username = serializers.CharField(source='customer')
  spent_money = serializers.IntegerField(source='total__sum')
  gems = serializers.CharField(source='turophile')
  class Meta:
    model = Test
    fields = ('username','spent_money','gems')
