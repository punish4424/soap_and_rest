from django.urls import path

from apps.task import views

urlpatterns = [
    path("soap", views.XMLtoJSONAPIView.as_view(), name="soap_api"),
    path("rest", views.RestAPIView.as_view(), name="rest_api"),
]
