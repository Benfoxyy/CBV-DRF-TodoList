from rest_framework import serializers
from main.models import ToDoList

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id','author','content','created']
        read_only_fields = ['author']
    def create(self, validated_data):
        validated_data['author'] = self.context.get('request').user
        return super().create(validated_data)