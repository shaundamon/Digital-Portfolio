from rest_framework import serializers
from info.models import DataScienceConsultingRequest, RoboticProcessAutomationRequest, Event, Blog

class DataScienceConsultingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataScienceConsultingRequest
        fields = '__all__'

class RoboticProcessAutomationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoboticProcessAutomationRequest
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'