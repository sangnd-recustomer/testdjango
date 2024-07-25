from django.urls import path

from .views import upload, sendmail

urlpatterns = [
    path('upload/', upload, name='test_upload'),
    path('sendmail/', sendmail, name='test_sendmail'),
]
