from django.urls import path
from .views import SubmitKPAForm,UserKPAFormView

urlpatterns = [
        path('form/submit', SubmitKPAForm.as_view(),name='submit-kpa-form'),
        path('form/userdata', UserKPAFormView.as_view(),name='user-kpa-form'),
]