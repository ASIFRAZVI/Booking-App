from django.urls import path
from apps.authentication_app.views import Registration, Login

urlpatterns=[
    path('signup/', Registration.as_view(), name="signupuser" ),
    path('signin/', Login.as_view(), name="Loginuser"),
]