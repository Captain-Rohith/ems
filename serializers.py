from rest_framework import serializers
from events1.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'short_description', 'date', 'time', 'location', 'image']