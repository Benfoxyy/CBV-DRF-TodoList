from rest_framework import serializers
from main.models import ToDoList

class ToDoSerializer(serializers.ModelSerializer):
    related_url = serializers.URLField(source='get_related_url',read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    class Meta:
        model = ToDoList
        fields = ['id','author','content','related_url','absolute_url','created']
        read_only_fields = ['author']

    def create(self, validated_data):
        validated_data['author'] = self.context.get('request').user
        return super().create(validated_data)

    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)