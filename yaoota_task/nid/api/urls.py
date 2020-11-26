from django.urls import path
from .views import NationalIdCheckApi

app_name = "nid_api"

urlpatterns = [
    path("check/", NationalIdCheckApi.as_view(), name="check"),
]
