from .models import KPAformdata
from rest_framework.serializers import ModelSerializer

class KPAserializer(ModelSerializer):
    class Meta:
        model = KPAformdata
        fields = '__all__'
        read_only_fields = ['user', 'submitted_at']
    
    def validate_age(self, value):
        if value < 0 or value > 120:
            raise ModelSerializer.ValidationError('Invalid Age')
        return value
