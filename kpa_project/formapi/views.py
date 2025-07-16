from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import KPAserializer
from .models import KPAformdata

class SubmitKPAForm(CreateAPIView):
    queryset = KPAformdata.objects.all()
    serializer_class = KPAserializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserKPAFormView(ListAPIView):
    serializer_class = KPAserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return KPAformdata.objects.filter(user=self.request.user)
    


    