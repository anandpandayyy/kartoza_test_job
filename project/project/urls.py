from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from app.forms import UserForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "register/",
        RegistrationView.as_view(form_class=UserForm),
        name="django_registration_register",
    ),
    path("", include('django_registration.backends.one_step.urls')),
    url(r"^login/$", auth_views.LoginView.as_view(), name="login"),
]
