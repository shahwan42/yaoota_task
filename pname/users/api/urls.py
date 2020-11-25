from django.urls.conf import path


from .views import SignUpApi

app_name = "users_api"

urlpatterns = [
    path("signup/", SignUpApi.as_view(), name="signup"),
]
